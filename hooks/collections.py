"""MkDocs hook for the Punched In design wiki.

Responsibilities:

* read the frontmatter of every collection entry and validate it against the
  schemas below (problems are logged as warnings, so `--strict` fails);
* replace `<!-- collection: NAME -->` markers with the generated index of that
  collection, and `<!-- recently-added -->` with the latest changed entries;
* add automatic `rarity:`, `type:`, `category:` and `status:` tags to entries;
* insert a metadata header under the H1 of every entry page.

Nothing is ever written back to the source files.
"""

from __future__ import annotations

import datetime as dt
import html
import json
import logging
import os
import posixpath
import re
import subprocess
from dataclasses import dataclass, field

import yaml
from mkdocs.structure.files import File
from mkdocs.structure.pages import Page

log = logging.getLogger("mkdocs.plugins.punched_in")

# --------------------------------------------------------------------------
# Schemas
# --------------------------------------------------------------------------

TBD = "TBD"
STATUSES = ("idea", "approved", "implemented", "cut")
DECISION_STATUSES = ("proposed", "accepted", "superseded")
RARITIES = ("common", "rare", "legendary", "cursed")
RARITIES_NOT_CURSED = ("common", "rare", "legendary")

# Character categories, in the order the characters index lists them.
CHARACTER_CATEGORIES = ("player", "boss", "minion", "shopkeeper", "npc")
CATEGORY_HEADINGS = {"player": "Player", "boss": "Bosses", "minion": "Minions",
                     "shopkeeper": "Shopkeepers", "npc": "NPCs"}

# Biomes are listed in this order; biomes not in the list come after, A–Z.
BIOME_ORDER = ("shark", "fox", "old-raccoon", "sloth", "snake")

# Files inside a collection folder that are pages, not entries.
NOT_ENTRIES = {"index.md", "open-questions.md"}

# Frontmatter keys understood by Material for MkDocs itself; allowed anywhere.
MATERIAL_KEYS = {"title", "description", "hide", "icon", "search", "template"}

# Index pages that Material's `navigation.indexes` may use as the landing page
# of their nav section. See `on_nav`.
SECTION_LANDING_PAGES: set[str] = set()


@dataclass(frozen=True)
class Field:
    kind: str  # "str", "list" (list of str), "date" or "enum"
    required: bool = False
    # Allowed values for "enum". `None` means "the item types from mkdocs.yml".
    choices: tuple[str, ...] | None = ()
    default: str | None = None


SHARED = {
    "name": Field("str", required=True),
    "status": Field("enum", required=True, choices=STATUSES),
    "author": Field("str"),
    "tags": Field("list"),
    "summary": Field("str"),
}


SLUG = r"[a-z0-9]+(?:-[a-z0-9]+)*"


@dataclass(frozen=True)
class Collection:
    key: str  # folder name under docs/
    singular: str
    template: str  # file name in _templates/
    fields: dict[str, Field]
    slug_pattern: str = SLUG  # filename without .md
    slug_example: str = "lowercase-words-with-dashes.md"


COLLECTIONS = {
    c.key: c
    for c in (
        Collection(
            "menu-items", "Menu item", "menu-item.md",
            {
                **SHARED,
                "rarity": Field("enum", required=True, choices=RARITIES),
                "type": Field("enum", required=True, choices=None),
                "cursed_with": Field("str"),
            },
        ),
        Collection(
            "consumables", "Consumable", "consumable.md",
            {
                **SHARED,
                "rarity": Field("enum", choices=RARITIES_NOT_CURSED),
                "shop": Field("enum", choices=("dish-pit",), default="dish-pit"),
            },
        ),
        Collection(
            "relics", "Relic", "relic.md",
            {
                **SHARED,
                "rarity": Field("enum", choices=RARITIES_NOT_CURSED),
                "shop": Field("enum", choices=("bar",), default="bar"),
            },
        ),
        Collection("keywords", "Keyword", "keyword.md", dict(SHARED)),
        Collection(
            "biomes", "Biome", "biome.md",
            {**SHARED, "boss": Field("str", required=True)},
        ),
        Collection(
            "characters", "Character", "character.md",
            {
                **SHARED,
                "category": Field("enum", required=True, choices=CHARACTER_CATEGORIES),
                "biome": Field("str"),
            },
        ),
        Collection(
            "playtests", "Playtest", "playtest-note.md",
            {
                "name": SHARED["name"],
                "author": SHARED["author"],
                "tags": SHARED["tags"],
                "summary": SHARED["summary"],
                "date": Field("date", required=True),
                "players": Field("list"),
                "build": Field("str"),
            },
            slug_pattern=rf"\d{{4}}-\d{{2}}-\d{{2}}-{SLUG}",
            slug_example="YYYY-MM-DD-short-title.md",
        ),
        Collection(
            "decisions", "Decision", "decision.md",
            {
                **SHARED,
                "status": Field("enum", required=True, choices=DECISION_STATUSES),
                "id": Field("str", required=True),
                "date": Field("date", required=True),
                "decided_by": Field("list"),
                "superseded_by": Field("str"),
            },
            slug_pattern=rf"\d{{4}}-{SLUG}",
            slug_example="NNNN-short-title.md",
        ),
    )
}


