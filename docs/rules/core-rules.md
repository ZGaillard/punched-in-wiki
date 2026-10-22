# Core rules

The rules of a single game of Punched In: the board, the orders, damage, and
how a game is won or lost. For the words used here (order, pillar, refire,
serve, plate…), see the [glossary](glossary.md). For how games chain into a
run, see [Run structure](run-structure.md).

## Board & orders

- Each game is a game of **classic backgammon** (not Trictrac).
- The board is **the pass**. A checker on the board is an **order**; the 24
  points keep their usual name, **points**.
- The player's whole collection of checkers is their **menu**: always exactly
  **15 orders**. See [Drafting & curses](drafting-and-curses.md).
- The enemy also always has **15 orders**.
- **Placement:** almost every game uses the standard backgammon starting
  setup. Exceptions are listed on each [biome page](../biomes/index.md) (e.g.
  The Shark's *Table stealer*).

## Enemies

- In a **service**, the enemy is the biome's three **minions**. Each one owns
  5 of the enemy's 15 orders. They share one AI and one roll, and play as a
  single player.
- In a **close**, the enemy is the biome's **boss**.
- Some enemy orders are **special orders**, with an ability of their own.
  They look different on the board, so the player can always tell which ones
  they are. Bosses can also have abilities not tied to orders.
- How many special orders an enemy has grows each day. See
  [How a biome works](../biomes/index.md#how-a-biome-works).

## Damage & HP

!!! info "Draft"
    The numbers in this section are `status: idea`.

- The player has HP; enemies have none.
- The player has **15 HP per day**. HP carries over between the games of a
  day and is restored to full by the
  [staff meal](../characters/the-saint-bernard.md) at the end of each day.
- Each enemy order that is served removes **1 HP**. Some special orders deal
  more (e.g. The Shark's
  [Feeding frenzy](../biomes/shark.md#special-orders) orders: 2 HP).
- The run is lost when the player's HP reaches 0.

## Refire & the pillar

Hitting a lone enemy order (a **blot**) **refires** it: it goes to the
**pillar** (backgammon's "bar") and must re-enter the board before its side
can move anything else, as in classic backgammon.

Some special orders change this: for example the Sloth biome's
[Deer](../biomes/sloth.md#minion-3-deer) can escape instead of going to the
pillar, and the Shark biome's
[Pelican](../biomes/shark.md#minion-3-pelican) freezes the orders it refires.

## Serving

- Bearing off is **serving**. A served order becomes a **plate** on the pass
  shelf.
- Each plate the player serves leaves 1 tip (see
  [Shops](../shops.md#tips)).
- Enemy orders deal damage to the player when they are served (see
  [Damage & HP](#damage-hp)).

## Win & loss

| What happens                       | Result |
|------------------------------------|--------|
| The player serves all their orders | The player wins the game, however many enemy orders are left. |
| The enemy serves all 15 orders     | The player has taken at least 15 damage that day: the run is lost. This applies to services and closes alike. |
| The player's HP reaches 0          | The run is lost. |

!!! info "Current build"
    The Godot build has no HP and no enemies yet, so a lost game never ends
    the run there.
