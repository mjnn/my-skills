param(
    [Parameter(Mandatory = $true)]
    [string]$SkillDir
)

$ErrorActionPreference = "Stop"
. (Join-Path $PSScriptRoot "resolve_tools.ps1")

$python = Get-QoderPython
$linkScript = Join-Path $PSScriptRoot "link_python_packages.py"
if (-not (Test-Path $linkScript)) {
    Write-Error "link_python_packages.py not found"
    exit 1
}

& $python $linkScript --skill-dir $SkillDir
exit $LASTEXITCODE
