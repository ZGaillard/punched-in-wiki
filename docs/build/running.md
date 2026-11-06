# Running the game

## Open and play

1. Install **Godot 4.7** (standard build, GDScript).
2. Clone [`ZGaillard/punched-in-v-0`](https://github.com/ZGaillard/punched-in-v-0)
   and open its `project.godot`, or run `godot --path .` in it.
3. Press **F5**. The game opens on the **debug menu**: **Normal run** plays a
   plain run from Thursday's first game.

## The debug menu

The main menu is a testing tool for now, with four tabs:

- **Start**: any biome, day (or the final) and game of the day; come back to
  the menu after one game, or go on with the run.
- **AI & scenarios**: start from a saved position or a pasted position code.
  The AI's controls wait there, disabled.
- **Items**: open a shop at once, start with items and coins, force items into
  the offers, and tune prices and weights.
- **Settings**: game speed, window, open the F1 panel at start.

A fixed **seed** in the header replays the biomes, the rolls and the offers.

## In a game

- Click a checker (any bill of a stack picks its top one), then a ghost to
  move. **End turn** is the bell; **Esc** opens the pause menu.
- **F1** (debug builds) opens the dev panel: paste or copy a position code,
  set or queue dice, play random moves to any point, open a shop, add coins,
  and the **BILLS** tool to turn any checker into a minion's special checker.

## Checks

`tools/check.sh` in the game repository runs the automated tests (rules,
special checkers, consumables, the run, the screens) and checks that the
code's docs only name files and functions that exist. Run it before you
commit; it takes about 15 seconds.
