---
name: TBD
boss: The Shark
status: approved
summary: Marine animals, the servers. Aggressive; they punish your blots.
---

The biome tied to **The Shark**. This page collects everything about the biome: its identity, its boss, its three minions and notes on each of its games. The biome's name is not decided yet, so the page is titled after its boss.

!!! info "Draft"
    Everything below the overview is `status: idea`.

## Overview

- **Animals:** marine animals.
- **Role:** the servers. Aggressive; they punish your blots.
- **Keyword:** [hit boost](../keywords/hit-boost.md), the enemy gets a boost from hitting your checkers.
- **Dishes:** plain checkers are burgers. Each special checker has its own
  dish: Sardine *Sardines on toast*, Pufferfish *Fugu*, Pelican *Catch of the
  day*, the Shark's Feeding frenzy *Surf and turf* and Shark bite *Shark sushi*.

### Biome rule: Riptide

Applies in every game of the biome.

- At the end of each of **your** turns (not the enemy's), your blots drift
  backward by random pips: **1 on day 1, 2 on day 2, 3 on day 3**, spread over
  the same or different blots. The pips are handed out one at a time, each to
  a random blot; a pip given to a blot that can't drift is lost.
- Only your blots are affected, never the enemy's.
- A drifting blot is stopped by any point the enemy occupies (1 or more
  checkers): it stops just before it. It never hits.
- A blot stops at the edge of the board: it never drifts past your starting
  point.

## Boss: *The Shark*

Character page: [The Shark](../characters/the-shark.md).

### Description

The classic aggressive server who steals tables.

### Special checkers

- **Blood in the water** (ability): every time he hits one of your checkers,
  he gets a free extra 1-pip move.
- **Feeding frenzy checkers:** cost you **2 HP** when borne off instead of 1.
- **Shark bite checkers** (separate from Feeding frenzy): when one hits your
  checker, that checker loses its menu effect for the rest of the game.
- **Table stealer** (ability, boss game only, not when he shows up in the second
  regular game): on the first turn, he takes your rarest checker and places it on the
  furthest point from his home board. It plays for him, keeping its menu
  effect.

| Day | Feeding frenzy | Shark bite | Total special |
|-----|----------------|------------|---------------|
| 1   | 2              | 2          | 4             |
| 2   | 4              | 4          | 8             |
| 3   | 8              | 7          | 15 (all)      |

### Placement rule

Standard backgammon starting setup, except for *Table stealer*, which moves
your rarest checker on the first turn.

### Behaviour / AI notes

Aggressive: fits the **Blitzer** personality. His style is his minions',
milder and sharper: hitting ×1.5, his own blots ×0.7 (see
[Enemy AI](../ai.md#styles)). Like his minions, he looks one turn ahead (only the Fox looks ahead).

## Minion 1: Sardine

Character page: [Sardine](../characters/sardine.md).

### Description

Strong in a group, weak alone.

### Special checkers

Special checkers: **2 / 3 / 4** by day.

- **School speed** (special checkers only): when it moves from a point shared
  with another Sardine checker (special or not), it moves 1 extra pip. The
  extra pip is forced.
- **Eaten alone** (all 5 Sardine checkers): every Sardine you hit is removed
  from the game for good (a hit checker is always alone on its point). The
  enemy then has one checker fewer to bear off.

### Placement rule

Standard backgammon starting setup.

### Behaviour / AI notes

Shares the minions' single AI (see [Game notes](#game-notes)).

## Minion 2: Pufferfish

Character page: [Pufferfish](../characters/pufferfish.md).

### Description

Buff only.

### Special checkers

Special checkers: **1 / 2 / 3** by day.

- **Deflated:** if it moved during the enemy's last turn, it can be hit like
  any blot.
- **Puffed up:** if it didn't move during the enemy's last turn, hitting it
  sends your hitting checker to the bar too. It's a trade: the Pufferfish
  is hit as usual, and both go to the bar.

### Placement rule

Standard backgammon starting setup.

### Behaviour / AI notes

Shares the minions' single AI (see [Game notes](#game-notes)).

## Minion 3: Pelican

Character page: [Pelican](../characters/pelican.md).

### Description

!!! note "TBD"
    Who this minion is and how it plays.

### Special checkers

Special checkers: **2 / 3 / 4** by day.

- **Numbness:** when a special Pelican hits one of your checkers, that checker
  is caught in its pouch and frozen for 1 turn before going to the bar.
  While it is in the pouch, it is not on the bar: you play your other
  checkers freely. On your next turn it lands on the bar and must re-enter
  first, as usual.

### Placement rule

Standard backgammon starting setup.

### Behaviour / AI notes

Shares the minions' single AI (see [Game notes](#game-notes)).

## Game notes

The three minions share one AI and play as a single player: one enemy turn,
one roll. Their style, **Shark minions**, values hitting your checkers ×1.8
and minds its own blots only half as much: they hunt your blots and leave
their own. Each minion's special checkers bring their hints (a still
Pufferfish is bait, Sardines stick together, a Pelican hit is worth more). See
[Enemy AI](../ai.md). Each minion owns 5 of the enemy's 15 checkers and only provides its
special checkers and their effects.

| Day | Sardine | Pufferfish | Pelican | Regular game 1 | Regular game 2 (+ Shark) | Boss game |
|-----|---------|------------|---------|-----------|---------------------|-------|
| 1   | 2       | 1          | 2       | 5         | 6                   | 4     |
| 2   | 3       | 2          | 3       | 8         | 10                  | 8     |
| 3   | 4       | 3          | 4       | 11        | 14                  | 15    |

### Regular game 1

The three minions only; no Shark checkers.

### Regular game 2

The Shark shows up early: he replaces **1 / 2 / 3** (by day) of his minions'
non-special checkers with his own, **Shark bite only** (Feeding frenzy is saved
for the boss game). Minions keep the same number of special checkers as in
regular game 1. *Table stealer* doesn't apply.

### Boss game

The boss game against The Shark: all four of his abilities apply, with the
special checker counts above.

## Design notes

- The pelican stays in this biome even if a birds biome is added later.
- On the board, the Sardines come as one school that shrinks as you eat them;
  then the Shark comes for them ([decision 0008](../decisions/0008-enemies-behind-the-pass.md)).
