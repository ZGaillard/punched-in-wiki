# Working with agents

Most of the code is written by AI agents, each handed one goal. This page is
how that works, for humans steering it.

## Who owns which fact

| Fact | Where |
|------|-------|
| What the game should be: rules, items, biomes, characters, design decisions | This wiki |
| How the code works now | The game repository's `docs/` |
| What is built | The game's `docs/status.md`, and each wiki page's `status:` |
| Work to do | The game's `docs/tasks/`, one file per goal |
| Technical decisions | The game's `docs/decisions.md` |
| What each session did | The game's `docs/log/`, one file per month |

The game's docs link to this wiki and never restate it.

## From a goal to a change

1. A goal becomes a **task file** in the game's `docs/tasks/backlog/`, from
   its template: the goal, what to read, the scope, the decisions already
   made, **open questions for you**, acceptance criteria and how to verify.
2. An agent starts by asking the open questions, then moves the file to
   `active/`.
3. It works within the task's scope, with the role prompt that fits
   (`docs/roles/`: architect, gameplay, visuals, reviewer, rules tester, docs
   keeper).
4. When done it moves the file to `done/` with its result filled in.

## Definition of done

Every change, by any agent:

1. `tools/check.sh` passes, with tests for any new or changed rule.
2. The game's docs and `status.md` match the code.
3. Decisions are recorded: technical ones in the game's `decisions.md`, design
   ones in this wiki's [Decisions](../decisions/index.md).
4. A wiki page's `status:` changes to `implemented` when its feature lands.
5. A log entry is added.

Commits happen only when you ask for them.
