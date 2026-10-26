# Punched In — Design Wiki

## 1. What this is

The internal design wiki for **Punched In**, a roguelike built on classic
backgammon with a restaurant-kitchen theme. The game itself is developed in
Godot 4 in a separate repository; this repository contains **only the design
wiki**.

The wiki is a [MkDocs](https://www.mkdocs.org/) site using
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/). Content is
written as Markdown files in `docs/`, edited locally and pushed to git; GitHub
Actions rebuilds the site and publishes it to GitHub Pages.

A small hook, `hooks/collections.py`, does the bookkeeping:

- builds the index of every collection (menu items, relics, playtests…) from
  the files in its folder;
- checks every entry's frontmatter and warns about mistakes;
- tags each entry with its rarity, type, category and status;
- adds a metadata line (rarity, type, status, author…) under each entry's title;
- lists the 10 most recently changed entries on the home page;
- shows each biome's boss and minions on its card, linked to their character
  pages.

So adding content never requires editing anything but the new file.

## 2. Run locally

Requires Python 3.12.

```bash
python3.12 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
mkdocs serve
```

Open <http://127.0.0.1:8000>. It redirects to the site's path (the path part
of `site_url` in `mkdocs.yml`). The page reloads when you save a file;
validation warnings appear in the terminal.

`mkdocs build --strict` runs the same build as CI: it fails on any warning.

> Versions are pinned in `requirements.txt` on purpose. Material for MkDocs
> prints a notice about MkDocs 2.0, which will not support plugins or hooks;
> this wiki stays on MkDocs 1.6.

## 3. Adding content

The workflow is the same for every collection:

1. Copy the template from `_templates/` into the collection's folder in `docs/`.
2. Rename it following the naming convention (below).
3. Fill in the frontmatter (the block between the two `---` lines) and the body.
   Optional fields are commented out with `# `; remove the `# ` to use one.
4. Delete the instructions comment at the top of the body.
5. Run `mkdocs serve` to check there are no warnings, then commit and push.

The entry then shows up in its collection index, on the Tags page, in "Recently
added" and in search. Individual entries are not listed in the navigation
sidebar; they are reached through their index, tags and search.

**Filenames** are the entry's *slug*: its name in lowercase ASCII, words
separated by `-` (e.g. `beef-tartare.md`). Playtest notes are named
`YYYY-MM-DD-short-title.md`, decisions `NNNN-short-title.md` (4-digit,
zero-padded id).

The frontmatter blocks below are **examples** with placeholder values, not
real game content.

### Menu items

Template `_templates/menu-item.md` → `docs/menu-items/<slug>.md`.
Required: `name`, `rarity`, `type`, `status`.

```yaml
---
name: Example item
rarity: rare
type: TBD
status: idea
cursed_with: example-cursed-item   # optional
author: Example author             # optional
tags: [example-tag]                # optional
summary: One line shown in the index table.   # optional
---
```

`cursed_with` is the filename (without `.md`) of the cursed menu item that
comes attached to this one. That item must exist and have `rarity: cursed`; its
page then shows "Comes attached to: Example item".

### Consumables

Template `_templates/consumable.md` → `docs/consumables/<slug>.md`.
Required: `name`, `status`.

```yaml
---
name: Example consumable
status: idea
rarity: common       # optional: common, rare or legendary
shop: dish-pit       # optional, dish-pit is the default
---
```

### Relics

Template `_templates/relic.md` → `docs/relics/<slug>.md`.
Required: `name`, `status`.

```yaml
---
name: Example relic
status: idea
rarity: legendary    # optional: common, rare or legendary
shop: bar            # optional, bar is the default
---
```

### Keywords

Template `_templates/keyword.md` → `docs/keywords/<slug>.md`.
Required: `name`, `status`. The index lists keywords alphabetically.

```yaml
---
name: Example keyword
status: idea
summary: One-line definition shown in the index.
---
```

### Biomes

Template `_templates/biome.md` → `docs/biomes/<slug>.md`.
Required: `name`, `boss`, `status`.

```yaml
---
name: TBD
boss: The Example Boss
status: idea
---
```