# --------------------------------------------------------------------------
# Build state (rebuilt on every build, including `mkdocs serve` reloads)
# --------------------------------------------------------------------------

@dataclass
class Entry:
    collection: Collection
    file: File
    meta: dict
    updated: dt.datetime
    attached_to: list[Entry] = field(default_factory=list)

    @property
    def slug(self) -> str:
        return posixpath.splitext(posixpath.basename(self.file.src_uri))[0]

    @property
    def title(self) -> str:
        name = _text(self.meta.get("name"))
        if self.collection.key == "biomes" and name in ("", TBD):
            boss = _text(self.meta.get("boss"))
            return f"{boss} biome" if boss else self.slug
        return name or self.slug

    def get(self, key: str) -> str:
        """A field as text, or its default, or ""."""
        value = _text(self.meta.get(key))
        spec = self.collection.fields.get(key)
        return value or (spec.default if spec and spec.default else "")

    def date(self) -> dt.date | None:
        return _parse_date(self.meta.get("date"))


_item_types: tuple[str, ...] = ()
_entries: dict[str, list[Entry]] = {}
_by_src: dict[str, Entry] = {}


def _warn(path: str, message: str) -> None:
    log.warning(f"{path}: {message}")


def _text(value) -> str:
    return value.strip() if isinstance(value, str) else ""


def _parse_date(value) -> dt.date | None:
    if isinstance(value, dt.datetime):
        return value.date()
    if isinstance(value, dt.date):
        return value
    if isinstance(value, str) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", value.strip()):
        try:
            return dt.date.fromisoformat(value.strip())
        except ValueError:
            return None
    return None


def _type_name(value) -> str:
    return {
        bool: "true/false", int: "a number", float: "a number",
        list: "a list", dict: "a mapping", dt.date: "a date",
    }.get(type(value), type(value).__name__)


# --------------------------------------------------------------------------
# Reading
# --------------------------------------------------------------------------

FRONTMATTER_RE = re.compile(r"\A---[ \t]*\n(.*?\n)?(?:---|\.\.\.)[ \t]*(?:\n|\Z)", re.S)


def _read_frontmatter(path: str, text: str) -> dict | None:
    """The frontmatter as a dict, or None (after a warning) if it can't be read."""
    match = FRONTMATTER_RE.match(text.replace("\r\n", "\n"))
    if not match:
        _warn(path, "no frontmatter found (the file must start with a '---' line)")
        return None
    try:
        data = yaml.safe_load(match.group(1) or "")
    except yaml.YAMLError as error:
        problem = getattr(error, "problem", None) or str(error)
        mark = getattr(error, "problem_mark", None)
        where = f" on line {mark.line + 2}" if mark else ""
        _warn(path, f"frontmatter is not valid YAML{where}: {problem}")
        return None
    except ValueError as error:  # e.g. an impossible date such as 2026-13-01
        _warn(path, f"frontmatter contains an impossible date ({error})")
        return None
    if data is None:
        return {}
    if not isinstance(data, dict):
        _warn(path, "frontmatter must be a list of 'field: value' lines")
        return None
    return data


