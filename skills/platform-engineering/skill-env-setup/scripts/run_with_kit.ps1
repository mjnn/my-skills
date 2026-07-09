# Run a Python script using portable skill-kit Python
param(
    [Parameter(Mandatory = $true)]
    [string]$ScriptPath,
    [string[]]$ScriptArgs = @()
)

$ErrorActionPreference = "Stop"
$kitRoot = Join-Path $env:USERPROFILE ".qoder-cn\tools\skill-kit"
$resolve = Join-Path $kitRoot "scripts\resolve_tools.ps1"
if (-not (Test-Path $resolve)) {
    $resolve = Join-Path $PSScriptRoot "..\..\skill-kit\scripts\resolve_tools.ps1"
}
if (-not (Test-Path $resolve)) {
    Write-Error "skill-kit not installed. Run install_skill_kit.ps1 first."
    exit 1
}
. $resolve
$py = Get-QoderPython
& $py $ScriptPath @ScriptArgs
exit $LASTEXITCODE
