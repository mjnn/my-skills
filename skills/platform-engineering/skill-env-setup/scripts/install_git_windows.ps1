# Deploy bundled MinGit portable zip to user profile (no admin required)
param(
    [string]$SkillRoot = (Split-Path $PSScriptRoot -Parent)
)

$ErrorActionPreference = 'Stop'

$gitDir = Join-Path $SkillRoot 'assets\git'
$installRoot = Join-Path $env:USERPROFILE '.qoder-cn\tools\git'
$gitCmd = Join-Path $installRoot 'cmd\git.exe'
$pathEntry = Join-Path $installRoot 'cmd'

function Add-GitToUserPath {
    param([string]$Entry)
    $userPath = [Environment]::GetEnvironmentVariable('Path', 'User')
    $parts = @()
    if ($userPath) {
        $parts = $userPath -split ';' | Where-Object { $_ -and ($_ -ne $Entry) }
    }
    $newPath = (@($Entry) + $parts) -join ';'
    [Environment]::SetEnvironmentVariable('Path', $newPath, 'User')
    $env:Path = "$Entry;$env:Path"
}

if (Test-Path $gitCmd) {
    Write-Host "Portable Git already installed: $gitCmd"
    & $gitCmd --version
    Add-GitToUserPath -Entry $pathEntry
    Write-Host 'User PATH updated for portable Git.'
    exit 0
}

$archive = Get-ChildItem -Path $gitDir -Filter 'MinGit-*-64-bit.zip' -ErrorAction SilentlyContinue | Select-Object -First 1
if (-not $archive) {
    Write-Error "MinGit zip not found in $gitDir"
    exit 1
}

Write-Host "Using bundled archive: $($archive.FullName)"
New-Item -ItemType Directory -Path $installRoot -Force | Out-Null
Expand-Archive -Path $archive.FullName -DestinationPath $installRoot -Force

if (-not (Test-Path $gitCmd)) {
    Write-Error "git.exe not found at $gitCmd after extraction"
    exit 1
}

Add-GitToUserPath -Entry $pathEntry
& $gitCmd --version
Write-Host "Portable Git installed to $installRoot (no admin required)."