def _git_dates(docs_dir: str) -> dict[str, dt.datetime]:
    """Last commit date of every file under docs_dir, keyed by docs-relative path."""
    try:
        out = subprocess.run(
            ["git", "-c", "core.quotePath=false", "log", "--relative",
             "--name-only", "--format=%x00%cI", "--", "."],
            cwd=docs_dir, capture_output=True, text=True, check=True,
        ).stdout
    except (OSError, subprocess.CalledProcessError):
        return {}
    dates: dict[str, dt.datetime] = {}
    current = None
    for line in out.splitlines():
        if line.startswith("\x00"):
            current = dt.datetime.fromisoformat(line[1:])
        elif line and current is not None:
            dates.setdefault(line, current)
    return dates


# --------------------------------------------------------------------------
# Validation
# --------------------------------------------------------------------------

def _validate_field(path: str, key: str, spec: Field, value) -> None:
    if spec.kind == "str":
        if not isinstance(value, str) or not value.strip():
            _warn(path, f"{key} must be a non-empty text value, got {_type_name(value)}")
    elif spec.kind == "list":
        if not isinstance(value, list) or not all(
            isinstance(v, str) and v.strip() for v in value
        ):
            _warn(path, f"{key} must be a list of text values, e.g. [Alice, Bob]")
    elif spec.kind == "date":
        if _parse_date(value) is None:
            _warn(path, f"{key} '{value}' is not a valid date (expected YYYY-MM-DD)")
    elif spec.kind == "enum":
        choices = _item_types if spec.choices is None else spec.choices
        if not isinstance(value, str) or value not in choices:
            where = " (allowed values are set by extra.item_types in mkdocs.yml)" if spec.choices is None else ""
            _warn(path, f"{key} '{value}' is invalid (expected one of: {', '.join(choices)}){where}")


def _validate_entry(entry: Entry) -> None:
    c = entry.collection
    path = entry.file.src_uri
    meta = entry.meta

    filename = posixpath.basename(path)
    if not re.fullmatch(c.slug_pattern + r"\.md", filename):
        _warn(path, f"filename '{filename}' does not follow the naming convention ({c.slug_example})")

    for key, spec in c.fields.items():
        if key not in meta or meta[key] is None:
            if spec.required:
                _warn(path, f"{key} is required but missing")
            continue
        if key in ("id", "superseded_by") and isinstance(meta[key], int):
            _warn(path, f"{key} must be in quotes to keep its leading zeros, e.g. {key}: \"0001\"")
            continue
        _validate_field(path, key, spec, meta[key])

    for key in meta:
        if key not in c.fields and key not in MATERIAL_KEYS:
            _warn(path, f"unknown field '{key}' (allowed: {', '.join(c.fields)})")

    if c.key == "playtests":
        date = entry.date()
        if date and not filename.startswith(date.isoformat()):
            _warn(path, f"date '{date}' does not match the filename prefix '{filename[:10]}'")

    if c.key == "decisions":
        decision_id = meta.get("id")
        if isinstance(decision_id, str) and decision_id:
            if not re.fullmatch(r"\d{4}", decision_id):
                _warn(path, f"id '{decision_id}' must be 4 digits, e.g. 0001")
            elif not filename.startswith(decision_id + "-"):
                _warn(path, f"id '{decision_id}' does not match the filename prefix '{filename[:4]}'")


def _validate_links() -> None:
    items = {e.slug: e for e in _entries["menu-items"]}
    for entry in _entries["menu-items"]:
        target_slug = entry.get("cursed_with")
        if not target_slug:
            continue
        target = items.get(target_slug)
        path = entry.file.src_uri
        if target is None:
            _warn(path, f"cursed_with '{target_slug}' does not match any menu item "
                        "(expected the filename, without .md, of a cursed menu item)")
        elif target.get("rarity") != "cursed":
            _warn(path, f"cursed_with '{target_slug}' points to a menu item whose rarity is "
                        f"'{target.get('rarity')}' (it must be 'cursed')")
        else:
            target.attached_to.append(entry)

    biomes = {e.slug for e in _entries["biomes"]}
    for entry in _entries["characters"]:
        biome = entry.get("biome")
        if biome and biome not in biomes:
            _warn(entry.file.src_uri, f"biome '{biome}' does not match any biome "
                                      "(expected the filename, without .md, of a biome page)")

    decisions: dict[str, Entry] = {}
    for entry in _entries["decisions"]:
        decision_id = entry.get("id")
        if decision_id in decisions:
            _warn(entry.file.src_uri, f"id '{decision_id}' is already used by "
                                      f"{decisions[decision_id].file.src_uri}")
        decisions.setdefault(decision_id, entry)
    for entry in _entries["decisions"]:
        replacement = entry.get("superseded_by")
        if replacement and replacement not in decisions:
            _warn(entry.file.src_uri, f"superseded_by '{replacement}' does not match any decision id")


