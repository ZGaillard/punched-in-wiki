# Biomes

There are 5 biomes, each tied to its boss: The Shark, The Fox, The Old
Raccoon, The Sloth and The Snake. Each day of a run, the player faces one
biome: 2 services against the boss's 3 minions, then the close against the
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
| [The Snake](snake.md) | Reptiles | The bar | TBD | [Debuff](../keywords/debuff.md) |

<!-- collection: biomes -->

## How a biome works

!!! info "Draft"
    This section is `status: idea`.

- **Biome rule:** each biome has a rule that applies in every one of its
  games (e.g. *Riptide* for The Shark, *Overgrowth* for The Sloth).
- **Services:** all three minions play; each one owns 5 of the enemy's 15
  orders. They share one AI and one roll, playing as a single player. Each
  minion only provides its special orders and their effects.
- **Special orders:** each minion has one special order type of its own, so
  each biome has 3 minion special order types (15 across the 5 biomes).
  Special orders look different on the board, so the player can always tell
  which ones they are.
- **Scaling by day:** minions get stronger each day. Usually a minion has
  **2 special orders on day 1, 3 on day 2, 4 on day 3** (its other orders are
  normal); a biome page can make exceptions.
- **Boss in the second service:** in every biome, the boss sneaks **1 / 2 / 3**
  (by day) of his own special orders into the second service. They always
  replace non-special minion orders, never special ones.
- **The close:** the boss also gets harder each day. His special orders can
  be a mix of types; on the last day, all 15 of his orders are special.
  Bosses can also have abilities not tied to orders.
- **Placement:** almost every game uses the standard backgammon starting
  setup.

## Biome page layout

Every biome page follows the same layout, so they are easy to compare:

1. **Overview:** animals, restaurant role, keyword, biome rule.
2. **Boss:** description, special orders (with a table by day), placement,
   behaviour.
3. **Minion 1, 2, 3:** the same sections for each minion.
4. **Game notes:** special orders per game, then notes on service 1,
   service 2 and the close.
5. **Design notes:** ideas on ice, rejected ideas.

Each boss and minion also has a short [character page](../characters/index.md)
that links back here.
