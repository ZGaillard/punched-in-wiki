---
id: "0004"
name: Run order
date: 2026-10-22
status: accepted
tags: [run-structure]
summary: Draft and dish pit after each service; bar and staff meal after each close; a draft and the bar before the run.
---

## Context

[Decision 0003](0003-shop-order.md) put the dish pit after every game and
left open where drafting fits. The draft biomes also needed a moment for the
daily HP reset.

## Decision

The full order of a run:

0. **Before the run:** menu item choice, then the **bar** for a starting relic.
1. **First biome**
    1. Service 1, then menu item choice, then the **dish pit**.
    2. Service 2, then menu item choice, then the **dish pit**.
    3. The close, then the **bar**.
    4. **Staff meal:** heal to full HP.
2. **Second biome:** same as the first.
3. **Third biome:** same as the first.
4. **Final boss:** [The Pig](../final-boss.md).

- There is no menu item choice and no dish pit after a close.
- After the final boss, the run ends: no shop.

## Alternatives considered

The dish pit after every game, closes included (decision 0003).

## Consequences

- The dish pit is visited 6 times per run, the bar 4 times (once before the
  run, once after each close).
- The staff meal is the daily HP reset, run by
  [The Saint Bernard](../characters/the-saint-bernard.md). The player starts
  every day, and the final boss, at full HP.
