# Adaptive Learning Skill

[简体中文](README.zh-CN.md)

Turn a topic, question, or arbitrary entry point into a dependency-aware
learning path and teaching material with adaptive depth, meaningful
cross-connections, evidence handling, and reconstruction-based assessment.

This repository contains the V0.2 opt-in tutor protocol built on the V0.1
baseline. It is a playbook plus portable state contracts, not a hosted database
or web application. The design follows
the progression:

`information → knowledge → curriculum → mastery`

## What it does

- detects whether a request is a term, concept, method, tool, subfield, field,
  or interdisciplinary problem and scales the response accordingly;
- starts from what the learner already knows instead of forcing a full basics
  course;
- builds an internal hierarchy/dependency graph and exposes only useful links;
- adapts explanations to mathematics, science, computing, history, medicine,
  humanities, and mixed domains without hard-coding one discipline;
- uses L0–L6 mastery targets, examples, boundaries, practice, and transfer
  checks;
- selects a cognitive path and budgets which graph relationships are exposed as
  mainline, foreshadowing, or deferred branches;
- marks uncertainty and verifies time-sensitive, contested, research, and
  version-sensitive claims when tools are available.
- optionally tracks a user-approved profile, knowledge graph, mastery evidence,
  sessions, and review queue in portable YAML files.

## Use

Install or load this folder as a Codex skill. Then use natural language or the
optional routes:

```text
/learn overfitting
/learn French Revolution — I know the chronology but not the causes
/chapter scaled dot-product attention, target L3
/explain why photosynthesis needs both light reactions and the Calvin cycle
/practice TCP congestion control at L4
/test PID controller
/review
```

The skill keeps its internal graph richer than the prose so lessons remain a
coherent cognitive journey rather than a list of “related concepts”.

## Repository map

- `SKILL.md` — runtime instructions and output contracts;
- `references/` — progressive-detail protocols for evidence, domains,
  assessment, path selection, state, and staged evolution;
- `schemas/` — optional YAML shapes for interoperable graph, state, and evidence;
- `scripts/validate_state.py` — read-only validator for a user-approved state
  directory;
- `scripts/state_tool.py` — explicit `init`, `record`, `due`, and `validate`
  operations for opt-in progress tracking;
- `examples/` — compact good/bad patterns across domains;
- `examples/gae.md` — a worked cognitive-path and relationship-budget pattern;
- `tests/` — cross-domain cases, rubric, and repeatable contract checks;
- `CHANGELOG.md` — what is implemented versus intentionally deferred.

## Iteration policy

V0.1 proves the seven core capabilities. V0.2 adds opt-in file-based state and
path selection without silently persisting personal data. The V1.0 protocol
adds portable graph merge and archive import/export; hosted search, reminders,
and multi-user synchronisation remain out of scope. Run the cross-domain checks
after every instruction change, record observed failures, and promote only
demonstrated improvements (see `references/iteration-roadmap.md`).

Example state workflow (only after the learner explicitly requests saving
progress):

```powershell
python scripts/state_tool.py init .adaptive-learning
python scripts/state_tool.py validate .adaptive-learning
python scripts/state_tool.py due .adaptive-learning --at 2026-09-12
python scripts/state_tool.py export .adaptive-learning backup.zip
```

## License

MIT; see `LICENSE`.
