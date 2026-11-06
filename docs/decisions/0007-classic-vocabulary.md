---
id: "0007"
name: Classic backgammon vocabulary
date: 2026-11-06
status: accepted
tags: [vocabulary]
summary: Checker, board, hit, the bar, bear off and end turn replace the kitchen words; the kitchen stays in the look.
---

## Context

[Decision 0001](0001-kitchen-vocabulary.md) gave the board kitchen words
(order, pass, pillar, refire, serve, plate, bell), and the run had its own
(service, the close, tips, dish pit, bar, pockets, smoke break). Players
already know the backgammon words; the kitchen ones had to be learned and
translated back.

## Decision

The game, the wiki and the code use the classic backgammon words, and plain
words for the run:

| Was | Now |
|-----|-----|
| pass | board |
| order | checker (drawn as a bill, so also "bill") |
| pillar | bar |
| refire | hit |
| serve, plate | bear off, borne-off checker |
| ring the bell | end turn |
| service, the close | regular game, boss game |
| tips | coins |
| dish pit | consumable shop |
| bar (the relic shop) | relic shop |
| pockets | inventory |
| smoke break | pause |

The kitchen stays in the look: checkers are drawn as bills with an owner and
a dish, borne-off checkers as plates on a shelf, the end-turn button as a
bell, the pause button as a cigarette pack. The [glossary](../rules/glossary.md)
is the reference.

## Alternatives considered

"Capture" instead of "hit": plainer for newcomers, but not the backgammon
word.

## Consequences

Item, enemy and keyword texts read "when this checker is hit" or "when an
enemy checker is borne off". The relic shop is no longer called "the bar", so
"the bar" always means the board's bar. Game decision D46.
