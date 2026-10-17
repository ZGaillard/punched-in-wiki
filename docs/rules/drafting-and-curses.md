# Drafting & curses

How the player's menu changes during a run: the draft between games, item
rarities, and cursed items that come attached to other items.

## The menu

- The **menu** is the player's whole collection of checkers. It is always
  exactly **15 checkers**.
- The starting menu of the basic starting character is 15 **Burgers**.
  Burgers have no effect.

## Drafting: pick 1 of 3, then swap

Between games, the player is offered **3 menu items** and may add **one** of
them. Adding an item means **swapping** it with an item already on the menu, so
the menu stays at 15.

## Rarities

| Rarity    | Notes                         |
|-----------|-------------------------------|
| Common    |                               |
| Rare      |                               |
| Legendary |                               |
| Cursed    | Cursed items have negative effects. |

## Cursed items attached to other items

Some items come **attached to a cursed item**. When the player adds such an
item, the attached cursed item must also be added (swapped in).

In the wiki, this link is the `cursed_with` field of a menu item: it points to
the cursed item that comes attached.

### Worked example

The player starts with the basic starting character's menu and picks, from
the 3 offered items, a rare item that comes attached to a cursed item.

| Menu before the draft | Menu after the draft  |
|-----------------------|-----------------------|
| 15 × Burger           | 13 × Burger           |
|                       | 1 × the rare item     |
|                       | 1 × the cursed item   |
| **15 checkers**       | **15 checkers**       |

!!! note "TBD"
    Whether the player can skip a draft, whether a cursed item can replace
    another cursed item, and how cursed items are removed. See
    [open questions](../decisions/open-questions.md).
