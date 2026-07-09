# Main entry: skill-kit check, skill scan, vendor link status, optional Hub compare.
param(
    [switch]$CompareHub,
    [switch]$JsonOnly,
    [switch]$KitOnly
)

$ErrorActionPreference = "Stop"
$kitRoot = Join-Path $env:USERPROFILE ".qoder-cn\tools\skill-kit"
$skillsDir = Join-Path $env:USERPROFILE ".qoder-cn\skills"
$checkKit = Join-Path $kitRoot "scripts\check_skill_kit_ready.ps1"
$resolve = Join-Path $kitRoot "scripts\resolve_tools.ps1"
$scanPy = Join-Path $PSScriptRoot "scan_local_runtime.py"

function Write-DiagResult {
    param([object]$Payload, [int]$ExitCode)
    if ($JsonOnly) {
        $Payload | ConvertTo-Json -Depth 8
    } else {
        Write-Host ($Payload | ConvertTo-Json -Depth 8)
    }
    exit $ExitCode
}

# Fallback kit check script from installed skill-kit skill package
if (-not (Test-Path $checkKit)) {
    $fallback = Join-Path $env:USERPROFILE ".qoder-cn\skills\skill-kit\scripts\check_skill_kit_ready.ps1"
    if (Test-Path $fallback) { $checkKit = $fallback }
}

$pythonExe = Join-Path $kitRoot "python\python.exe"
$kitOk = Test-Path $pythonExe

if (-not $kitOk) {
    Write-DiagResult @{
        ok = $false
        exit_code = 1
        phase = "kit_check"
        reason = "skill-kit not installed"
        remediation = "Run skill-env-setup (configure Qoder Skills environment); do not use winget or system python"
        skills_dir = $skillsDir
        kit_root = $kitRoot
    } 1
}

try {
    $ver = & $pythonExe -c "import sys; print(sys.version.split()[0])" 2>&1
    if ($LASTEXITCODE -ne 0) { throw "python failed: $ver" }
} catch {
    Write-DiagResult @{
        ok = $false
        exit_code = 1
        phase = "kit_check"
        reason = "QODER_PYTHON not functional"
        detail = "$_"
        remediation = "Re-run skill-env-setup node 4.0 (install_skill_kit.ps1)"
    } 1
}

$env:QODER_PYTHON = $pythonExe
$env:QODER_TOOLS_ROOT = $kitRoot
$gitExe = Join-Path $kitRoot "git\cmd\git.exe"
if (Test-Path $gitExe) { $env:QODER_GIT = $gitExe }

if ($KitOnly) {
    Write-DiagResult @{
        ok = $true
        exit_code = 0
        phase = "kit_check"
        reason = "skill-kit ready"
        qoder_python = $pythonExe
        qoder_git = $(if (Test-Path $gitExe) { $gitExe } else { $null })
    } 0
}

if (-not (Test-Path $scanPy)) {
    Write-DiagResult @{
        ok = $false
        exit_code = 1
        phase = "scan"
        reason = "scan_local_runtime.py not found"
        detail = $scanPy
    } 1
}

$args = @()
if ($CompareHub) { $args += "--compare-hub" }

$jsonText = & $pythonExe $scanPy @args 2>&1 | Out-String
try {
    $scan = $jsonText | ConvertFrom-Json
} catch {
    Write-DiagResult @{
        ok = $false
        exit_code = 1
        phase = "scan"
        reason = "scan script failed"
        raw = $jsonText
    } 1
}

$exitCode = if ($scan.ok) { 0 } else { 2 }
$payload = @{
    ok = [bool]$scan.ok
    exit_code = $exitCode
    phase = "full_diagnose"
    kit = @{
        ready = $true
        qoder_python = $pythonExe
        qoder_git = $(if (Test-Path $gitExe) { $gitExe } else { $null })
    }
    scan = $scan
}

if (-not (Test-Path $skillsDir)) {
    $payload.ok = $false
    $payload.exit_code = 2
    $payload.issues = @("skills_dir_missing")
    $payload.remediation = "Run skill-env-setup to create skills dir and install init bundle"
}

Write-DiagResult $payload $payload.exit_code
