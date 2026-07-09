# Wrapper: check skill-kit then run a Python script with portable python
param(
    [Parameter(Mandatory = $true)]
    [string]$ScriptPath,
    [string]$SkillDir = "",
    [string[]]$ScriptArgs = @()
)

$ErrorActionPreference = "Stop"
$check = Join-Path $PSScriptRoot "check_skill_kit_ready.ps1"
if ($SkillDir) {
    & powershell -ExecutionPolicy Bypass -File $check -SkillDir $SkillDir -JsonOnly | Out-Null
    if ($LASTEXITCODE -ne 0) {
        Write-Error "skill-kit not ready (exit $LASTEXITCODE). Run skill-env-setup first."
        exit $LASTEXITCODE
    }
} else {
    & powershell -ExecutionPolicy Bypass -File $check -JsonOnly | Out-Null
    if ($LASTEXITCODE -ne 0) {
        Write-Error "skill-kit not ready. Run skill-env-setup first."
        exit $LASTEXITCODE
    }
}

. (Join-Path $PSScriptRoot "resolve_tools.ps1")
$py = Get-QoderPython
& $py $ScriptPath @ScriptArgs
exit $LASTEXITCODE
