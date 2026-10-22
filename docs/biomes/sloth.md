---
name: TBD
boss: The Sloth
status: approved
summary: Forest animals, the busboys. Slow and defensive; they build walls.
---

The biome tied to **The Sloth**. This page collects everything about the biome: its identity, its boss, its three minions and notes on each of its games. The biome's name is not decided yet, so the page is titled after its boss.

!!! info "Draft"
    Everything below the overview is `status: idea`.

## Overview

- **Animals:** forest animals.
- **Role:** the busboys. Slow and defensive; they build lots of walls.
- **Keyword:** [mistakes](../keywords/mistakes.md), the boss's errors cause you problems during the
  game.

### Biome rule: Overgrowth

Applies in every game of the biome.

- At the start of the game, random empty points are blocked: **1 on day 1,
  2 on day 2, 3 on day 3**. Neither side can use them.
- **Counterplay:** instead of moving, spend a die to clear a blocked point at
  exactly that distance from one of your orders.

## Boss: *The Sloth*

Character page: [The Sloth](../characters/the-sloth.md).

### Description

The slow, defensive, clumsy busboy.

### Special orders

- **Butterfingers orders:** when one is the last order moved off a point, it
  drops a **dirty plate** there for **1 / 2 / 3 turns** by day. The Sloth's
  orders can land on plates; yours can't.
- **Spill orders:** when you refire one, dirty plates appear on both
  neighbouring points (same effect and duration).
- **Plate counterplay:** refiring a Sloth order clears his nearest plate; you
  can also spend a die to clear a plate at exactly that distance.
- Overgrowth stays neutral in the close: the Sloth can't use blocked points,
  only his plates.

| Day | Butterfingers | Spill | Total special |
|-----|---------------|-------|---------------|
| 1   | 4             | 2     | 6             |
| 2   | 6             | 4     | 10            |
| 3   | 9             | 6     | 15 (all)      |

### Placement rule

Standard backgammon starting setup; Overgrowth blocks random empty points at
the start.

### Behaviour / AI notes

Slow and defensive, builds walls: fits the **Primer** / **Cautious**
personalities.

## Minion 1: Beaver

Character page: [Beaver](../characters/beaver.md).

### Description

Builds walls.

### Special orders

Special orders: **1 active** every day, plus **1 / 2 / 3 passive** by day
(2 / 3 / 4 in total).

- **Flood** (active, when it completes a 3-point wall): at any distance in
  front of the wall, the first point you occupy is pushed back as a whole
  stack, **1 / 2 / 3 points** by day. It can land on your own orders; if an
  enemy point blocks, it stops on the last free point.
- **Gnaw** (passive, at the start of every enemy turn while part of a wall):
  within the 6 points in front of the wall, your first blot is pushed back
  1 pip. Blocked by enemy points.

### Placement rule

Standard backgammon starting setup.

### Behaviour / AI notes

Shares the minions' single AI (see [Game notes](#game-notes)).

## Minion 2: Capybara

Character page: [Capybara](../characters/capybara.md).

### Description

Defensive support.

### Special orders

Special orders: **1 / 2 / 3** by day.

- **Chill zone:** enemy blots on the points on either side of a special
  Capybara can't be hit. The Capybara itself isn't protected: alone it can be
  hit, breaking the zone; on a made point it's safe and keeps protecting.

### Placement rule

Standard backgammon starting setup.

### Behaviour / AI notes

Shares the minions' single AI (see [Game notes](#game-notes)).

## Minion 3: Deer

Character page: [Deer](../characters/deer.md).

### Description

Runs away.

### Special orders

Special orders: **3 / 4 / 5** by day (an exception to the usual 2 / 3 / 4).

- **Escape** (once per special order per game): when refired, it rolls one
  die and runs forward by that number instead of going to the pillar. If it
  would land on a blocked point or on your blot, it's caught anyway.

### Placement rule

Standard backgammon starting setup.

### Behaviour / AI notes

Shares the minions' single AI (see [Game notes](#game-notes)).

## Game notes

The three minions share one AI and play as a single player: one enemy turn,
one roll. Each minion owns 5 of the enemy's 15 orders and only provides its
special orders and their effects.

| Day | Beaver | Capybara | Deer | Service 1 | Service 2 (+ Sloth) | Close |
|-----|--------|----------|------|-----------|---------------------|-------|
| 1   | 2      | 1        | 3    | 6         | 7                   | 6     |
| 2   | 3      | 2        | 4    | 9         | 11                  | 10    |
| 3   | 4      | 3        | 5    | 12        | 15                  | 15    |

### Service 1

The three minions only; no Sloth orders.

### Service 2

The Sloth shows up early: **1 / 2 / 3 Butterfingers** orders by day replace
non-special minion orders. Spill is saved for the close.

### Boss game

The close against The Sloth, with the special order counts above.

## Design notes

- **On ice:** let some special orders move onto blocked points; limit
  Overgrowth blocks to the 2nd and 3rd quadrants.

??? abstract "Rejected / earlier versions"
    - *Clutter* became Butterfingers.
    - Beaver: Dam, Lodge, Sturdy, Busy beaver, an older Flood that pushed all
      orders.
    - Capybara: Seat for everyone, Unbothered, Mellow.
    - Deer: jump 1 or 2 pips either way.
    - Sloth: Nap, Knocked-over tray, Hanging, Heavy, Yawn, Bus tub, Wrong
      table, an enemy-only Overgrowth.
