/*
 * Filters for the generated collection tables (menu items, consumables,
 * relics). The hook marks each table container with `data-pi-filters`, a JSON
 * list of filter groups: [{key, label, options: [[value, label], ...]}].
 * Each row carries `data-name`, `data-summary` and one `data-<key>` per group.
 *
 * Filters combine with AND across groups and OR within a group. State is kept
 * in the query string (?q=...&rarity=rare,legendary&status=approved) so a
 * filtered view can be shared by link.
 */
(function () {
  "use strict";

  function create(tag, className, text) {
    var node = document.createElement(tag);
    if (className) node.className = className;
    if (text) node.textContent = text;
    return node;
  }

  function readState(groups) {
    var params = new URLSearchParams(window.location.search);
    var state = { q: params.get("q") || "", groups: {} };
    groups.forEach(function (group) {
      var raw = params.get(group.key);
      state.groups[group.key] = new Set(raw ? raw.split(",").filter(Boolean) : []);
    });
    return state;
  }

  function writeState(state, groups) {
    var url = new URL(window.location.href);
    if (state.q) url.searchParams.set("q", state.q);
    else url.searchParams.delete("q");
    groups.forEach(function (group) {
      var values = Array.from(state.groups[group.key]);
      if (values.length) url.searchParams.set(group.key, values.join(","));
      else url.searchParams.delete(group.key);
    });
    // Keep commas readable in shared links.
    var search = url.searchParams.toString().replace(/%2C/g, ",");
    url.search = search ? "?" + search : "";
    window.history.replaceState(window.history.state, "", url.toString());
  }

  function setup(container) {
    if (container.dataset.piReady) return;
    container.dataset.piReady = "true";

    var groups = JSON.parse(container.dataset.piFilters);
    var noun = container.dataset.piNoun || "entries";
    var rows = Array.prototype.slice.call(container.querySelectorAll("tbody tr"));
    var state = readState(groups);

    var panel = create("div", "pi-filters");

    var search = create("input", "pi-filters__search");
    search.type = "search";
    search.placeholder = "Search name or summary…";
    search.setAttribute("aria-label", "Search by name or summary");
    search.value = state.q;
    search.addEventListener("input", function () {
      state.q = search.value.trim();
      update();
    });
    panel.appendChild(search);

    var checkboxes = [];
    groups.forEach(function (group) {
      var fieldset = create("fieldset", "pi-filters__group");
      fieldset.appendChild(create("legend", "pi-filters__legend", group.label));
      group.options.forEach(function (option) {
        var value = option[0];
        var total = rows.filter(function (row) {
          return row.dataset[group.key] === value;
        }).length;
        var chip = create("label", "pi-chip");
        var box = create("input");
        box.type = "checkbox";
        box.value = value;
        box.checked = state.groups[group.key].has(value);
        box.addEventListener("change", function () {
          if (box.checked) state.groups[group.key].add(value);
          else state.groups[group.key].delete(value);
          update();
        });
        checkboxes.push(box);
        chip.appendChild(box);
        chip.appendChild(create("span", "pi-chip__label", option[1]));
        chip.appendChild(create("span", "pi-chip__count", String(total)));
        fieldset.appendChild(chip);
      });
      panel.appendChild(fieldset);
    });

    var footer = create("div", "pi-filters__footer");
    var count = create("span", "pi-filters__count");
    count.setAttribute("aria-live", "polite");
    var reset = create("button", "md-button pi-filters__reset", "Reset");
    reset.type = "button";
    reset.addEventListener("click", function () {
      state.q = "";
      search.value = "";
      groups.forEach(function (group) {
        state.groups[group.key].clear();
      });
      checkboxes.forEach(function (box) {
        box.checked = false;
      });
      update();
    });
    footer.appendChild(count);
    footer.appendChild(reset);
    panel.appendChild(footer);

    var empty = create("p", "pi-filters__empty", "No entries match these filters.");
    container.insertBefore(panel, container.firstChild);
    container.appendChild(empty);

    function matches(row) {
      if (state.q) {
        var text = ((row.dataset.name || "") + " " + (row.dataset.summary || "")).toLowerCase();
        if (text.indexOf(state.q.toLowerCase()) === -1) return false;
      }
      return groups.every(function (group) {
        var selected = state.groups[group.key];
        return selected.size === 0 || selected.has(row.dataset[group.key]);
      });
    }

    function update() {
      var shown = 0;
      rows.forEach(function (row) {
        var visible = matches(row);
        row.hidden = !visible;
        if (visible) shown += 1;
      });
      count.textContent = shown + " of " + rows.length + " " + noun;
      empty.hidden = shown !== 0;
      writeState(state, groups);
    }

    update();
  }

  function init() {
    document.querySelectorAll("[data-pi-filters]").forEach(setup);
  }

  // With `navigation.instant`, Material swaps the page content without a full
  // reload and emits on `document$` every time; fall back to a normal load.
  if (typeof window.document$ !== "undefined") {
    window.document$.subscribe(init);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
