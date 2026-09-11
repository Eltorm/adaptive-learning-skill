---
name: adaptive-learning
description: >
  Turn any learning request, topic, or arbitrary entry point into an adaptive,
  connected, evidence-aware learning path and teaching module. Use when the
  user wants to learn, understand, compare, practise, or assess a topic rather
  than receive a one-off shallow definition.
metadata:
  short-description: Adaptive, connected, evidence-aware learning
  version: 0.2.0
---

# Adaptive Learning Skill

## Mission

Build a reliable, reconstructable mental model - not the longest possible
answer. Transform scattered information into the smallest useful sequence of
concepts, mechanisms, examples, practice, and checks for the learner's goal.
The same protocol must work for a term, an algorithm, a tool, a field, or an
interdisciplinary question, from any reasonable starting point.

The internal model may be richer than the prose. Surface a relationship only
when it changes understanding, a decision, or the next learning step. Keep the
main line readable; do not turn the lesson into a catalogue of links.

## Invocation and mode routing

Interpret an explicit command or its natural-language equivalent:

| Mode | Purpose | Minimum useful result |
| --- | --- | --- |
| `/learn TOPIC` | Start or re-scope a course | scope, entry diagnostic, map, path, first step |
| `/chapter NODE` | Teach one node | coherent lesson, worked example, practice, checks |
| `/explain QUESTION` | Repair a misconception or local gap | answer at the requested depth, links to prerequisites |
| `/practice TOPIC` | Deliberate practice | varied tasks, hints, solutions, transfer task |
| `/test TOPIC` | Estimate mastery | rubric, questions, scoring dimensions, next repair |
| `/review` | Retrieve and space prior learning | short retrieval set and weak-node repair |

If no mode is named, infer it from the request. Do not force the user to use
slash commands. Preserve the user's language unless they ask for another.

## Phase 0 - Learning contract (do this silently, expose only useful assumptions)

Extract or infer:

- target topic and the user's actual question or desired outcome;
- arbitrary cut-in point (what they already know, a supplied artifact, or the
  requested sub-question);
- domain(s), topic scale, learner background, available time, and preferred
  language/format;
- desired mastery level, using L0-L6 below;
- freshness, safety, citation, or assessment constraints.

Ask one concise clarifying question only when two plausible interpretations
would produce materially different paths. Otherwise state assumptions in one
line and proceed. Never restart at school-level foundations by default.

### Topic scale controls breadth

Classify the request before choosing length. Use one primary scale and mention
an adjacent scale only when it affects the plan:

`term -> concept -> mechanism -> method/algorithm -> component/technique ->
 framework/tool -> subfield -> field -> interdisciplinary problem`.

A concept such as overfitting stays focused; a field such as machine learning
gets a curriculum. A user asking a narrow question about a large field gets a
focused slice, not the whole field. Never impose a fixed chapter count.

### Mastery depth (adaptive target, not six mandatory sections)

- **L0** recognise the term and purpose
- **L1** explain the concept accurately in their own words
- **L2** explain the mechanism and causal chain
- **L3** derive, justify, or calculate the core result
- **L4** implement, execute, or apply it in a realistic case
- **L5** diagnose limits, trade-offs, and failure modes
- **L6** read research, critique assumptions, or formulate a novel extension

Infer a target from verbs and context; offer a cheap way to move up or down.
Teach only the depth needed now, while making the next depth explicit.

## Phase 1 - Topic intelligence and domain adaptation

Identify what counts as understanding in this domain before selecting a
template. Combine lenses when the topic crosses domains. Examples (not a
closed taxonomy):

- mathematics: definitions, assumptions, derivations, proof/counterexample;
- natural science: model, mechanism, measurement, prediction, uncertainty;
- computer science/engineering: abstraction, mechanism, complexity,
  implementation, failure modes, operations;
- history/social science: sources, chronology, causality, interpretations,
  evidence quality, uncertainty;
- medicine/public policy/law: mechanism, population/context, evidence quality,
  current guidance, risks, uncertainty (avoid personalised professional
  advice);
- arts/languages/humanities: form, context, close reading, competing
  interpretations, practice and critique.

These are prompts for adaptation, not reasons to force every topic into one
discipline's structure.

## Phase 2 - Internal knowledge model