# --------------------------------------------------------------------------
# Hook events
# --------------------------------------------------------------------------

def on_config(config):
    global _item_types
    types = config.extra.get("item_types")
    if not isinstance(types, list) or not types or not all(isinstance(t, str) for t in types):
        log.warning("mkdocs.yml: extra.item_types must be a non-empty list of text values")
        types = []
    _item_types = tuple(types)


def on_files(files, config):
    _entries.clear()
    _by_src.clear()
    for key in COLLECTIONS:
        _entries[key] = []

    git_dates = _git_dates(config.docs_dir)
    for file in files.documentation_pages():
        folder, filename = posixpath.split(file.src_uri)
        if folder not in COLLECTIONS or filename in NOT_ENTRIES:
            continue
        meta = _read_frontmatter(file.src_uri, file.content_string)
        updated = git_dates.get(file.src_uri) or dt.datetime.fromtimestamp(
            os.path.getmtime(file.abs_src_path), dt.timezone.utc
        )
        entry = Entry(COLLECTIONS[folder], file, meta or {}, updated)
        _entries[folder].append(entry)
        _by_src[file.src_uri] = entry
        if meta is not None:  # unreadable frontmatter was already reported
            _validate_entry(entry)

    _validate_links()
    return files


class _PlainPage(Page):
    """A page that Material's `navigation.indexes` won't turn into a section landing page."""

    @property
    def is_index(self) -> bool:
        return False


def on_nav(nav, config, files):
    # Material treats *any* index.md inside a nav section as that section's
    # landing page. The collection indexes (Keywords, Menu items, Decisions…)
    # are ordinary pages of their tab, so only SECTION_LANDING_PAGES keep it.
    for page in nav.pages:
        if (page.parent is not None and page.file.name == "index"
                and page.file.src_uri not in SECTION_LANDING_PAGES):
            page.__class__ = _PlainPage
    return nav


MARKER_RE = re.compile(r"<!--\s*collection:\s*([\w-]+)\s*-->")
RECENT_RE = re.compile(r"<!--\s*recently-added\s*-->")


def on_page_markdown(markdown, page, config, files):
    src = page.file.src_uri
    folder, filename = posixpath.split(src)

    if filename == "index.md" and folder in COLLECTIONS and not MARKER_RE.search(markdown):
        _warn(src, f"marker <!-- collection: {folder} --> is missing, so the list of entries is not shown")

    def replace(match):
        key = match.group(1)
        if key not in COLLECTIONS:
            _warn(src, f"unknown collection '{key}' in marker (expected one of: {', '.join(COLLECTIONS)})")
            return match.group(0)
        return _render_collection(COLLECTIONS[key], page)

    markdown = MARKER_RE.sub(replace, markdown)
    markdown = RECENT_RE.sub(lambda _: _render_recent(page), markdown)

    entry = _by_src.get(src)
    if entry is not None:
        page.meta["tags"] = _tags(entry)
        markdown = _add_header(markdown, entry, page)
    return markdown


# --------------------------------------------------------------------------
# Rendering helpers
# --------------------------------------------------------------------------

def _esc(value) -> str:
    return html.escape(str(value), quote=True)


def _label(value: str) -> str:
    return value.replace("-", " ").capitalize() if value else ""


def _badge(group: str, value: str) -> str:
    """`group` is rarity, status or decision; unknown values get a neutral badge."""
    known = {"rarity": RARITIES, "status": STATUSES, "decision": DECISION_STATUSES}[group]
    modifier = f" pi-badge--{group}-{value}" if value in known else ""
    return f'<span class="pi-badge{modifier}">{_esc(value)}</span>'


