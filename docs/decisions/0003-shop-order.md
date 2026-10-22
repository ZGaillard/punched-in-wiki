---
id: "0003"
name: Dish pit after every game, bar after each close
date: 2026-10-21
status: accepted
tags: [run-structure]
summary: After a service, the dish pit; after a close, the dish pit then the bar.
---

## Context

The wiki said the dish pit comes "between games" and the bar "between days",
and left their exact order TBD. The Godot run loop needed one (game decision
D17).

## Decision

- After every game (service or close), the player visits the **dish pit**.
- After a **close**, the player visits the dish pit, then the **bar**, then
  the next day starts.
- After the final boss, the run ends: no shop.

## Alternatives considered

Bar before dish pit. Shops opened only from the game-over screen.

## Consequences

Where drafting fits in this sequence is still open.
