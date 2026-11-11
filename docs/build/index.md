# Build

What the Godot build can do today, and how it is made. The design lives in
the rest of this wiki; the code and its own docs live in the game repository,
[`ZGaillard/punched-in-v-0`](https://github.com/ZGaillard/punched-in-v-0)
(private). Its
[`docs/status.md`](https://github.com/ZGaillard/punched-in-v-0/blob/main/docs/status.md)
is the detailed, up-to-date list.

## What is built

- **Backgammon** without the doubling cube, on the hand-drawn board, against
  the [AI](../ai.md) (or both sides by hand, or AI against AI, from the debug
  menu). Checkers are drawn as bills
  with their owner and a dish; hover a stack to spread it, rest on a bill to
  read it.
- **The run**: three days of two regular games and a boss game, then the final;
  coins for every checker you bear off; the consumable shop after every game
  and the relic shop after a boss game. You have HP: each enemy checker borne
  off costs some, and the run is lost at 0.
- **Enemies**: each checker belongs to the day's minions or boss. The Shark's
  minions ([Sardine](../characters/sardine.md),
  [Pufferfish](../characters/pufferfish.md),
  [Pelican](../characters/pelican.md)) have their special checkers, and the
  biome rule Riptide applies. [The Shark](../characters/the-shark.md) has Blood
  in the water and Feeding frenzy (Shark bite and Table stealer wait for the
  menu), and steps into the second regular game. The enemies come out from
  behind the pass as their checkers move. The other biomes have names only.
- **Items**: the [19 implemented consumables](../consumables/index.md) work.
  Relics are placeholders with no effect.
- **Your menu**: the first 8 [menu items](../menu-items/index.md) work. There
  is no drafting yet: the debug menu's Menu tab sets which ones your 15
  checkers start with, and Burgers fill the rest.
- **Tools**: a debug menu to start any game, position or loadout, and an F1
  panel to set up positions, dice and special checkers in a game.

Pages marked `implemented` in this wiki are in the build; the
[Roadmap](../roadmap.md) says what comes next.

## Pages

- [Running the game](running.md): opening the project, the debug menu, F1,
  the checks.
- [Architecture](architecture.md): how the code is organised.
- [Working with agents](working-with-agents.md): how goals become task files,
  and which repository owns which fact.