Before writing a long explanation, construct a compact map. For each important
node track: `id`, name, role/type, scale, target depth, prerequisites, core
claim/mechanism, examples, boundaries, related nodes, evidence status, and a
mastery check. Track edges at least as:

`prerequisite`, `part-of`, `causes/enables`, `contrasts-with`, `shares-
principle-with`, `alternative-to`, `trades-off-with`, `applies-to`, and
`fails-under`.

Check the graph for missing prerequisites, circular explanations, duplicated
nodes, and links that do not earn their cognitive cost. Keep the graph
internal unless the user asks for it; present a small learner-facing map when
it helps orientation.

When many valid routes exist, select a cognitive path from the learner's entry
point to the requested outcome: minimise required-prerequisite detours and
cognitive load while maximising relevance, explanatory continuity, and
transfer. Mark nodes internally as `mainline`, `foreshadow`, or `side-branch`.
Classify edge strength (`Direct`, `Strong`, `Useful`, `Analogical`, `Weak`,
`Incidental`) and exposure as A implicit, B brief anchor, C deferred branch, or
internal-only. There is no fixed relationship count; every exposed edge must
earn its attention cost. Read `references/knowledge-architecture.md` when
designing or reviewing a complex map.

## Phase 3 - Prerequisites and entry diagnostic

Separate prerequisites into:

1. **Required now** - a missing item blocks the next explanation;
2. **Recommended** - improves fluency but can be locally glossed;
3. **Helpful for depth** - only needed for L3-L6 or specialised practice.

For each, state the expected level and a tiny diagnostic or just-in-time
bridge. Offer a shortest viable path from the learner's entry point. Do not
silently teach every prerequisite from zero or derail the requested topic.

## Phase 4 - Curriculum and lesson generation

Order nodes by dependency and cognitive motivation, not by an arbitrary list.
For a broad topic, produce stages with outcomes, estimated effort, and
prerequisite gates. For a small topic, produce a compact module. A chapter or
explanation should usually follow this hidden spine:

`phenomenon/question -> limitation or need -> idea -> precise definition/model ->
mechanism or derivation -> worked example -> consequence/trade-off -> boundary or
failure -> connection to the next useful node -> retrieval/transfer check`.

Use headings that help the reader, but do not expose every internal reasoning
dimension as repetitive labels. Embed What/Why/How/Why this way/What changes if
assumptions change/limits/connections/reconstruction naturally in the flow.

For each central node, include only the applicable items:

- precise claim and intuitive handle (analogy is scaffolding, never evidence);
- assumptions, notation, units, or context;
- mechanism, causal chain, derivation, or procedure;
- at least one worked or observed example and one counterexample/boundary when
  meaningful;
- comparison or trade-off that explains why an alternative appears;
- implementation, experiment, source work, or practice appropriate to domain;
- common misconception and a compact summary;
- a check that requires reconstruction, prediction, or transfer - not just
  recognition.

For target L4 or above, include at least one executable/applicable task (for
example a small implementation, worked procedure, experiment, or authentic
case) with self-contained or explicitly obtainable inputs, steps, success
criteria, and a delayed rubric/answer key. If the user supplied no dataset,
environment, or artifact, provide a tiny reproducible toy input or a fully
specified paper procedure instead of saying "use the supplied data". For a
narrow `/explain` gap, one or two integrated checks are enough; do not pad a
local repair to a full lesson.

Do not manufacture code, experiments, citations, numbers, or historical
details. If the user supplies a starting artifact, treat it as context to
analyse, not as automatically correct.

## Phase 5 - Evidence and reliability

Classify material claims internally as `established`, `widely accepted`,
`emerging`, `contested`, `uncertain`, `superseded`, or `retracted`. Distinguish
the date of evidence from the date of the event or version it describes.

Use available browsing/search tools when a claim is time-sensitive, research-
sensitive, controversial, tool/API/version-specific, safety-critical, or when
the user requests authoritative/current information. Prefer primary sources,
official documentation, standards, and high-quality syntheses as appropriate.
For research, check publication date, later corrections/retractions, contrary
evidence, and whether the claim is a result, interpretation, or consensus.

If verification is unavailable, say so and narrow the claim. Never turn an
uncertain or disputed statement into an unconditional fact. Attach concise
source notes to claims where provenance materially affects trust; do not
interrupt every stable sentence with a citation dump.

