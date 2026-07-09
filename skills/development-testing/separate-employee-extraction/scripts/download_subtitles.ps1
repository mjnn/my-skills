# Download subtitles using vendored yt-dlp module (no system python / no bash)
param(
    [Parameter(Mandatory = $true)]
    [string]$Url,
    [string]$OutputDir = "references/sources/subtitles"
)

$ErrorActionPreference = "Stop"
$skillRoot = Split-Path $PSScriptRoot -Parent
$check = Join-Path $env:USERPROFILE ".qoder-cn\tools\skill-kit\scripts\check_skill_kit_ready.ps1"
if (-not (Test-Path $check)) {
    $check = Join-Path $env:USERPROFILE ".qoder-cn\skills\skill-kit\scripts\check_skill_kit_ready.ps1"
}
& powershell -ExecutionPolicy Bypass -File $check -SkillDir $skillRoot | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Error "skill-kit not ready (exit $LASTEXITCODE). Run skill-env-setup first."
    exit $LASTEXITCODE
}

. (Join-Path $env:USERPROFILE ".qoder-cn\tools\skill-kit\scripts\resolve_tools.ps1")
$py = Get-QoderPython
$init = Join-Path $env:USERPROFILE ".qoder-cn\tools\skill-kit\scripts\init_skill_python.ps1"
if (Test-Path $init) {
    & powershell -ExecutionPolicy Bypass -File $init -SkillDir $skillRoot | Out-Null
}

New-Item -ItemType Directory -Path $OutputDir -Force | Out-Null
& $py -m yt_dlp --write-subs --write-auto-subs --sub-langs "zh,en" --skip-download -o (Join-Path $OutputDir "%(id)s") $Url
exit $LASTEXITCODE