def _status_badge(entry: Entry) -> str:
    group = "decision" if entry.collection.key == "decisions" else "status"
    return _badge(group, entry.get("status")) if entry.get("status") else ""


def _link(entry: Entry, page: Page, text: str | None = None) -> str:
    """HTML link (used inside raw HTML, where MkDocs doesn't rewrite .md links)."""
    url = entry.file.url_relative_to(page.file)
    return f'<a href="{_esc(url)}">{_esc(text or entry.title)}</a>'


def _md_link(entry: Entry, page: Page) -> str:
    """Markdown link to the entry's source file, so MkDocs validates it."""
    rel = posixpath.relpath(entry.file.src_uri, posixpath.dirname(page.file.src_uri) or ".")
    title = entry.title.replace("[", r"\[").replace("]", r"\]")
    return f"[{title}]({rel})"


def _table(headers: list[str], rows: list[tuple[dict, list[str]]], attrs: str = "") -> str:
    """rows: (attributes of the <tr>, already-escaped cell HTML)."""
    head = "".join(f"<th>{_esc(h)}</th>" for h in headers)
    body = []
    for row_attrs, cells in rows:
        attr_html = "".join(f' {k}="{_esc(v)}"' for k, v in row_attrs.items())
        body.append(f"<tr{attr_html}>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>")
    return (f"<div{attrs}>\n<table>\n<thead><tr>{head}</tr></thead>\n<tbody>\n"
            + "\n".join(body) + "\n</tbody>\n</table>\n</div>")


def _order(values: tuple[str, ...], value: str) -> int:
    return values.index(value) if value in values else len(values)


def _sorted(c: Collection) -> list[Entry]:
    entries = _entries[c.key]
    by_title = lambda e: e.title.casefold()
    if c.key in ("menu-items", "consumables", "relics"):
        return sorted(entries, key=lambda e: (_order(RARITIES, e.get("rarity")), by_title(e)))
    if c.key == "biomes":
        return sorted(entries, key=lambda e: (_order(BIOME_ORDER, e.slug), by_title(e)))
    if c.key == "characters":
        # Characters without a biome (the Pig, shopkeepers…) come after the biomes.
        return sorted(entries, key=lambda e: (_order(BIOME_ORDER, e.get("biome")),
                                              not e.get("biome"), by_title(e)))
    if c.key == "playtests":
        return sorted(entries, key=lambda e: (e.date() or dt.date.min, e.slug), reverse=True)
    if c.key == "decisions":
        return sorted(entries, key=lambda e: (e.date() or dt.date.min, e.get("id")), reverse=True)
    return sorted(entries, key=by_title)


def _render_collection(c: Collection, page: Page) -> str:
    entries = _sorted(c)
    if not entries:
        return (f"*No entries yet.* To add one, copy `_templates/{c.template}` "
                f"to `docs/{c.key}/` and follow the instructions at the top of the file.")

    if c.key in ("menu-items", "consumables", "relics"):
        return _render_filterable(c, entries, page)

    if c.key == "characters":
        return _render_characters(entries, page)

    if c.key == "keywords":
        lines = []
        for e in entries:
            summary = f" — {e.get('summary')}" if e.get("summary") else ""
            lines.append(f"- **{_md_link(e, page)}** {_status_badge(e)}{summary}")
        return "\n".join(lines)

    if c.key == "biomes":
        cards = []
        for e in entries:
            boss = _boss_character(e)
            boss_html = _link(boss, page) if boss else _esc(e.get("boss") or TBD)
            # Minions in the order the biome page presents them (Minion 1, 2, 3).
            source = e.file.content_string
            minions = sorted(
                (m for m in _entries["characters"]
                 if m.get("biome") == e.slug and m.get("category") == "minion"),
                # A minion the page never links to sorts last (find() returns -1).
                key=lambda m: (source.find(f"characters/{m.slug}.md") % (len(source) + 1),
                               m.title.casefold()),
            )
            minions_html = ", ".join(_link(m, page) for m in minions) or TBD
            summary = f"    {_esc(e.get('summary'))}\n\n" if e.get("summary") else ""
            cards.append(
                f"-   :material-map-outline:{{ .lg .middle }} **{_md_link(e, page)}**\n\n"
                f"    ---\n\n"
                f"{summary}"
                f"    Boss: {boss_html}<br>\n"
                f"    Minions: {minions_html}\n\n"
                f"    {_status_badge(e)}\n"
            )
        return '<div class="grid cards" markdown>\n\n' + "\n".join(cards) + "\n</div>"

    if c.key == "playtests":
        rows = [({}, [
            _esc(e.date() or e.meta.get("date", "")),
            _link(e, page),
            _esc(", ".join(e.meta["players"])) if isinstance(e.meta.get("players"), list) else "",
            _esc(e.get("build")),
        ]) for e in entries]
        return _table(["Date", "Name", "Players", "Build"], rows)

    # decisions
    ids = {e.get("id"): e for e in _entries["decisions"]}
    rows = []
    for e in entries:
        status = _status_badge(e)
        title = _link(e, page)
        attrs = {}
        if e.get("status") == "superseded":
            attrs["class"] = "pi-superseded"
            title = f"<del>{title}</del>"
            replacement = ids.get(e.get("superseded_by"))
            if replacement is not None:
                status += " by " + _link(replacement, page, replacement.get("id"))
        rows.append((attrs, [_esc(e.get("id")), _esc(e.date() or e.meta.get("date", "")), title, status]))
    return _table(["Id", "Date", "Title", "Status"], rows)


