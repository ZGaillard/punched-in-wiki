---
name: Decaf
status: implemented
rarity: common
tags: [debuff, subtract-from-dice]
summary: −1 to one die.
---

## Effect

−1 to one die.

Debuff: used against the enemy's next turn, or on your own current roll. Family: **Subtract from dice**.

## Cost & availability

Common: 4 tips at the [dish pit](../shops.md#dish-pit).

## Design notes

- Downer, mirror of [Coffee](coffee.md).
- Can target the enemy (their next turn) or yourself (your current roll), since a lower die is sometimes useful.
- A die at 0 can't move; below 0, the order moves backward. Option under discussion: cap dice at 0, since backward moves can sometimes help the enemy (hitting blots behind, rebuilding points).

- In the game, Decaf on the enemy hits the higher die of its next roll.

## Changelog

- 2026-10-22: first draft.
- 2026-10-26: implemented in the Godot build (rules: decision D34 in the game repo).
