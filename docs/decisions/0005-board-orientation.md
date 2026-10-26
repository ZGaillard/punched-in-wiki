---
id: "0005"
name: The player plays clockwise, in a fixed colour
date: 2026-10-26
status: accepted
tags: [board, art]
summary: The player moves clockwise with their home board at the bottom left; the player's colour is fixed and enemies are tinted by biome.
---

## Context

In classic backgammon, the direction of play depends on where the players sit,
not on the colour of their checkers. The Godot build lets the player pick
White (anticlockwise, home board at the bottom right) or Black (clockwise,
home board at the bottom left). Both directions are legal and common. Pro
backgammon software shows the player at the bottom and offers the direction
as a display setting.

The plate shelf is drawn in the left window of the pass art.

## Decision

- The player is always at the bottom of the pass and moves **clockwise**,
  with their **home board at the bottom left**. The enemy plays the mirror
  image, with its home board at the top left.
- The player's orders have one **fixed colour**. Enemy orders are tinted by
  **biome**: e.g. The Shark's marine animals are shades of blue.

## Alternatives considered

- **Anticlockwise, home board at the bottom right:** the layout of most
  diagrams and the default of most backgammon software. Rejected because both
  home boards would sit at the opposite end from the plate shelf, so every
  served order would fly across the pillar.
- **Letting the player choose White or Black,** as the build does now.

## Consequences

- Both home boards sit next to the plate shelf: every plate lands near the
  point it was served from.
- Rule, item and enemy texts never say "left" or "right". They use home
  board, outer board, point numbers counted from the mover's side (24 down
  to 1), and "in front of" / "behind", so that a mirrored board can be added
  later.
- Built in the Godot build (26 October 2026): the side choice is gone; the
  player is White and plays clockwise. Biome tints are not built yet.
- An option to switch the direction is in the
  [parking lot](../parking-lot.md#board-direction).
- Each biome needs a colour palette. The player's colour must stay out of
  every biome's palette. Special orders have to stand out within their
  biome's palette by more than a shade (an icon or a mark, for example).
