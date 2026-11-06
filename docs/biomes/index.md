# Biomes

There are 5 biomes, each tied to its boss: The Shark, The Fox, The Old
Raccoon, The Sloth and The Snake. Each day of a run, the player faces one
biome: 2 regular games against the boss's 3 minions, then the boss game against the
boss. A run uses 3 of the 5 biomes. Biome names are not decided yet, so each
biome is named after its boss for now.

After the third day comes the [final boss](../final-boss.md),
[The Pig](../characters/the-pig.md).

## At a glance

Each biome's animals are one kind of restaurant staff.

| Biome | Animals | Restaurant role | Biome rule | Keyword |
|-------|---------|-----------------|------------|---------|
| [The Shark](shark.md) | Marine animals | Servers | [Riptide](shark.md#biome-rule-riptide) | [Hit boost](../keywords/hit-boost.md) |
| [The Fox](fox.md) | TBD | Waitresses | TBD | [Swap](../keywords/swap.md) |
| [The Old Raccoon](old-raccoon.md) | City animals | Cooks | TBD | TBD |
| [The Sloth](sloth.md) | Forest animals | Busboys | [Overgrowth](sloth.md#biome-rule-overgrowth) | [Mistakes](../keywords/mistakes.md) |
| [The Snake](snake.md) | Reptiles | The drinks bar | TBD | [Debuff](../keywords/debuff.md) |

<!-- collection: biomes -->

## How a biome works

!!! info "Draft"
    This section is `status: idea`.

- **Biome rule:** each biome has a rule that applies in every one of its
  games (e.g. *Riptide* for The Shark, *Overgrowth* for The Sloth).
- **Regular games:** all three minions play; each one owns 5 of the enemy's 15
  checkers. They share one AI and one roll, playing as a single player. Each
  minion only provides its special checkers and their effects.
- **Special checkers:** each minion has one special checker type of its own, so
  each biome has 3 minion special checker types (15 across the 5 biomes).
  Special checkers look different on the board, so the player can always tell
  which ones they are.
- **Scaling by day:** minions get stronger each day. Usually a minion has
  **2 special checkers on day 1, 3 on day 2, 4 on day 3** (its other checkers are
  normal); a biome page can make exceptions.
- **Boss in the second regular game:** in every biome, the boss sneaks **1 / 2 / 3**
  (by day) of his own special checkers into the second regular game. They always
  replace non-special minion checkers, never special ones.
- **The boss game:** the boss also gets harder each day. His special checkers can
  be a mix of types; on the last day, all 15 of his checkers are special.
  Bosses can also have abilities not tied to checkers.
- **Placement:** almost every game uses the standard backgammon starting
  setup.

## Biome page layout

Every biome page follows the same layout, so they are easy to compare:

1. **Overview:** animals, restaurant role, keyword, biome rule.
2. **Boss:** description, special checkers (with a table by day), placement,
   behaviour.
3. **Minion 1, 2, 3:** the same sections for each minion.
4. **Game notes:** special checkers per game, then notes on regular game 1,
   regular game 2 and the boss game.
5. **Design notes:** ideas on ice, rejected ideas.

Each boss and minion also has a short [character page](../characters/index.md)
that links back here.
