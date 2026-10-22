# Triggers

The moments an effect can react to, for menu items, relics and consumables.
Item texts should use these wordings so the same trigger always reads the
same way. Words like *refire*, *serve* and *pillar* are defined in the
[glossary](glossary.md); named effects are in [Keywords](../keywords/index.md).

!!! info "Draft"
    Every trigger here is a candidate (`status: idea`).

## Simple triggers

| Trigger | Fires when |
|---------|------------|
| When an order moves | One of your orders moves. |
| When refiring an enemy order | You hit an enemy blot. |
| When one of your orders is refired | The enemy hits one of your blots. |
| When serving | You bear off an order. |
| When the enemy serves | The enemy bears off an order. |
| When a move is forced | Only one legal move is available. |
| When rolling doubles | Your roll is a double. |
| When entering from the pillar | One of your orders re-enters the board. |
| When hitting from the pillar | An order entering from the pillar lands on an enemy blot. |
| When ringing the bell | At the end of your turn; checks the board, e.g. "if this order is still a blot". |
| When making a new point | A second order of yours lands on a point. |
| When leaving a blot | One of your points drops to a single order. |
| When contact breaks | The game becomes a pure race. |

## Complex triggers

| Trigger | Fires when |
|---------|------------|
| Jumping over a point | An order jumps over an enemy-made point, or over a wall of several. |
| X orders on the pillar | X orders are on the pillar: yours, the enemy's, or both. |
| Clearing a quadrant | None of your orders are left in one of the 4 quarters of the board. |
| Alone in a quadrant | An order is the only one of yours in its quarter, or the only order of either side. |
| Completing an X-point wall | X consecutive points are each held by 2+ of your orders, anywhere on the board. One-shot. |
| Part of an X-point wall | Ongoing: lasts while the order stays in such a wall. |
