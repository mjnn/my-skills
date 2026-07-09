# Fix kit gaps (guide only), re-init vendors, optional Hub zip upgrade for named skills.
param(
    [switch]$RelinkAll,
    [string[]]$RelinkSkills = @(),
    [string[]]$UpgradeSkills = @(),
    [switch]$JsonOnly
)

$ErrorActionPreference = "Stop"
$kitRoot = Join-Path $env:USERPROFILE ".qoder-cn\tools\skill-kit"
$skillsDir = Join-Path $env:USERPROFILE ".qoder-cn\skills"
$initOne = Join-Path $kitRoot "scripts\init_skill_python.ps1"
$initAll = Join-Path $env:USERPROFILE ".qoder-cn\skills\skill-env-setup\scripts\init_all_skill_runtimes.ps1"
if (-not (Test-Path $initAll)) {
    $initAll = Join-Path $PSScriptRoot "..\..\skill-env-setup\scripts\init_all_skill_runtimes.ps1"
}
$pythonExe = Join-Path $kitRoot "python\python.exe"
$upgradePy = Join-Path $PSScriptRoot "upgrade_skill_from_hub.py"

function Write-RepairResult {
    param([hashtable]$R, [int]$Code)
    if ($JsonOnly) { $R | ConvertTo-Json -Depth 6 } else { Write-Host ($R | ConvertTo-Json -Depth 6) }
    exit $Code
}

if (-not (Test-Path $pythonExe)) {
    Write-RepairResult @{
        ok = $false
        exit_code = 1
        reason = "skill-kit not installed"
        remediation = "Run skill-env-setup; repair cannot install kit without full onboarding"
    } 1
}

$env:QODER_PYTHON = $pythonExe
$env:QODER_TOOLS_ROOT = $kitRoot
$actions = @()
$errors = @()

if ($RelinkAll) {
    if (-not (Test-Path $initAll)) {
        $errors += "init_all_skill_runtimes.ps1 not found"
    } else {
        & powershell -ExecutionPolicy Bypass -File $initAll -SkillsDir $skillsDir
        if ($LASTEXITCODE -ne 0) { $errors += "init_all_skill_runtimes failed" }
        else { $actions += "relink_all_vendors" }
    }
} elseif ($RelinkSkills.Count -gt 0) {
    if (-not (Test-Path $initOne)) {
        $errors += "init_skill_python.ps1 not found"
    } else {
        foreach ($name in $RelinkSkills) {
            $skillDir = Join-Path $skillsDir $name
            if (-not (Test-Path $skillDir)) {
                $errors += "skill not found: $name"
                continue
            }
            & powershell -ExecutionPolicy Bypass -File $initOne -SkillDir $skillDir
            if ($LASTEXITCODE -ne 0) { $errors += "init failed: $name" }
            else { $actions += "relink_vendor:$name" }
        }
    }
}

if ($UpgradeSkills.Count -gt 0) {
    if (-not (Test-Path $upgradePy)) {
        $errors += "upgrade_skill_from_hub.py not found"
    } else {
        foreach ($name in $UpgradeSkills) {
            & $pythonExe $upgradePy --skill $name 2>&1 | Out-Null
            if ($LASTEXITCODE -ne 0) { $errors += "hub upgrade failed: $name" }
            else { $actions += "hub_upgrade:$name" }
        }
    }
}

if ($actions.Count -eq 0 -and $errors.Count -eq 0) {
    Write-RepairResult @{
        ok = $false
        exit_code = 1
        reason = "no repair action specified"
        hint = "Use -RelinkAll, -RelinkSkills, or -UpgradeSkills"
    } 1
}

$ok = $errors.Count -eq 0
Write-RepairResult @{
    ok = $ok
    exit_code = $(if ($ok) { 0 } else { 2 })
    actions = $actions
    errors = $errors
} $(if ($ok) { 0 } else { 2 })
