# Shops & breaks

Everything that happens between games: the two shops where the player spends
**coins**, the staff meal, and the pause menu. For when each
one happens, see [Order of a run](rules/run-structure.md#order-of-a-run).

| Stop | Run by | What | When |
|------|--------|------|------|
| [Consumable shop](#consumable-shop) | [The Elephant](characters/the-elephant.md) | Consumables | After each regular game |
| [Relic shop](#relic-shop) | [The Octopus](characters/the-octopus.md) | Relics | Before the run, after each boss game |
| [Staff meal](#staff-meal) | [The Saint Bernard](characters/the-saint-bernard.md) | Heal to full HP | End of each day |
| [Pause](#pause) | — | Pause menu | Any time |

## Consumable shop

- Run by [The Elephant](characters/the-elephant.md).
- Consumables are single-use.
- Visited after each **regular game**, right after the menu item choice. Not after
  a boss game.
- Offers **3 different consumables**.
- **The inventory has no limit**: the player can hold any number of consumables,
  copies of the same one included. Each card on offer sells once.
- Browse every consumable in [Consumables](consumables/index.md).

| Rarity    | Price (coins) |
|-----------|--------------|
| Common    | 4            |
| Rare      | 6            |
| Legendary | 9            |

!!! note "TBD"
    How the offer is chosen (random among all consumables in the current
    build).

## Relic shop

- Run by [The Octopus](characters/the-octopus.md).
- Relics are game-changing items.
- Visited **before the run** (for a starting relic) and after each **boss game**
  (the end of a day). The staff meal follows.
- Offers **3 different relics**.
- Relics are kept for the rest of the run. No limit on how many, but one of
  each.
- Browse every relic in [Relics](relics/index.md).

| Rarity    | Price (coins) |
|-----------|--------------|
| Common    | 8            |
| Rare      | 12           |
| Legendary | 16           |

!!! note "TBD"
    How the offer is chosen (random among the relics not owned yet in the
    current build), and whether the starting relic is free.

## Staff meal

- Cooked by [The Saint Bernard](characters/the-saint-bernard.md): the meal
  the crew eats together before the next day.
- At the end of each day, after the relic shop.
- Heals the player to full HP, so every day and the final boss start at full
  HP.

## Pause

The pause menu, available **at any time**. From the pause the player
can:

- save;
- quit or abandon the run;
- view their current menu, relics and consumables.

## Coins

Coins are the in-run currency, spent in the consumable shop and the relic shop.

- The player starts a run with **10 coins**.
- Each checker the player bears off earns **1 coin**, win or lose, paid at the end
  of the game.

See [decision 0002](decisions/0002-tips-and-prices.md).

!!! note "TBD"
    The money system is not final: other sources of coins (bonuses for
    winning, items…), and whether the starting relic is free. See
    [open questions](decisions/open-questions.md#money-system).
