# Core rules

The rules of a single game of Punched In: the board, the checkers, damage, and
how a game is won or lost. For the words used here (order, pillar, refire,
serve, plate…), see the [glossary](glossary.md).

## Board & checkers

- Each game is a game of **classic backgammon** (not Trictrac).
- The board is **the pass**. A checker on the board is an **order**; the 24
  points keep their usual name, **points**.
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
- Enemy orders deal damage to the player when they are served.
- The run is lost if the player's HP reaches zero.

!!! note "TBD"
    Exact damage values and the player's HP. See
    [open questions](../decisions/open-questions.md).

## Refire & the pillar

Hitting a lone enemy order **refires** it: it goes to the **pillar**
(backgammon's "bar") and must re-enter the board before its side can move
anything else, as in classic backgammon.

!!! note "TBD"
    Any rule about refired orders beyond classic backgammon.

## Serving

- Bearing off is **serving**. A served order becomes a **plate** on the pass
  shelf.
- The player wins a game by serving all of their own orders.
- Enemy orders deal damage to the player when they are served (see
  [Damage & HP](#damage-hp)).

## Win & loss conditions

| What happens                         | In a service             | Against a boss                  |
|--------------------------------------|--------------------------|---------------------------------|
| The player serves all their orders   | The player wins the game | The player wins the game        |
| The enemy serves all 15 orders       | The run continues (the player will have lost a lot of HP) | The player loses the run immediately |

!!! info "Current build"
    The Godot build has no HP and no enemies yet, so a lost game never ends
    the run there.
| The player's HP reaches zero           | The run is lost          | The run is lost                 |
