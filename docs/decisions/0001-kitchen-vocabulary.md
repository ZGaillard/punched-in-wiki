---
id: "0001"
name: Kitchen vocabulary for the board
date: 2026-10-20
status: accepted
tags: [vocabulary]
summary: Order, point, pillar, refire, serve and plate replace the backgammon terms.
---

## Context

The wiki first called a point holding checkers a **bill** and a hit checker
**refired** (standing for backgammon's "bar"). The Godot build settled on its
own set of words (game decision D7), used in the code, the UI and its docs.
The two had to match before art and content arrive.

## Decision

| Backgammon        | Punched In        |
|-------------------|-------------------|
| board             | pass              |
| checker           | order             |
| point             | point             |
| bar               | pillar            |
| hit               | refire            |
| bear off          | serve             |
| borne-off checker | plate             |

"Bill" is dropped. The [glossary](../rules/glossary.md) is the reference.

## Alternatives considered

Keeping "bill" for a point: an extra word for something players already know
as a point, and the game code doesn't use it.

## Consequences

Item, enemy and keyword texts use these words, e.g. "when this order is
refired" or "when an enemy order is served".
