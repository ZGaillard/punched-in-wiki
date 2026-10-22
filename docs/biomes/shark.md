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
- **Keyword:** [hit boost](../keywords/hit-boost.md), the enemy gets a boost from refiring your orders.

### Biome rule: Riptide

Applies in every game of the biome.

- At the end of each turn, your blots drift backward by random pips: **1 on
  day 1, 2 on day 2, 3 on day 3**, spread over the same or different blots.
- Only your blots are affected, never the enemy's.

## Boss: *The Shark*

Character page: [The Shark](../characters/the-shark.md).

### Description

The classic aggressive server who steals tables.

### Special orders

- **Blood in the water** (ability): every time he refires one of your orders,
  he gets a free extra 1-pip move.
- **Feeding frenzy orders:** cost you **2 HP** when served instead of 1.
- **Shark bite orders** (separate from Feeding frenzy): when one refires your
  order, that order loses its menu effect for the rest of the game.
- **Table stealer** (ability, close only, not when he shows up in the second
  service): on the first turn, he takes your rarest order and places it on the
  furthest point from his home board. It plays for him, keeping its menu
  effect.

| Day | Feeding frenzy | Shark bite | Total special |
|-----|----------------|------------|---------------|
| 1   | 2              | 2          | 4             |
| 2   | 4              | 4          | 8             |
| 3   | 8              | 7          | 15 (all)      |

### Placement rule

Standard backgammon starting setup, except for *Table stealer*, which moves
your rarest order on the first turn.

### Behaviour / AI notes

Aggressive: fits the **Blitzer** personality.

## Minion 1: Sardine

Character page: [Sardine](../characters/sardine.md).

### Description

Strong in a group, weak alone.

### Special orders

Special orders: **2 / 3 / 4** by day.

- **School speed** (special orders only): when it moves from a point shared
  with another Sardine order (special or not), it moves 1 extra pip.
- **Eaten alone** (all 5 Sardine orders): if you refire a Sardine that was
  alone, it's removed from the game for good.

### Placement rule

Standard backgammon starting setup.

### Behaviour / AI notes

Shares the minions' single AI (see [Game notes](#game-notes)).

## Minion 2: Pufferfish

Character page: [Pufferfish](../characters/pufferfish.md).

### Description

Buff only.

### Special orders

Special orders: **1 / 2 / 3** by day.

- **Deflated:** if it moved during the enemy's last turn, it can be hit like
  any blot.
- **Puffed up:** if it didn't move during the enemy's last turn, hitting it
  sends your hitting order to the pillar too.

### Placement rule

Standard backgammon starting setup.

### Behaviour / AI notes

Shares the minions' single AI (see [Game notes](#game-notes)).

## Minion 3: Pelican

Character page: [Pelican](../characters/pelican.md).

### Description

!!! note "TBD"
    Who this minion is and how it plays.

### Special orders

Special orders: **2 / 3 / 4** by day.

- **Numbness:** when a special Pelican refires one of your orders, that order
  is caught in its pouch and frozen for 1 turn before going to the pillar.

### Placement rule

Standard backgammon starting setup.

### Behaviour / AI notes

Shares the minions' single AI (see [Game notes](#game-notes)).

## Game notes

The three minions share one AI and play as a single player: one enemy turn,
one roll. Each minion owns 5 of the enemy's 15 orders and only provides its
special orders and their effects.

| Day | Sardine | Pufferfish | Pelican | Service 1 | Service 2 (+ Shark) | Close |
|-----|---------|------------|---------|-----------|---------------------|-------|
| 1   | 2       | 1          | 2       | 5         | 6                   | 4     |
| 2   | 3       | 2          | 3       | 8         | 10                  | 8     |
| 3   | 4       | 3          | 4       | 11        | 14                  | 15    |

### Service 1

The three minions only; no Shark orders.

### Service 2

The Shark shows up early: he replaces **1 / 2 / 3** (by day) of his minions'
non-special orders with his own, **Shark bite only** (Feeding frenzy is saved
for the close). Minions keep the same number of special orders as in
service 1. *Table stealer* doesn't apply.

### Boss game

The close against The Shark: all four of his abilities apply, with the
special order counts above.

## Design notes

- The pelican stays in this biome even if a birds biome is added later.