def _boss_character(biome: Entry) -> Entry | None:
    """The boss character page of a biome, if there is one."""
    return next((e for e in _entries["characters"]
                 if e.get("biome") == biome.slug and e.get("category") == "boss"), None)


def _render_characters(entries: list[Entry], page: Page) -> str:
    biomes = {e.slug: e for e in _entries["biomes"]}
    sections = []
    for category in CHARACTER_CATEGORIES:
        group = [e for e in entries if e.get("category") == category]
        sections.append(f"## {CATEGORY_HEADINGS[category]}\n")
        if not group:
            sections.append("*None yet.*\n")
            continue
        rows = []
        for e in group:
            biome = biomes.get(e.get("biome"))
            rows.append(({}, [_link(e, page), _link(biome, page) if biome else "—",
                              _status_badge(e), _esc(e.get("summary"))]))
        sections.append(_table(["Name", "Biome", "Status", "Summary"], rows) + "\n")
    return "\n".join(sections)


def _render_filterable(c: Collection, entries: list[Entry], page: Page) -> str:
    is_menu = c.key == "menu-items"
    rarities = RARITIES if is_menu else RARITIES_NOT_CURSED

    groups = [{"key": "rarity", "label": "Rarity",
               "options": [[r, _label(r)] for r in rarities]}]
    if not is_menu:
        groups[0]["options"].append(["none", "Not set"])
    if is_menu:
        groups.append({"key": "type", "label": "Type",
                       "options": [[t, t] for t in _item_types]})
    groups.append({"key": "status", "label": "Status",
                   "options": [[s, _label(s)] for s in STATUSES]})

    items = {e.slug: e for e in _entries["menu-items"]}
    rows = []
    for e in entries:
        rarity = e.get("rarity")
        cells = [_link(e, page), _badge("rarity", rarity) if rarity else "—"]
        if is_menu:
            cells.append(_esc(e.get("type")))
        cells += [_status_badge(e), _esc(e.get("summary"))]
        if is_menu:
            target = items.get(e.get("cursed_with"))
            cells.append(_link(target, page) if target else _esc(e.get("cursed_with")))
        attrs = {"data-name": e.title, "data-summary": e.get("summary"),
                 "data-rarity": rarity or "none", "data-status": e.get("status")}
        if is_menu:
            attrs["data-type"] = e.get("type")
        rows.append((attrs, cells))

    headers = ["Name", "Rarity"] + (["Type"] if is_menu else []) + ["Status", "Summary"]
    if is_menu:
        headers.append("Cursed with")
    noun = {"menu-items": "items", "consumables": "consumables", "relics": "relics"}[c.key]
    attrs = (f' class="pi-collection" data-pi-noun="{noun}"'
             f' data-pi-filters="{_esc(json.dumps(groups))}"')
    return _table(headers, rows, attrs)