Do not add an H1: the title is generated from `name`, or "`<boss>` biome"
while `name` is `TBD`. The five main biomes are listed in a fixed order
(Shark, Fox, Old Raccoon, Sloth, Snake); other biomes come after them,
alphabetically. The five main biome pages are also in the navigation sidebar
(`nav` in `mkdocs.yml`); a new biome page only needs adding there if it should
appear in the sidebar too.

Every biome page follows the same layout (overview and biome rule, boss,
minions 1–3, game notes, design notes); `docs/biomes/shark.md` is the
reference example. Also add a character page for the boss and each minion,
with `biome:` set to the biome's slug: the biome's card on the Biomes page
then links the boss and lists the minions automatically, in the order the
biome page links to them. The card also shows the biome's `summary`.

### Characters

Template `_templates/character.md` → `docs/characters/<slug>.md`.
Required: `name`, `category`, `status`. The index groups characters by
category (Player, Bosses, Minions, Shopkeepers, NPCs), then by biome.

```yaml
---
name: Example character
category: minion       # player, boss, minion, shopkeeper or npc
status: idea
biome: example-biome   # optional
---
```

`biome` is the filename (without `.md`) of the character's biome page; it
must exist. Keep the "Starting menu", "Starting relic/consumables" and
"Unlock" sections for player characters only.

### Playtest notes

Template `_templates/playtest-note.md` → `docs/playtests/YYYY-MM-DD-short-title.md`.
Required: `name`, `date`. Playtests have no `status`.

```yaml
---
name: Example session
date: 2026-01-31             # must match the filename prefix
players: [Player one, Player two]   # optional
build: abc1234               # optional: build or commit tested
---
```

### Decisions

Template `_templates/decision.md` → `docs/decisions/NNNN-short-title.md`
(next free number). Required: `id`, `name`, `date`, `status`.

```yaml
---
id: "0001"                   # in quotes, same as the filename prefix
name: Example decision
date: 2026-01-31
status: accepted             # proposed, accepted or superseded
decided_by: [Name one]       # optional
superseded_by: "0002"        # optional: id of the replacing decision
---
```

Keep the quotes around ids: without them YAML reads `0001` as the number 1
(and `0010` as 8). Superseded decisions stay in the log, struck through, with
a link to their replacement.

### Other pages

Rules, triggers, shops & breaks, meta progression, open questions, parking
lot and roadmap are ordinary Markdown pages: edit them directly. A new standalone page must be
added to `nav` in `mkdocs.yml`.

## 4. Frontmatter reference

Types: `str` (text), `list[str]` (e.g. `[a, b]`), `date` (`YYYY-MM-DD`),
`enum` (one of the listed values). Unknown fields produce a warning, which
catches typos.

### Shared fields (all collections)

| Field     | Type      | Required | Values / notes |
|-----------|-----------|----------|----------------|
| `name`    | str       | yes      | Display name |
| `status`  | enum      | yes      | `idea`, `approved`, `implemented`, `shelved`, `cut` (not used by playtests) |
| `author`  | str       | no       | Who wrote the entry |
| `tags`    | list[str] | no       | Free tags, listed on the Tags page |
| `summary` | str       | no       | One line shown in index tables |

### Menu items

| Field         | Type | Required | Values / notes |
|---------------|------|----------|----------------|
| `rarity`      | enum | yes      | `common`, `rare`, `legendary`, `cursed` |
| `type`        | enum | yes      | One of `extra.item_types` in `mkdocs.yml` |
| `cursed_with` | str  | no       | Slug of an existing menu item whose `rarity` is `cursed` |

### Consumables and relics

| Field    | Type | Required | Values / notes |
|----------|------|----------|----------------|
| `rarity` | enum | no       | `common`, `rare`, `legendary` |
| `shop`   | enum | no       | Consumables: `dish-pit`. Relics: `bar`. Defaults to that value. |

### Keywords

Shared fields only.

### Characters

| Field      | Type | Required | Values / notes |
|------------|------|----------|----------------|
| `category` | enum | yes      | `player`, `boss`, `minion`, `shopkeeper`, `npc` |
| `biome`    | str  | no       | Slug of an existing biome page |

### Biomes

