---
id: "0009"
name: One effect system for checkers, relics and biome rules
date: 2026-11-11
status: accepted
tags: [rules, relics, menu-items]
summary: Menu items, special checkers, relics and biome rules are one kind of effect, firing on the same triggers in a fixed order; relics act on your side for the whole run.
---

## Context

Special checkers and the Shark's biome rule already react to fixed moments of
the game (a hit, a move, the end of a turn). Menu items and relics will need
the same, and consumables work on their own. The [triggers](../rules/triggers.md)
list is still a draft, and no menu item has an effect yet.

## Decision

- **One kind of effect.** A menu item's effect, an enemy's special checker, a
  relic and a biome rule all react to the same [triggers](../rules/triggers.md).
- **Where an effect lives:**
    - on a **checker**: menu items and special checkers;
    - on the **game**: the biome rule;
    - on **your side, for the whole run**: relics (for example
      [Slow burn](../relics/slow-burn.md), +1 pip every turn). A relic is never
      carried by a checker.
- **Order.** When several effects fire at once: first the checker that moved,
  then the checker it hit, then side effects (relics), then the biome rule.
- **Built as needed.** The triggers are built when the first menu items need
  them, not from the whole list ahead of time.
- **Consumables stay as they are** for now. Their waiting effects (Chill pill,
  Edible, Decaf on the enemy, Poppers) join the system with the decision on
  stacking consumables.

## Alternatives considered

- Relics carried by a checker, like a menu item: they could be hit or stolen,
  which mixes them up with menu items.
- Your effects always before the enemy's, or the enemy's first.
- Building every simple trigger now: some might never be used.

## Consequences

- Menu items come first: the user designs the first ones, then their triggers
  are built.
- [Relic effects](../relics/index.md) wait for those triggers.
