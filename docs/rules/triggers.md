# Triggers

The moments an effect can react to, for menu items, relics and consumables.
Item texts should use these wordings so the same trigger always reads the
same way. Words like *hit*, *bear off* and *bar* are defined in the
[glossary](glossary.md); named effects are in [Keywords](../keywords/index.md).

!!! info "Draft"
    Every trigger here is a candidate (`status: idea`).

## Simple triggers

| Trigger | Fires when |
|---------|------------|
| When a checker moves | One of your checkers moves. |
| When hitting an enemy checker | You hit an enemy blot. |
| When one of your checkers is hit | The enemy hits one of your blots. |
| When bearing off | You bear off a checker. |
| When the enemy bears off | The enemy bears off a checker. |
| When a move is forced | Only one legal move is available. |
| When rolling doubles | Your roll is a double. |
| When entering from the bar | One of your checkers re-enters the board. |
| When hitting from the bar | A checker entering from the bar lands on an enemy blot. |
| When ending your turn | At the end of your turn; checks the board, e.g. "if this checker is still a blot". |
| When making a new point | A second order of yours lands on a point. |
| When leaving a blot | One of your points drops to a single checker. |
| When contact breaks | The game becomes a pure race. |

## Complex triggers

| Trigger | Fires when |
|---------|------------|
| Jumping over a point | A checker jumps over an enemy-made point, or over a wall of several. |
| X checkers on the bar | X checkers are on the bar: yours, the enemy's, or both. |
| Clearing a quadrant | None of your checkers are left in one of the 4 quarters of the board. |
| Alone in a quadrant | A checker is the only one of yours in its quarter, or the only checker of either side. |
| Completing an X-point wall | X consecutive points are each held by 2+ of your checkers, anywhere on the board. One-shot. |
| Part of an X-point wall | Ongoing: lasts while the checker stays in such a wall. |
