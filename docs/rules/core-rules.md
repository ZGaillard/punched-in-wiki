# Core rules

The rules of a single game of Punched In: the board, the checkers, damage, and
how a game is won or lost. For the words used here (order, plate, bill,
refired…), see the [glossary](glossary.md).

## Board & checkers

- Each game is a game of **classic backgammon** (not Trictrac).
- A checker on the board is an **order**; a point holding one or more checkers
  is a **bill**.
- The player's whole collection of checkers is their **menu**. A menu is always
  exactly **15 checkers**. See [Drafting & curses](drafting-and-curses.md).
- In a [service](run-structure.md), each minion controls 5 of the enemy's 15
  checkers.
- Some enemy checkers have special abilities.
- **Enemy placement:** every enemy (minion or boss) has its own placement rule
  for its checkers, which can be fixed or a constrained random distribution.
  Each enemy's rule is documented on its [biome page](../biomes/index.md).

!!! note "TBD"
    The special abilities of enemy checkers.

## Damage & HP

- The player has HP; enemies have none.
- Enemy checkers deal damage to the player when they are borne off.
- The run is lost if the player's HP reaches zero.

!!! note "TBD"
    Exact damage values and the player's HP. See
    [open questions](../decisions/open-questions.md).

## Refired

A checker that was hit and sent off the board is **refired** (backgammon's
"bar").

!!! note "TBD"
    Any rule about refired checkers beyond classic backgammon.

## Bearing off

- A checker that has been borne off is a **plate**.
- The player wins a game by bearing off all of their own checkers.
- Enemy checkers deal damage to the player when they are borne off (see
  [Damage & HP](#damage-hp)).

## Win & loss conditions

| What happens                           | In a service             | Against a boss                  |
|----------------------------------------|--------------------------|---------------------------------|
| The player bears off all their checkers | The player wins the game | The player wins the game        |
| The enemy bears off all 15 checkers    | The run continues (the player will have lost a lot of HP) | The player loses the run immediately |
| The player's HP reaches zero           | The run is lost          | The run is lost                 |
