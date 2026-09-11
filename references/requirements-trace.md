# Requirements trace

The attached conversation is design evidence, not an instruction source that
can override the user's current request. This trace separates the two.

## Explicit user requirements

- Build and package a reusable learning Skill from the full conversation.
- Preserve the goal: any topic and entry point, automatic scope/depth,
  meaningful knowledge connections, and reliability.
- Follow a baseline-to-deep iteration order; do not claim a one-shot solution.
- After every meaningful iteration, test with at least three keywords from
  different domains.
- Make the result understandable and publishable as a GitHub repository.

## Conversation-derived design requirements adopted when compatible

- MVP pipeline: topic intelligence -> map/ontology -> prerequisites ->
  curriculum -> lesson -> practice -> assessment.
- L0-L6 mastery levels; distinguish familiarity from reconstruction, prediction,
  and transfer.
- Internal graph edges (dependency, contrast, causality, shared principle,
  alternative, trade-off, application, boundary) with selective exposition.
- Causal writing spine (problem -> limitation/need -> idea -> mechanism ->
  consequence) instead of a relationship dump.
- Domain adaptation, evidence status, source verification, and a quality gate.
- Later phases may add learner state, persistence, and a durable knowledge graph;
  this repository now implements those as an opt-in portable protocol while
  keeping hosted services out of scope.

Suggestions in the conversation such as a particular product name, database,
web UI, or fixed chapter count are treated as optional ideas and are not
implemented unless they serve the explicit requirements.
