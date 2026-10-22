# Shops & breaks

Everything that happens between games: the two shops where the player spends
**tips**, the staff meal, and the smoke break (the pause menu). For when each
one happens, see [Order of a run](rules/run-structure.md#order-of-a-run).

| Stop | Run by | What | When |
|------|--------|------|------|
| [Dish pit](#dish-pit) | [The Elephant](characters/the-elephant.md) | Consumables | After each service |
| [Bar](#bar) | [The Octopus](characters/the-octopus.md) | Relics | Before the run, after each close |
| [Staff meal](#staff-meal) | [The Saint Bernard](characters/the-saint-bernard.md) | Heal to full HP | End of each day |
| [Smoke break](#smoke-break) | — | Pause menu | Any time |

## Dish pit

- The **consumables** shop, run by [The Elephant](characters/the-elephant.md).
- Consumables are single-use.
- Visited after each **service**, right after the menu item choice. Not after
  a close.
- Offers **3 different consumables**.
- The player has **3 pockets**: at most 3 consumables held at once.
- Browse every consumable in [Consumables](consumables/index.md).

| Rarity    | Price (tips) |
|-----------|--------------|
| Common    | 4            |
| Rare      | 6            |
| Legendary | 9            |

!!! note "TBD"
    How the offer is chosen (random among all consumables in the current
    build).

## Bar

- The **relics** shop ("shift beer"), run by
  [The Octopus](characters/the-octopus.md).
- Relics are game-changing items.
- Visited **before the run** (for a starting relic) and after each **close**
  (the end of a day). The staff meal follows.
- Offers **3 different relics**.
- Relics are kept for the rest of the run. No limit on how many, but one of
  each.
- Browse every relic in [Relics](relics/index.md).

| Rarity    | Price (tips) |
|-----------|--------------|
| Common    | 8            |
| Rare      | 12           |
| Legendary | 16           |

!!! note "TBD"
    How the offer is chosen (random among the relics not owned yet in the
    current build), and whether the starting relic is free.

## Staff meal

- Cooked by [The Saint Bernard](characters/the-saint-bernard.md): the meal
  the crew eats together before service.
- At the end of each day, after the bar.
- Heals the player to full HP, so every day and the final boss start at full
  HP.

## Smoke break

The pause menu, available **at any time**. From the smoke break the player
can:

- save;
- quit or abandon the run;
- view their current menu, relics and consumables.

## Tips

Tips are the in-run currency, spent in the dish pit and the bar.

- The player starts a run with **10 tips**.
- Each plate the player serves leaves **1 tip**, win or lose, paid at the end
  of the game.

See [decision 0002](decisions/0002-tips-and-prices.md).

!!! note "TBD"
    The money system is not final: other sources of tips (bonuses for
    winning, items…), and whether the starting relic is free. See
    [open questions](decisions/open-questions.md#money-system).
