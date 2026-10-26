# Open questions

Design questions that still need an answer, grouped by area. When one is
answered, record it as a [decision](index.md) and remove it from this list.

## Rules

### Exact damage values and HP { #damage-and-hp }

A draft exists (15 HP per day, 1 HP per served enemy order, restored by the
staff meal). It still needs playtesting. See
[Core rules](../rules/core-rules.md#damage-hp).

### Drafting and cursed items

- Can the player skip a menu item choice?
- Can a cursed item replace another cursed item?
- How are cursed items removed?

See [Drafting & curses](../rules/drafting-and-curses.md).

## Run & economy

### Money system

The tips economy ([decision 0002](0002-tips-and-prices.md)) is not final.
Among other things: is the starting relic, bought at the bar before the run,
free or paid with the starting 10 tips?

See [Shops & breaks](../shops.md#tips) and
[Order of a run](../rules/run-structure.md#order-of-a-run).

### Choosing the biomes of a run

How are the 3 biomes of a run chosen among the 5? See
[Run structure](../rules/run-structure.md).

## Biomes

### Biome names

Every biome is still named after its boss. See
[Biomes](../biomes/index.md).

### Boss special orders on days 1 and 2

How many special orders a boss has on days 1 and 2 is set per biome for now
(see [The Shark](../biomes/shark.md) and [The Sloth](../biomes/sloth.md)); no
general rule yet.

### The Snake

- Which debuffs does he serve? Do his minions debuff too?
- His biome is "the bar", but the **bar** is also the relics shop.

See [The Snake](../biomes/snake.md).

### The Old Raccoon

Playstyle: *the rush* or *the veteran*? See
[The Old Raccoon](../biomes/old-raccoon.md).

### The Fox

- Does she take ownership of your orders, or swap positions on the board?
- Whose effect does a swapped order carry, given the 15-order menu?

See [The Fox](../biomes/fox.md).

### More biomes

Insects and birds: which roles, which bosses? See the
[parking lot](../parking-lot.md#more-biomes).

## Content

### Item types

The allowed item types are listed in `extra.item_types` in `mkdocs.yml`,
currently only `TBD`.

### How are menu items upgraded?

See [Menu items](../menu-items/index.md).

### Consumables

- Eye drops needs a real name.
- Should dice be capped at 0? Below 0, orders move backward, which can
  sometimes help the enemy. Either way, the AI move generator must support
  backward moves (Vape, Cuban cigar).

See [Consumables](../consumables/index.md).

## Meta

### What is the meta currency?

See [Meta progression](../meta-progression.md).

## Stacking copies of a consumable

With no pocket limit, the same consumable can be used twice in one turn. Today:
two Chill pills both hit the enemy's next roll (the second does nothing more);
a second Foraged mushrooms or Poppers in the same turn adds nothing. Should
copies stack, chain onto later rolls, or be refused once one is waiting? See
[decision 0006](0006-no-pocket-limit.md).
