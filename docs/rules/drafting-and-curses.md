# Drafting & curses

How the player's menu changes during a run: the menu item choice (the draft),
item rarities, and cursed items that come attached to other items.

## The menu

- The **menu** is the player's whole collection of orders. It is always
  exactly **15 orders**.
- The [starting character](../characters/starting-character.md)'s menu is
  15 [Burgers](../menu-items/burger.md). Burgers have no effect.
- Browse every item in [Menu items](../menu-items/index.md).

## Menu item choice: pick 1 of 3, then swap

**When:** before the run and after each service, never after a close (see
[Order of a run](run-structure.md#order-of-a-run)).

The player is offered **3 menu items** and may add **one** of them. Adding an
item means **swapping** it with an item already on the menu, so the menu stays
at 15.

## Rarities

- **Common**, **rare** and **legendary** items.
- **Cursed** items have negative effects. They come attached to other items
  (below).

## Cursed items attached to other items

Some items come **attached to a cursed item**. When the player adds such an
item, the attached cursed item must also be added (swapped in).

In the wiki, this link is the `cursed_with` field of a menu item: it points to
the cursed item that comes attached.

### Worked example

The player starts with the starting character's menu and picks, from the 3
offered items, a rare item that comes attached to a cursed item.

| Menu before the choice | Menu after the choice |
|------------------------|-----------------------|
| 15 × Burger            | 13 × Burger           |
|                        | 1 × the rare item     |
|                        | 1 × the cursed item   |
| **15 orders**          | **15 orders**         |

!!! note "TBD"
    Whether the player can skip a choice, whether a cursed item can replace
    another cursed item, and how cursed items are removed. See
    [open questions](../decisions/open-questions.md#drafting-and-cursed-items).