def _render_recent(page: Page) -> str:
    entries = sorted(_by_src.values(), key=lambda e: e.updated, reverse=True)[:10]
    if not entries:
        return "*No entries yet.*"
    return "\n".join(
        f"- {_md_link(e, page)} — {e.collection.singular} · {e.updated:%Y-%m-%d}"
        for e in entries
    )


def _tags(entry: Entry) -> list[str]:
    tags = entry.meta.get("tags")
    tags = [t for t in tags if isinstance(t, str)] if isinstance(tags, list) else []
    for key in ("rarity", "type", "category", "status"):
        if key in entry.collection.fields and entry.get(key):
            tags.append(f"{key}:{entry.get(key)}")
    return list(dict.fromkeys(tags))


def _header(entry: Entry, page: Page) -> str:
    c, meta = entry.collection, entry.meta
    parts = []

    def add(label: str, value_html: str) -> None:
        if value_html:
            parts.append(f'<span class="pi-meta__item"><span class="pi-meta__label">{label}</span> {value_html}</span>')

    def join(key: str) -> str:
        value = meta.get(key)
        return _esc(", ".join(v for v in value if isinstance(v, str))) if isinstance(value, list) else ""

    if c.key == "decisions":
        add("Decision", _esc(entry.get("id")))
    if "rarity" in c.fields and entry.get("rarity"):
        add("Rarity", _badge("rarity", entry.get("rarity")))
    if "type" in c.fields:
        add("Type", _esc(entry.get("type")))
    if "category" in c.fields:
        add("Category", _esc("NPC" if entry.get("category") == "npc" else _label(entry.get("category"))))
    if c.key == "characters" and entry.get("biome"):
        target = next((e for e in _entries["biomes"] if e.slug == entry.get("biome")), None)
        add("Biome", _link(target, page) if target else _esc(entry.get("biome")))
    if "status" in c.fields:
        add("Status", _status_badge(entry))
    if "shop" in c.fields:
        add("Shop", _esc(_label(entry.get("shop"))))
    if "boss" in c.fields:
        boss = _boss_character(entry)
        add("Boss", _link(boss, page) if boss else _esc(entry.get("boss")))
    if "date" in c.fields:
        add("Date", _esc(entry.date() or meta.get("date", "")))
    add("Players", join("players"))
    add("Build", _esc(entry.get("build")) if "build" in c.fields else "")
    add("Decided by", join("decided_by"))
    add("Author", _esc(entry.get("author")))
    if c.key == "menu-items" and entry.get("cursed_with"):
        target = next((e for e in _entries["menu-items"] if e.slug == entry.get("cursed_with")), None)
        add("Cursed with", _link(target, page) if target else _esc(entry.get("cursed_with")))
    if c.key == "decisions" and entry.get("superseded_by"):
        target = next((e for e in _entries["decisions"] if e.get("id") == entry.get("superseded_by")), None)
        add("Superseded by", _link(target, page) if target else _esc(entry.get("superseded_by")))

    out = f'<div class="pi-meta">{"".join(parts)}</div>'
    if entry.attached_to:
        links = ", ".join(_link(e, page) for e in sorted(entry.attached_to, key=lambda e: e.title.casefold()))
        out += f'\n\n<p class="pi-attached"><strong>Comes attached to:</strong> {links}</p>'
    return out


def _add_header(markdown: str, entry: Entry, page: Page) -> str:
    """Insert the metadata header after the first H1, adding an H1 if there is none."""
    lines = markdown.split("\n")
    fence = None
    h1_end = None
    for i, line in enumerate(lines):
        stripped = line.lstrip()
        if fence:
            if stripped.startswith(fence):
                fence = None
            continue
        if stripped.startswith(("```", "~~~")):
            fence = stripped[:3]
            continue
        if re.match(r"#(?!#)\s*\S", line):
            h1_end = i + 1
            break
        if line.strip() and i + 1 < len(lines) and re.fullmatch(r"=+\s*", lines[i + 1]):
            h1_end = i + 2
            break

    header = _header(entry, page)
    if h1_end is None:
        title = entry.title.replace("#", r"\#")
        return f"# {title}\n\n{header}\n\n{markdown}"
    return "\n".join(lines[:h1_end]) + f"\n\n{header}\n\n" + "\n".join(lines[h1_end:])
