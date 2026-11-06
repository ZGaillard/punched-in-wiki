# Core rules

The rules of a single game of Punched In: the board, the checkers, damage, and
how a game is won or lost. For the words used here (checker, bar, hit,
bear off, plate…), see the [glossary](glossary.md). For how games chain into a
run, see [Run structure](run-structure.md).

## Board & checkers

- Each game is a game of **classic backgammon** (not Trictrac).
- The board is **the board**. A checker on the board is an **checker**; the 24
  points keep their usual name, **points**.
- The player's whole collection of checkers is their **menu**: always exactly
  **15 checkers**. See [Drafting & curses](drafting-and-curses.md).
- The enemy also always has **15 checkers**.
- **Direction:** the player sits at the bottom of the board and moves
  clockwise, with their home board at the bottom left; the enemy plays the
  mirror image. The player's checkers have a fixed colour, and enemy checkers
  are tinted by biome. See [decision 0005](../decisions/0005-board-orientation.md).
- **Placement:** almost every game uses the standard backgammon starting
  setup. Exceptions are listed on each [biome page](../biomes/index.md) (e.g.
  The Shark's *Table stealer*).

## Enemies

- In a **regular game**, the enemy is the biome's three **minions**. Each one owns
  5 of the enemy's 15 checkers. They share one AI and one roll, and play as a
  single player.
- In a **boss game**, the enemy is the biome's **boss**.
- Some enemy checkers are **special checkers**, with an ability of their own.
  They look different on the board, so the player can always tell which ones
  they are. Bosses can also have abilities not tied to checkers.
- How many special checkers an enemy has grows each day. See
  [How a biome works](../biomes/index.md#how-a-biome-works).

## Damage & HP

!!! info "Draft"
    The numbers in this section are `status: idea`.

- The player has HP; enemies have none.
- The player has **15 HP per day**. HP carries over between the games of a
  day and is restored to full by the
  [staff meal](../characters/the-saint-bernard.md) at the end of each day.
- Each enemy checker that is borne off removes **1 HP**. Some special checkers deal
  more (e.g. The Shark's
  [Feeding frenzy](../biomes/shark.md#special-checkers) checkers: 2 HP).
- The run is lost when the player's HP reaches 0.

## Hit & the bar

Hitting a lone enemy checker (a **blot**) **hits** it: it goes to the
**bar** (backgammon's "bar") and must re-enter the board before its side
can move anything else, as in classic backgammon.

Some special checkers change this: for example the Sloth biome's
[Deer](../biomes/sloth.md#minion-3-deer) can escape instead of going to the
bar, and the Shark biome's
[Pelican](../biomes/shark.md#minion-3-pelican) freezes the checkers it hits.

## Bearing off

- A borne-off checker is drawn as a **plate** on the board's shelf.
- Each checker the player bears off earns 1 coin (see
  [Shops](../shops.md#coins)).
- Enemy checkers deal damage to the player when they are borne off (see
  [Damage & HP](#damage-hp)).

## Win & loss

| What happens                       | Result |
|------------------------------------|--------|
| The player bears off all their checkers | The player wins the game, however many enemy checkers are left. |
| The enemy bears off all 15 checkers     | The player has taken at least 15 damage that day: the run is lost. This applies to regular games and boss games alike. |
| The player's HP reaches 0          | The run is lost. |

!!! info "Current build"
    The Godot build has no HP and no enemies yet, so a lost game never ends
    the run there.
