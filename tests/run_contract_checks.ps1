param(
  [string]$SkillRoot = (Split-Path -Parent $PSScriptRoot),
  [string]$KeywordsCsv = 'overfitting|TCP congestion control|French Revolution|photosynthesis|eigenvalue|sonnet'
)

$ErrorActionPreference = 'Stop'
$Keywords = @($KeywordsCsv -split '\|') | Where-Object { $_.Trim().Length -gt 0 }
$skill = Get-Content -Raw (Join-Path $SkillRoot 'SKILL.md')
$required = @('Topic scale controls breadth','Mastery depth','Prerequisites and entry diagnostic','Internal knowledge model','cognitive path','relationship','persistent record','Evidence and reliability','Final quality gate','/learn','/chapter','/practice','reconstruction','transfer','executable/applicable task','causal-reconstruction','writing-guidelines')
$missing = @($required | Where-Object { $skill -notmatch [regex]::Escape($_) })
if ($missing.Count -gt 0) { throw "Missing required contract anchors: $($missing -join ', ')" }
if ($Keywords.Count -lt 3) { throw 'Each test run must include at least three keywords.' }
$domainMap = @{
  'overfitting' = 'computing'
  'TCP congestion control' = 'computing'
  'French Revolution' = 'history'
  'photosynthesis' = 'biology'
  'eigenvalue' = 'mathematics'
  'sonnet' = 'literature'
  'GAE' = 'reinforcement-learning'
  'plate tectonics' = 'earth-science'
}
$domains = @($Keywords | ForEach-Object { if ($domainMap.ContainsKey($_)) { $domainMap[$_] } else { 'unclassified' } } | Select-Object -Unique)
if ($domains.Count -lt 3) { throw "Each test run must cover at least three domain families; got: $($domains -join ', ')" }
$caseText = Get-Content -Raw (Join-Path $SkillRoot 'tests/cases.md')
foreach ($k in $Keywords) {
  if ($caseText -notmatch [regex]::Escape($k)) { throw "Keyword is not represented in tests/cases.md: $k" }
}
foreach ($path in @('references/output-protocol.md','references/evidence-verification.md','references/domain-adaptation.md','references/assessment.md','references/iteration-roadmap.md','references/requirements-trace.md','references/knowledge-architecture.md','references/writing-guidelines.md','references/state-management.md','schemas/concept.yaml','schemas/curriculum.yaml','schemas/evidence.yaml','schemas/profile.yaml','schemas/mastery.yaml','schemas/review-queue.yaml','schemas/knowledge-graph.yaml','schemas/session.yaml','scripts/validate_state.py','scripts/state_tool.py','tests/run_state_checks.ps1','tests/fixtures/state/incoming-graph.yaml')) {
  if (-not (Test-Path (Join-Path $SkillRoot $path))) { throw "Missing referenced resource: $path" }
}
python (Join-Path $SkillRoot 'scripts/validate_state.py') (Join-Path $SkillRoot 'tests/fixtures/state')
pwsh -File (Join-Path $SkillRoot 'tests/run_state_checks.ps1')
Write-Output "PASS: $($Keywords.Count) keywords across distinct domain cases; contract anchors and references present."
