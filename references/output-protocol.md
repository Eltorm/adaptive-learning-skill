# Learning contract (optional structured form)

Use this shape when a user wants a reusable plan, asks for machine-readable
output, or a later session needs to resume. Omit fields that do not apply; do
not fabricate learner state.

```yaml
learning_contract:
  topic: ""
  learner_goal: ""
  entry_point: ""
  domain: []
  scale: term|concept|mechanism|method|algorithm|component|framework|subfield|field|interdisciplinary
  target_depth: L0|L1|L2|L3|L4|L5|L6
  constraints:
    time: ""
    format: ""
    language: ""
    freshness_required: false
  assumptions: []

prerequisites:
  required: [{id: "", expected_level: "", diagnostic: "", bridge: ""}]
  recommended: []
  helpful_advanced: []

nodes:
  - id: ""
    name: ""
    role: concept|mechanism|method|example|boundary|skill
    path_role: mainline|foreshadow|side-branch
    target_depth: L1
    prerequisites: []
    edges: [{type: prerequisite, to: "", strength: Direct, exposure: A}]
    core_claim: ""
    mastery_checks: []

path:
  - stage: 1
    outcome: ""
    node_ids: []
    gate: ""

evidence:
  - claim: ""
    status: established|widely_accepted|emerging|contested|uncertain|superseded|retracted
    temporal_sensitivity: low|medium|high
    sources: []
    verified_at: ""

assessment:
  dimensions: [concept, mechanism, transfer]
  tasks: []
  next_step_rule: ""
```

The structured form is a planning aid, not a promise that every lesson must
show JSON/YAML. Human-facing prose should remain readable.
