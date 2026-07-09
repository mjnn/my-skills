# Install bundled init skills zip via portable Python (no system python)
param(
    [string]$SkillRoot = (Split-Path $PSScriptRoot -Parent)
)

$ErrorActionPreference = 'Stop'
$runner = Join-Path $PSScriptRoot 'run_with_kit.ps1'
if (-not (Test-Path $runner)) {
    Write-Error "run_with_kit.ps1 not found; complete skill-env-setup node 4.0 first"
    exit 1
}
& powershell -ExecutionPolicy Bypass -File $runner -ScriptPath (Join-Path $PSScriptRoot 'install_init_skills.py')
exit $LASTEXITCODE
