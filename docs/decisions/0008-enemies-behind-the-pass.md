---
id: "0008"
name: The enemies behind the pass
date: 2026-11-11
status: accepted
tags: [art, enemies, bosses]
summary: The enemy whose checker plays comes from behind the pass and stops on the right; the Sardines are one school; bosses have short lines.
---

## Context

The enemies had no presence on the board: only their bills said whose
checkers they were. The art for the Shark and the Sardines is drawn.

## Decision

- **Behind the pass.** During the enemy's turn, the owner of each checker
  about to move comes in from the right, behind the pass, and stops on the
  right. Minions come as their checkers play, so several can be there at
  once, each newcomer to the left of the others. Everyone leaves at the end of the enemy's turn.
- **The Sardines** come together as a school of four drawings, Sardine 1 to
  4 from left to right. Each Sardine you eat takes the rightmost drawing
  away. The Sardine has 5 checkers but only 4 drawings, so once 4 are eaten
  the Shark comes instead. He makes a snarky remark about it, and from then
  on he comes whenever a Sardine checker plays.
- **Bosses talk**, in a short speech bubble, at a few moments: coming in for
  the boss game, stepping in during regular game 2, sometimes after hitting
  you, and (the Shark) when the Sardines run out. Minions don't talk.
- **Slower play.** The enemy's moves and Riptide's drift play slowly
  enough to follow.
- A character whose art isn't drawn yet comes as a card with its name.

## Alternatives considered

- Every enemy on stage for the whole game: busier, and it doesn't show who
  is playing.
- One drawing per Sardine checker (5): there are 4 drawings.

## Consequences

- Each boss needs lines; the Shark's are placeholders for now. The game
  keeps them in `data/dialog.cfg`.
- The Pufferfish and Pelican need art, then every other biome's characters.
