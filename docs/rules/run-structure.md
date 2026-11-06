# Run structure

How a run is organised: the three days, the games played each day, and what
happens between games. For the rules of a single game, see
[Core rules](core-rules.md).

## At a glance

- A **run** lasts 3 days: **Thursday**, **Friday** and **Saturday**, then the
  final boss.
- Each day, the player faces one [biome](../biomes/index.md): 2 **regular games**
  (games against the biome's minions), then the **boss game** (the game against
  the biome's boss).
- There are 5 biomes; a run uses 3 of them.
- After the third day, the player faces the [final boss](../final-boss.md),
  [The Pig](../characters/the-pig.md), the owner.
- A run has **10 games** in total.

!!! note "TBD"
    How the 3 biomes of a run are chosen among the 5.

## One day

```mermaid
flowchart LR
  S1[Game 1] --> M1[Menu item choice] --> P1[Consumable shop]
  P1 --> S2[Game 2] --> M2[Menu item choice] --> P2[Consumable shop]
  P2 --> C[Boss game] --> B[Relic shop] --> F[Staff meal]
```

## Order of a run

See [decision 0004](../decisions/0004-run-order.md).

0. **Before the run:** menu item choice, then the [bar](../shops.md#relic-shop) for
   a starting relic.
1. **First biome** (Thursday)
    1. **Regular game 1**, then menu item choice, then the
       [consumable shop](../shops.md#consumable-shop).
    2. **Regular game 2**, then menu item choice, then the consumable shop.
    3. **The boss game**, then the relic shop.
    4. **Staff meal:** heal to full HP.
2. **Second biome** (Friday): same as the first.
3. **Third biome** (Saturday): same as the first.
4. **Final boss:** [The Pig](../final-boss.md). The run ends after it: no shop.

!!! note "TBD"
    Whether the starting relic is free or bought with the starting 10 coins
    (the cheapest relic costs 8). See
    [open questions](../decisions/open-questions.md#money-system).

## Game numbering

| Game       | Day      | Game type  | Opponent                    |
|------------|----------|------------|-----------------------------|
| 1.1        | Thursday | Regular game    | The day's biome minions     |
| 1.2        | Thursday | Regular game    | The day's biome minions (+ a few boss checkers) |
| 1.B        | Thursday | Boss game  | The day's biome boss        |
| 2.1        | Friday   | Regular game    | The day's biome minions     |
| 2.2        | Friday   | Regular game    | The day's biome minions (+ a few boss checkers) |
| 2.B        | Friday   | Boss game  | The day's biome boss        |
| 3.1        | Saturday | Regular game    | The day's biome minions     |
| 3.2        | Saturday | Regular game    | The day's biome minions (+ a few boss checkers) |
| 3.B        | Saturday | Boss game  | The day's biome boss        |
| Final boss | —        | Final boss | [The Pig](../final-boss.md) |

Enemies get stronger each day: see
[How a biome works](../biomes/index.md#how-a-biome-works).

## Between games

| Stop | What happens | When | Run by |
|------|--------------|------|--------|
| **Menu item choice** | Pick 1 of 3 menu items, swapped into the menu. See [Drafting & curses](drafting-and-curses.md). | Before the run, after each regular game | — |
| **[Consumable shop](../shops.md#consumable-shop)** | Buy consumables with coins. | After each regular game | [The Elephant](../characters/the-elephant.md) |
| **[Relic shop](../shops.md#relic-shop)** | Buy a relic with coins. | Before the run, after each boss game | [The Octopus](../characters/the-octopus.md) |
| **[Staff meal](../shops.md#staff-meal)** | Heal to full HP. | End of each day, after the relic shop | [The Saint Bernard](../characters/the-saint-bernard.md) |
| **[Pause](../shops.md#pause)** | The pause menu. | Any time | — |

There is no menu item choice and no consumable shop after a boss game.