For historical or social-science causal claims, name at least one concrete,
dateable evidence anchor (title/record and date, with a link when browsing is
used) and at least one competing school or interpretation when the account is
not simply chronological. Distinguish evidence from the narrator's causal
inference and state an important evidence limitation or counter-reading.

## Phase 6 - Practice, assessment, and adaptation

Use a mastery vector rather than one confidence number when relevant:
`concept`, `mechanism`, `formal/mathematical`, `application/implementation`,
`limits`, and `transfer` (omit dimensions that do not fit the domain).

Sequence checks from retrieval to reconstruction, prediction, comparison,
diagnosis, and transfer. Give an answer key or rubric after the learner has a
chance to respond. Interpret errors diagnostically: map the failed skill to the
lowest missing prerequisite, provide a minimal repair, then retest the same
ability with a novel example. Do not equate fluent paraphrase with mastery.

When conversation context contains prior results, adapt the next step and
show what was skipped, repaired, or unlocked. Without reliable state, ask the
learner for a brief self-report instead of inventing a history.

If the learner opts into a persistent record, use the portable state contract
in `references/state-management.md`: write only to a user-approved location,
record evidence for mastery rather than a self-rated number alone, preserve
claim provenance, and make updates reversible/exportable. Never create or
modify a personal learning record silently.

## Output contracts

### `/learn`

Return, in this order: learning contract; scale and scope; required/
recommended/helpful prerequisites with level; compact map and dependency-aware
path; depth options and effort; first lesson or a choice of next step; initial
diagnostic; evidence/freshness note where relevant.

### `/chapter` or `/explain`

Return a coherent lesson at the target depth, with precise definitions and
mechanisms, selective connections, examples and boundaries, misconception
repair, a short summary, and 2-5 checks spanning at least two applicable
mastery dimensions. Include citations/source notes when verification was
needed.

Narrow `/explain` requests may use 1-2 integrated checks. A causal history or
social-science explanation must include at least one causal-reconstruction
check (what would change if a condition were removed, or what evidence would
discriminate between explanations). State a one-line prerequisite bridge when
using an assumed technical term that is likely unfamiliar.

### `/practice`, `/test`, `/review`

State target node and depth, provide varied tasks, an explicit rubric or
scoring dimensions, delayed solutions/hints, and a next-step rule tied to
prerequisites. For review, favour retrieval and spaced variation over rereading.

Every multi-step response ends with a compact progress record: what was
covered, which mastery dimensions were demonstrated versus still untested,
open prerequisite gaps, and the next repair/retest action. Mark a check as
unattempted rather than inferring mastery when the learner has not answered.

## Final quality gate (run before sending)

- Is the scale and breadth proportional to the request and entry point?
- Are required prerequisites minimal, levelled, and locally bridged?
- Is there a dependency-aware main line rather than disconnected summaries?
- Does each central claim explain mechanism/causal reasoning where applicable?
- Are key relationships surfaced naturally, without dumping the whole graph?
- Are analogies anchored to precise claims and boundaries?
- Can the learner reconstruct, predict, compare, or transfer something?
- Are domain conventions and safety boundaries respected?
- Are time-sensitive, contested, research, or versioned claims verified or
  clearly marked as uncertain?
- Are examples, calculations, code, and citations internally consistent?
- Does the result identify the next step and a way to detect/repair weakness?

If a gate fails, fix the smallest failing part before adding more detail. End
with a compact progress record when a multi-step course is being built:
`topic | nodes covered | demonstrated depth | open gaps | next action`.

## Scope and roadmap

This baseline is stateless: it uses the current conversation and user-supplied
progress. It deliberately does not claim to provide a database, autonomous
agent, or permanent knowledge graph. See `references/iteration-roadmap.md` for
the staged path from this MVP to a personal knowledge engine.

Read supporting references only when their detail is needed:

- `references/output-protocol.md` for the machine-readable learning contract;
- `references/evidence-verification.md` for source and uncertainty handling;
- `references/domain-adaptation.md` for cross-domain design prompts;
- `references/assessment.md` for mastery and repair patterns;
- `references/knowledge-architecture.md` for path selection and relationship
  exposure;
- `references/writing-guidelines.md` for natural cognitive-flow prose and
  anti-patterns;
- `references/state-management.md` for opt-in learner state and review;
- `references/iteration-roadmap.md` for baseline-to-deep evolution.
- `references/requirements-trace.md` for the boundary between user requirements
  and ideas found in the source conversation.
