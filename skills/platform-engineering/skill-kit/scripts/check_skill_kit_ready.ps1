# Check skill-kit installation and optional per-skill vendor link status.
param(
    [string]$SkillDir = "",
    [switch]$JsonOnly
)

$ErrorActionPreference = "Stop"
$kitRoot = Join-Path $env:USERPROFILE ".qoder-cn\tools\skill-kit"
$pythonExe = Join-Path $kitRoot "python\python.exe"
$checkScript = Join-Path $kitRoot "scripts\check_skill_kit_ready.ps1"

# Allow running from skill package before install copies scripts to kitRoot
if (-not (Test-Path $checkScript)) {
    $candidates = @(
        (Join-Path $env:USERPROFILE ".qoder-cn\skills\skill-kit\scripts\check_skill_kit_ready.ps1"),
        (Join-Path $PSScriptRoot "check_skill_kit_ready.ps1")
    )
    foreach ($c in $candidates) {
        if (Test-Path $c) { $checkScript = $c; break }
    }
}

function Write-Result {
    param([hashtable]$R)
    if ($JsonOnly) {
        $R | ConvertTo-Json -Depth 4
    } else {
        Write-Host ($R | ConvertTo-Json -Depth 4)
    }
}

if (-not (Test-Path $pythonExe)) {
    $r = @{
        ok = $false
        exit_code = 1
        reason = "skill-kit not installed"
        remediation = "Run skill-env-setup (configure Qoder Skills environment) to complete node 4.0"
        qoder_python = $null
    }
    Write-Result $r
    exit 1
}

try {
    $ver = & $pythonExe -c "import sys; print(sys.version.split()[0])" 2>&1
    if ($LASTEXITCODE -ne 0) { throw "python failed: $ver" }
} catch {
    $r = @{
        ok = $false
        exit_code = 1
        reason = "QODER_PYTHON not functional"
        detail = "$_"
        remediation = "Re-run skill-env-setup or install_skill_kit.ps1"
    }
    Write-Result $r
    exit 1
}

$env:QODER_PYTHON = $pythonExe
$env:QODER_TOOLS_ROOT = $kitRoot
$gitExe = Join-Path $kitRoot "git\cmd\git.exe"
if (Test-Path $gitExe) { $env:QODER_GIT = $gitExe }

$vendorOk = $true
$vendorDetail = "no vendor dir"
if ($SkillDir -and (Test-Path $SkillDir)) {
    $vendor = Join-Path $SkillDir "vendor\python-packages"
    if (Test-Path $vendor) {
        $hasPkgs = @(Get-ChildItem -Path $vendor -Directory -ErrorAction SilentlyContinue).Count -gt 0
        if ($hasPkgs) {
            $skillName = Split-Path $SkillDir -Leaf
            $safe = $skillName -replace '[^a-zA-Z0-9_-]', '-'
            $pth = Join-Path $kitRoot "python\Lib\site-packages\qoder-skill-$safe.pth"
            $vendorOk = Test-Path $pth
            $vendorDetail = if ($vendorOk) { "vendor linked via $pth" } else { "vendor not linked; run init_skill_python.ps1" }
        }
    }
}

if (-not $vendorOk) {
    $r = @{
        ok = $false
        exit_code = 2
        reason = "skill vendor packages not linked"
        detail = $vendorDetail
        remediation = "Run init_skill_python.ps1 -SkillDir `"$SkillDir`" or re-run skill-env-setup node 4.6"
        qoder_python = $pythonExe
    }
    Write-Result $r
    exit 2
}

$r = @{
    ok = $true
    exit_code = 0
    reason = "skill-kit ready"
    qoder_python = $pythonExe
    qoder_git = $(if (Test-Path $gitExe) { $gitExe } else { $null })
    vendor = $vendorDetail
}
Write-Result $r
exit 0
