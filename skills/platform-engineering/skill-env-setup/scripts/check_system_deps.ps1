# Node 0: system dependency check without assuming Python/Git/curl/tar
param(
    [switch]$ReportAuto,
    [string]$ReportPath = ""
)

$ErrorActionPreference = "Continue"

function Test-Command {
    param([string]$Name, [string[]]$CmdArgs = @("--version"))
    if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
        return @{ ok = $false; detail = "not found" }
    }
    try {
        $p = Start-Process -FilePath $Name -ArgumentList $CmdArgs -NoNewWindow -Wait -PassThru `
            -RedirectStandardOutput "$env:TEMP\qoder-dep-out.txt" `
            -RedirectStandardError "$env:TEMP\qoder-dep-err.txt"
        $out = Get-Content "$env:TEMP\qoder-dep-out.txt" -ErrorAction SilentlyContinue | Select-Object -First 1
        return @{ ok = ($p.ExitCode -eq 0); detail = "$out" }
    } catch {
        return @{ ok = $false; detail = $_.Exception.Message }
    }
}

function Find-SkillKitAssets {
    $roots = @(
        (Join-Path $PSScriptRoot "..\assets\skill-kit"),
        (Join-Path $env:USERPROFILE ".qoder-cn\skills\skill-env-setup\assets\skill-kit"),
        (Join-Path $env:USERPROFILE ".qoder-cn\skills\skill-kit\assets")
    )
    foreach ($r in $roots) {
        if ((Test-Path (Join-Path $r "7za.exe")) -and (Test-Path (Join-Path $r "python.7z"))) {
            return $r
        }
    }
    return $null
}

$isWindows = $env:OS -like "*Windows*"
$os = if ($isWindows) { "Windows $($PSVersionTable.OS)" } else { [System.Environment]::OSVersion.VersionString }

$qoder = Test-Command -Name "qoder-cn" -CmdArgs @("--version")
$psVer = $PSVersionTable.PSVersion
$psOk = $psVer.Major -ge 5

$assets = Find-SkillKitAssets
$kitFiles = @()
$kitOk = $false
if ($assets) {
    foreach ($f in @("7za.exe", "python.7z", "python312.zip", "python312._pth")) {
        if (Test-Path (Join-Path $assets $f)) { $kitFiles += $f }
    }
    $gitDir = Join-Path $assets "git"
    $parentGit = Join-Path (Split-Path $assets -Parent) "git"
    $hasGit = Get-ChildItem -Path @($gitDir, $parentGit) -Filter "MinGit-*-64-bit.zip" -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($hasGit) { $kitFiles += "MinGit.zip" }
    $kitOk = ($kitFiles -contains "7za.exe") -and ($kitFiles -contains "python.7z") -and ($kitFiles -contains "python312.zip") -and ($kitFiles -contains "python312._pth") -and ($kitFiles -contains "MinGit.zip")
}

$d3Detail = if ($kitOk) { "assets: $assets ($($kitFiles -join ', '))" } else { "missing 7za.exe, python.7z, python312.zip, python312._pth, or MinGit zip" }

$hard = @(
    @{ id = "D1"; name = "Qoder CN"; status = $(if ($qoder.ok) { "pass" } else { "fail" }); detail = $qoder.detail; remediation = "Install Qoder CN client" },
    @{ id = "D2"; name = "PowerShell"; status = $(if ($psOk) { "pass" } else { "fail" }); detail = $psVer.ToString(); remediation = "Requires PowerShell 5.1+" },
    @{ id = "D3"; name = "skill-kit bundle"; status = $(if ($kitOk) { "pass" } else { "fail" }); detail = $d3Detail; remediation = "See assets/skill-kit/README.md" }
)

$hardPass = (($hard | Where-Object { $_.status -eq "pass" }).Count -eq $hard.Count)
$stamp = Get-Date -Format "yyyy-MM-ddTHH:mm:ss"
$gate = if ($hardPass) { "pass" } else { "fail" }
$message = if ($hardPass) { "Hard dependencies OK (zero-preinstall mode)" } else { "Hard dependencies missing" }

$report = [ordered]@{
    os = $os
    timestamp = $stamp
    hard_dependencies = $hard
    hard_gate = $gate
    message = $message
}

$mdLines = @(
    "# Qoder Skills dependency report",
    "",
    "> timestamp: $stamp",
    "> os: $os",
    "> gate: $gate",
    "",
    "| ID | name | status | detail |",
    "|----|------|--------|--------|"
)
foreach ($h in $hard) {
    $mdLines += "| $($h.id) | $($h.name) | $($h.status) | $($h.detail) |"
}
$mdText = $mdLines -join "`n"

$json = $report | ConvertTo-Json -Depth 6

if ($ReportAuto -or $ReportPath) {
    $reportDir = Join-Path $env:USERPROFILE ".qoder-cn\reports"
    New-Item -ItemType Directory -Path $reportDir -Force | Out-Null
    $prefix = if ($hardPass) { "dependency-pass" } else { "dependency-fail" }
    $path = if ($ReportPath) { $ReportPath } else { Join-Path $reportDir "$prefix-$(Get-Date -Format 'yyyyMMdd-HHmmss').md" }
    Set-Content -Path $path -Value $mdText -Encoding UTF8
}

Write-Output $json
if ($hardPass) { exit 0 } else { exit 1 }
