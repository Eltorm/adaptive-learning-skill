# V0.1.1 smoke-test report

Date: 2026-09-11  
Method: contract checks plus an independent behavioral simulation using
gpt-5.6-sol with low reasoning effort. The contract check is intentionally
structural; the rubric must still be applied to real model outputs when the
skill is loaded in a host.

## Iteration 1 — baseline smoke set

Keywords used (six domains/scales): `overfitting`, `TCP congestion control`,
`French Revolution`, `photosynthesis`, `eigenvalue`, `sonnet`.

Result: PASS. The baseline protocol exposed all required routing, scale,
prerequisite, graph, depth, evidence, and assessment instructions. Manual
review found two risks: a rigid lesson checklist could create repetitive prose,
and “related concepts” could become a list rather than a causal connection.

Independent behavioral scores (scale, prerequisites, depth, connections,
domain, reliability, assessment, flow): overfitting `/learn` =
`[5,4,4,4,4,4,4,4]`; French Revolution `/chapter` =
`[4,4,4,4,4,3,4,4]`; photosynthesis `/explain` =
`[5,4,4,4,5,4,4,5]`.

## Iteration 2 — targeted refinement

Keywords used (three distinct domains): `overfitting` (computing), `French
Revolution` (history), `photosynthesis` (biology).

Changes: made the lesson spine explicitly causal; marked deep-understanding
dimensions as internal rather than mandatory headings; added domain-adaptation
lenses, evidence status vocabulary, and a rule to surface only useful edges;
required an executable/applicable task at L4+; required an evidence or
interpretation anchor and causal-reconstruction check for history/social
science; allowed 1-2 high-information checks for narrow `/explain` requests.

Result: PASS via `tests/run_contract_checks.ps1`. The three examples now show
different scales and domain-appropriate checks while preserving the same
protocol. Follow-up simulation judged the three cases approximately 4.1/5,
3.9/5, and 4.4/5 respectively, with no rubric dimension below 3 after the
targeted rules. These are evaluation notes, not a guarantee of every future
generation; future iterations must score actual outputs with `tests/rubric.md`.

## Iteration 3 — cognitive path and opt-in state

Keywords used (three distinct domains): `GAE` (reinforcement learning),
`plate tectonics` (earth science), and `sonnet` (literature). The protocol now
selects a mainline/foreshadow/side-branch path, assigns relationship exposure
levels, and can persist learner-approved progress as versioned YAML. The
examples additionally demonstrate self-contained L4 inputs, delayed answer
keys, dateable historical evidence anchors, and explicit progress records.

Static and state checks: PASS. Host-level behavioral scoring for this iteration
must still be collected with the low-cost model before any further promotion.

## Iteration 4 — actionable depth and closed-loop evidence

Keywords used (three distinct domains): `overfitting` (computing), `French
Revolution` (history), and `photosynthesis` (biology).

Observed failures from the 5.6-sol/low independent pass were converted into
rules and examples: self-contained L4 inputs plus delayed rubric, concrete
dateable historical anchors plus competing readings, and two scored biology
prediction checks with prerequisite repair mapping. `state_tool.py` was run in
a temporary user-approved directory through `init`, `record`, `due`, and
`validate`; a separate invalid-cycle fixture was rejected. Static contract and
state checks both PASS. These checks establish the protocol and invariants;
future host-level generations should still be scored with `tests/rubric.md`.

## Reproduce

```powershell
pwsh -File tests/run_contract_checks.ps1 -KeywordsCsv 'overfitting|French Revolution|photosynthesis'
```

The next iteration should load the skill in a real model host, run at least
three cross-domain requests, attach scored outputs, and change only rules
supported by observed failures.

## Iteration 5 — portable knowledge engine invariants

Keywords used (three distinct domains): `GAE` (reinforcement learning), `plate
tectonics` (earth science), and `sonnet` (literature). The keyword contract
check passed while the state tool was exercised independently: graph merge
preserved a conflicting claim as `contested`, archive export/import round-tripped
the state, valid state passed, and a prerequisite cycle was rejected. No
personal state is stored in this repository; all writes occurred in a temporary
test directory and were removed after verification.
