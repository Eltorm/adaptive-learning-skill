# Opt-in learner state and review

The stateless skill can become a personal learning engine without a server by
using user-approved YAML/JSON artifacts. This is an optional protocol, not a
silent side effect.

## State files

Keep a versioned directory outside the skill package, for example
`.adaptive-learning/` in a user-selected project:

- `profile.yaml`: language, goals, constraints, background, and preferences;
- `knowledge-graph.yaml`: stable node IDs, typed edges, claim/evidence status,
  and source provenance;
- `mastery.yaml`: per-node dimension evidence, attempt date, task ID, score or
  rubric, and open gaps;
- `review-queue.yaml`: due items, interval, ease/confidence signal, and the
  next variation to retrieve;
- `sessions/`: append-only summaries linking what was taught, skipped, repaired,
  and unlocked.

Create or update these files only after the learner explicitly asks to save,
resume, track, or review progress and confirms the location if ambiguous. Do
not store secrets or unnecessary personal data. Keep a backup or emit a diff
before destructive replacement.

The optional `scripts/state_tool.py` provides explicit `init`, `record`, `due`,
`merge-graph`, `export`, `import`, and read-only `validate` commands. Call it
only with a user-approved state directory; `record` requires a node already
present in the graph and writes an atomic update to mastery and review files.
Graph merges preserve conflicting claims in a review list and mark the node
contested; exports/imports refuse to overwrite an existing destination and
reject unsafe archive paths.

## Update semantics

Use stable IDs and schema versions. A mastery record is evidence, not truth:
store the prompt/task, learner response or observation when available,
dimension, rubric result, timestamp, and evaluator uncertainty. Merge graph
updates by ID; on conflicting claims preserve both provenance and mark the
conflict for review rather than silently choosing one. Retain superseded or
retracted claims with status and reason.

## Adaptive review

Choose the next item by a combination of due date, demonstrated weakness,
prerequisite centrality, and variation from the previous task. After an
attempt, increase or decrease the interval conservatively according to the
rubric and schedule a novel surface form. A failed item should first trigger a
minimal prerequisite repair. If dates, timezone, or scheduler access are
unknown, show a suggested queue rather than pretending a reminder was set.
