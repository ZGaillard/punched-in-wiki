# Enemy AI

How the enemy plays its checkers. One AI plays every enemy. What makes a
biome's enemies play differently is their **style**, and what makes them use
their special checkers well is each checker's **hint**.

!!! info "Current build"
    Built in Godot for the Shark biome: the base AI, the Shark's minion and boss
    styles, and the hints of his minions' checkers. Every enemy looks one turn
    ahead; the bosses' sharper search comes next. The numbers are untuned.
    Code: the Godot project's `docs/reference/ai.md`.

## Goals

- **Difficulty comes from the enemies' special checkers, not from a strong
  AI.** The AI only has to *feel* clever. A first run must not be beatable.
- **Weak through character, never through noise.** The AI never plays a
  visible blunder: it only chooses among turns close to its best. It is weak
  because each enemy overvalues its own thing (the Shark's servers hit
  everything), which is readable and can be learned.
- **One style per biome.** The bosses play their biome's style, milder and
  sharper.
- **One AI plays the three minions** of a regular game as a single player,
  aware of every special checker on the board.
- **Fair:** it sees the board, never your next roll (only the Fox will) and
  not your items.

## How it plays

1. It lists every distinct turn its dice allow, by the game's own rules, so
   every special checker's effect is in.
2. It scores the position each turn leaves, in pips: pip count, blots and how
   likely they are to be hit, made points, home-board points, anchors, primes,
   your checkers on the bar, stacking.
   **The score is its side, judged with its style, minus your side, judged
   plainly.** A careless Shark minds its own blots less, but your blots still
   look just as tasty to it.
3. It keeps the turns within a few pips of its best (the **blunder cap**) and
   picks one of them, the better ones more often.
4. Bearing off in a race, it bears off as many checkers as it can.

On the board it pauses to think, then plays its moves one by one. The game can
be played human vs human, you vs the AI (always in a normal run), or AI vs AI
(to watch and balance).

## Styles

A style says how much more or less than plain backgammon the enemy values each
part of its own position, and how loosely it picks.

| Style | Plays | Values more | Values less |
|---|---|---|---|
| Base | biomes without a style yet, the final | — | — |
| Shark minions | the Shark's regular games | hitting (×1.8), keeping hit checkers out | its own blots (×0.5), racing |
| The Shark | his boss game | the same, milder (hitting ×1.5, blots ×0.7) | |

The [Sloth](biomes/sloth.md)'s style will be a builder of walls (Primer,
Cautious).

## Hints

Each special checker tells the AI what its effect is worth, so the AI plays it
well in any biome it appears in.

| Effect | Hint |
|---|---|
| Puffed up (Pufferfish) | a still Pufferfish is bait: keep it still; its blot is less at risk |
| School speed (Sardine) | Sardines sharing a point are worth more |
| Eaten alone (Sardine) | a Sardine you hit is a loss, and a Sardine blot risks the whole checker |
| Numbness (Pelican) | your checker in its pouch is worth extra |
| Riptide (biome rule) | none: it acts after your turn, and the AI sees where your blots drifted |

An effect without a hint is still obeyed. The AI just doesn't plan for it.

## Later

- The bosses look two turns ahead.
- The damage goal once HP exists: bear off the checkers that hurt most first.
- The Fox reads your next roll (her ability, not a cheat of the AI).
- Hints for your own menu items and relics, so the AI won't hit a checker of
  yours that punishes being hit.
