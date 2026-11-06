---
name: Vape
status: implemented
rarity: rare
tags: [buff, extra-pips]
summary: Move one checker 1 pip forward or backward.
---

## Effect

An extra move on top of your roll: move one checker 1 pip, forward or backward.

Buff: used on your own turn. Family: **Extra pips**.

## Cost & availability

Rare: 6 coins at the [consumable shop](../shops.md#consumable-shop).

## Design notes

- Part of the cheap nicotine family.
- Alternative name: Nicotine gum.
- The AI move generator must support backward moves.

## Changelog

- 2026-10-22: first draft.
- 2026-10-26: implemented in the Godot build (rules: decision D34 in the game repo).
