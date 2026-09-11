$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
python (Join-Path $root 'scripts/validate_state.py') (Join-Path $root 'tests/fixtures/state')
$invalid = Join-Path $root 'tests/fixtures/invalid-cycle'
$output = & python (Join-Path $root 'scripts/validate_state.py') $invalid 2>&1
if ($LASTEXITCODE -eq 0 -or ($output -notmatch 'prerequisite cycle')) {
  throw 'Expected the invalid prerequisite cycle fixture to fail validation.'
}
Write-Output 'PASS: valid state accepted and prerequisite cycle rejected.'
