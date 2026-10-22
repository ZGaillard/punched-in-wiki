# Run structure

How a run is organised: the three days, the games played each day, and where
the shops happen between games.

## Days

- A **run** lasts 3 days: **Thursday**, **Friday** and **Saturday**.
- Each day, the player faces one [biome](../biomes/index.md): 2 **services**
  (games against the biome's minions), then the **close** (the game against the
  biome's boss).
- There are 5 biomes; a run uses 3 of them.
- After the third day, the player faces the [final boss](../final-boss.md),
  The Pig, the owner.

!!! note "TBD"
    How the 3 biomes of a run are chosen among the 5.

## Game numbering

A run has 10 games in total.

| Game       | Day      | Game type | Opponent                    |
|------------|----------|-----------|-----------------------------|
| 1.1        | Thursday | Service   | The day's biome minions     |
| 1.2        | Thursday | Service   | The day's biome minions     |
| 1.B        | Thursday | Close     | The day's biome boss        |
| 2.1        | Friday   | Service   | The day's biome minions     |
| 2.2        | Friday   | Service   | The day's biome minions     |
| 2.B        | Friday   | Close     | The day's biome boss        |
| 3.1        | Saturday | Service   | The day's biome minions     |
| 3.2        | Saturday | Service   | The day's biome minions     |
| 3.B        | Saturday | Close     | The day's biome boss        |
| Final boss | —        | Final boss | [The Pig](../final-boss.md) |

## Between games

- **Drafting:** between games, the player is offered 3 menu items and may add
  one. See [Drafting & curses](drafting-and-curses.md).
- **Dish pit:** the consumables shop, visited after **every** game.
- **Bar:** the relics shop ("shift beer"), visited after each **close**, right
  after the dish pit.
- **Smoke break:** the pause menu, available at any time.

So after a service the player goes to the dish pit, then the next game; after
a close, to the dish pit, then the bar, then the next day. See
[Shops](../shops.md) for details and
[decision 0003](../decisions/0003-shop-order.md).

!!! note "TBD"
    Where drafting fits in that sequence.
