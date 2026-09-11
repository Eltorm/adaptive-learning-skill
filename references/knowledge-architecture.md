# Knowledge graph and cognitive-path selection

Use this reference during planning whenever a topic has many plausible
connections or the user enters from a non-standard point.

## Internal graph

Represent concepts as nodes and relations as typed edges. In addition to
prerequisites and part-of edges, record causality/enabling, contrast,
shared-principle, alternative, trade-off, application, and failure-boundary
links. Give each candidate edge a strength:

`Direct` (definition or dependency), `Strong` (needed to explain a mechanism),
`Useful` (improves transfer or a decision), `Analogical` (intuition only),
`Weak`, or `Incidental`.

Keep evidence/provenance attached to claims and edges when a relationship is
interpretive, empirical, or time-sensitive. Do not infer that two nodes are
equally important merely because both are in the graph.

## Cognitive path selector

1. Generate a small set of candidate paths from the learner's entry point to
   the requested outcome.
2. Reject paths with an unmet required prerequisite, circular explanation, or
   an unnecessary return to basics. Replace a missing prerequisite with the
   shortest just-in-time bridge when possible.
3. Prefer the path that maximises target relevance and explanatory continuity
   while minimising prerequisite detours, cognitive load, and unsupported
   claims. Make the trade-off visible if two paths are genuinely different
   (e.g., intuitive/application-first versus formal/research-first).
4. Mark nodes as `mainline`, `foreshadow`, or `side-branch`. Recompute this
   selection when the learner changes goal, depth, or demonstrated mastery.

## Relationship exposure budget

The graph may contain many edges, but exposition has a budget. For each central
node, ask whether an edge is indispensable now, useful but easy to miss, or
interesting only later:

- **A / implicit:** weave Direct or Strong links into the causal prose;
- **B / explicit anchor:** briefly name a Direct/Strong or Useful link when the
  learner would likely miss it;
- **C / side branch:** defer Useful/Analogical links to a short “continue with”
  note when they serve the requested goal;
- **internal only:** leave Weak/Incidental links in the graph.

There is no fixed numeric quota. Add a link only when its explanatory benefit
exceeds its attention cost. Prefer one coherent chain over a list of related
terms, and never expose the whole graph merely to prove that it exists.
