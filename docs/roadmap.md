# Roadmap

The project's milestones, in order, and where each one stands. The game is
built in Godot 4.7 in its own repository
([`ZGaillard/punched-in-v-0`](https://github.com/ZGaillard/punched-in-v-0));
this wiki holds the design. Each milestone is broken into task files in the
game repository's `docs/tasks/backlog/` (named in *italics* below). See
[Build](build/index.md) for what exists today.

| # | Milestone | Goal | Status |
|---|-----------|------|--------|
| 1 | Foundations | One board scene, feature folders, committed tests, docs that stay true, goals as task files. | Done |
| 2 | The AI opponent | The enemy plays itself: a full-turn search with a weighted evaluation, a style per biome and a hint per special checker; who plays each side. See [Enemy AI](ai.md). *ai-opponent*, *side-controllers*, then *shark-boss-ai*. | In progress: the base AI and the Shark's styles and hints are built |
| 3 | HP and losing the run | 15 HP a day, damage from borne-off enemy checkers, losing the run, the staff meal. *hp-and-damage*. | Done: HP, live damage, losing the run, the staff meal (no screen yet) |
| 4 | Enemies | Minions and bosses with their special checkers in every biome, and their colours. *shark-boss*, *enemy-tint-by-biome*, *bill-identity-in-codes*. | In progress: the Shark's three minions are built |
| 5 | Biome rules | One rule per biome, in every game of that biome. | In progress: Riptide (the Shark) is built |
| 6 | Menu drafting and curses | The player's 15 checkers as a menu, drafted between games; curses. See [Drafting & curses](rules/drafting-and-curses.md). | Not started |
| 7 | Relic effects | Relics do what their pages say, on one hook system shared with special checkers and biome rules. *rule-hooks-design*, then *relic-effects*. | Not started |
| 8 | The final boss | The Pig and the final game. See [Final boss](final-boss.md). | Not started |
| 9 | Meta-progression | What carries over between runs. See [Meta progression](meta-progression.md). | Not started |

Smaller tasks that fit in anywhere: *consumable-stacking*, *debug-menu-todos*,
*art-remaining*, *cursor-polish*, *merge-boardview-artboard*,
*shop-offer-in-run*.

!!! note "Order"
    This order was proposed during the 2026-11 refactor and taken as is. Change
    it here when priorities change.
