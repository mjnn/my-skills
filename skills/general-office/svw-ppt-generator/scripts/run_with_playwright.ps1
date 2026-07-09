# Run a Python script with vendor Playwright browsers (offline path)
param(
    [Parameter(Mandatory = $true)]
    [string]$ScriptPath,
    [string[]]$ScriptArgs = @()
)

$ErrorActionPreference = "Stop"
$skillRoot = Split-Path $PSScriptRoot -Parent
$kit = Join-Path $env:USERPROFILE ".qoder-cn\tools\skill-kit\scripts\run_skill_script.ps1"
$env:PLAYWRIGHT_BROWSERS_PATH = Join-Path $skillRoot "vendor\playwright-browsers"

& powershell -ExecutionPolicy Bypass -File $kit -ScriptPath $ScriptPath -SkillDir $skillRoot -ScriptArgs $ScriptArgs
exit $LASTEXITCODE