| Field  | Type | Required | Values / notes |
|--------|------|----------|----------------|
| `name` | str  | yes      | Biome name, or `TBD` |
| `boss` | str  | yes      | Boss name, e.g. `The Shark` |

### Playtest notes

| Field     | Type      | Required | Values / notes |
|-----------|-----------|----------|----------------|
| `date`    | date      | yes      | Must match the filename prefix |
| `players` | list[str] | no       | |
| `build`   | str       | no       | Game build / commit tested |

### Decisions

| Field           | Type      | Required | Values / notes |
|-----------------|-----------|----------|----------------|
| `id`            | str       | yes      | 4 digits in quotes, matches the filename prefix, unique |
| `date`          | date      | yes      | |
| `decided_by`    | list[str] | no       | |
| `status`        | enum      | yes      | `proposed`, `accepted`, `superseded` (replaces the shared enum) |
| `superseded_by` | str       | no       | Id of an existing decision |

## 5. Adding a new item type

Item types are defined in **one place**, `extra.item_types` in `mkdocs.yml`:

```yaml
extra:
  item_types:
    - TBD
    - Example type
```

Add a line, then use exactly that text as `type:` in menu items. The Type
filter on the menu items page picks it up automatically. Removing a type makes
every item still using it produce a warning.

## 6. Status values

| Status        | Meaning |
|---------------|---------|
| `idea`        | Proposed, not decided. Open for discussion. |
| `approved`    | Decided: part of the design, not yet in the game. |
| `implemented` | In the Godot build. |
| `shelved`     | Set aside for now; may come back later. Shown dimmed. |
| `cut`         | Removed from the design. Kept for history; shown struck through. |

Decisions use their own statuses: `proposed` (under discussion), `accepted`
(in force), `superseded` (replaced by a later decision, see `superseded_by`).

Every entry is also tagged automatically `status:<value>` (plus
`rarity:<value>`, `type:<value>` and `category:<value>` where they apply), so the Tags page lists,
for example, every `status:approved` entry.

## 7. Validation

Every build checks every entry. Problems are printed as warnings naming the
file, the field and the problem, for example:

```
WARNING -  menu-items/example-item.md: rarity 'epic' is invalid (expected one of: common, rare, legendary, cursed)
WARNING -  menu-items/example-item.md: name is required but missing
WARNING -  menu-items/example-item.md: type 'Example' is invalid (expected one of: TBD) (allowed values are set by extra.item_types in mkdocs.yml)
WARNING -  menu-items/example-item.md: cursed_with 'other-item' points to a menu item whose rarity is 'rare' (it must be 'cursed')
WARNING -  decisions/0001-example.md: id must be in quotes to keep its leading zeros, e.g. id: "0001"
```

Also checked: filename conventions, valid dates, YAML syntax, unknown fields,
playtest date vs filename, duplicate decision ids, `superseded_by` targets,
and broken links or anchors between pages.

Locally, `mkdocs serve` keeps working and shows the warnings. In CI the site is
built with `mkdocs build --strict`, so **any warning fails the build and
nothing is deployed** until it is fixed. Run `mkdocs build --strict` before
pushing to be sure.

## 8. Deployment

`.github/workflows/deploy.yml` runs on every push to `main` (and manually from
the Actions tab): it installs the requirements, runs `mkdocs build --strict`
and publishes the `site/` folder to GitHub Pages.

The site is published at <https://zgaillard.github.io/punched-in-wiki/>, from
the public repository
[ZGaillard/punched-in-wiki](https://github.com/ZGaillard/punched-in-wiki).
Pages is set to **Settings → Pages → Build and deployment → Source: GitHub
Actions**. To publish a change, push to `main`; the Actions tab shows the
build and any warning that stopped it.

If the repository moves, update `site_url` and `repo_url` in `mkdocs.yml`.

Notes:

- GitHub Pages on a **private** repository requires a paid GitHub plan
  (Pro, Team or Enterprise).
- The published site is **publicly reachable** by anyone who has the URL, even
  when the repository is private.
- The "Recently added" list uses each file's last commit date (the workflow
  checks out the full history for this); files not committed yet use their
  modification time.
