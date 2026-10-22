---
id: "0002"
name: Tips and shop prices
date: 2026-10-21
status: accepted
tags: [economy]
summary: Start with 10 tips, earn 1 per plate served; prices by rarity.
---

## Context

The wiki left how tips are earned and what items cost TBD. The Godot build
needed numbers to make the shops playable (game decision D18).

## Decision

- A run starts with **10 tips**.
- Each plate the player serves leaves **1 tip**, win or lose, paid at the end
  of the game.
- Prices by rarity:

| Rarity    | Consumable | Relic |
|-----------|------------|-------|
| Common    | 4          | 8     |
| Rare      | 6          | 12    |
| Legendary | 9          | 16    |

- Each shop offers 3 different items. The player has 3 pockets for
  consumables; relics are unlimited but one of each.

## Alternatives considered

A flat pay per game. No currency at all until items have effects.

## Consequences

Plates are already shown on the pass shelf, so the pay is easy to read. The
numbers are first guesses, to be revisited once items have effects and
playtests exist.
