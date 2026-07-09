# Initialize vendor/python-packages for all skills under ~/.qoder-cn/skills
param(
    [string]$SkillsDir = (Join-Path $env:USERPROFILE ".qoder-cn\skills")
)

$ErrorActionPreference = "Stop"
$kitRoot = Join-Path $env:USERPROFILE ".qoder-cn\tools\skill-kit"
$init = Join-Path $kitRoot "scripts\init_skill_python.ps1"
if (-not (Test-Path $init)) {
    $init = Join-Path $PSScriptRoot "..\..\skill-kit\scripts\init_skill_python.ps1"
}
if (-not (Test-Path $init)) {
    Write-Error "init_skill_python.ps1 not found"
    exit 1
}

if (-not (Test-Path $SkillsDir)) {
    Write-Host "Skills dir not found: $SkillsDir"
    exit 0
}

$results = @()
Get-ChildItem -Path $SkillsDir -Directory | ForEach-Object {
    $skillMd = Join-Path $_.FullName "SKILL.md"
    if (-not (Test-Path $skillMd)) { return }
    $vendor = Join-Path $_.FullName "vendor\python-packages"
    if (-not (Test-Path $vendor)) { return }
    Write-Host "Init python vendor: $($_.Name)"
    & powershell -ExecutionPolicy Bypass -File $init -SkillDir $_.FullName
    $results += $_.Name
}

Write-Host "Initialized $($results.Count) skill(s) with vendor packages."
exit 0
