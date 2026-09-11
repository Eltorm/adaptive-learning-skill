# Baseline-to-deep roadmap

The project is intentionally iterative. Each promotion requires cross-domain
tests and a recorded failure that the new rule addresses.

## V0.1 — stateless learning architect (implemented)

Topic-scale detection, minimal prerequisite analysis, internal graph, adaptive
depth, domain lenses, coherent lesson spine, evidence triage, and
reconstruction/transfer assessment. Context is the only progress store.

## V0.2 — interactive tutor (implemented as opt-in protocol)

The optional state contract now supports an explicit learner profile and
mastery records supplied by the user, error-to-prerequisite diagnosis across
turns, and a review queue. Persistence remains file-based and opt-in; the
validator and fixtures test state semantics without silently writing user data.

## V1.0 — portable personal knowledge engine (implemented subset)

The file protocol now provides a durable graph, explicit import/export,
source-bearing claims, path-selection metadata, and conflict preservation. A
hosted searchable service, automatic multi-user synchronisation, and external
reminder delivery remain out of scope; the skill must never imply they exist.
Treat stored claims as evidence-bearing data, not truth merely because they are
in the user's graph.

Every iteration should run at least three keywords from distinct domains (for
example a computing method, a historical event, and a biological mechanism),
score them with `tests/rubric.md`, and retain failures in the changelog.
