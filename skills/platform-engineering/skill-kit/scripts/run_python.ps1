param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Args
)

$ErrorActionPreference = "Stop"
. (Join-Path $PSScriptRoot "resolve_tools.ps1")
$python = Get-QoderPython
& $python @Args
exit $LASTEXITCODE
