# Install portable skill-kit to %USERPROFILE%\.qoder-cn\tools\skill-kit
param(
    [string]$AssetsRoot = "",
    [string]$InstallRoot = (Join-Path $env:USERPROFILE ".qoder-cn\tools\skill-kit")
)

$ErrorActionPreference = "Stop"

function Find-AssetsRoot {
    param([string]$Hint)
    if ($Hint -and (Test-Path (Join-Path $Hint "7za.exe"))) { return $Hint }

    $candidates = @(
        (Join-Path $PSScriptRoot "..\assets"),
        (Join-Path $env:USERPROFILE ".qoder-cn\skills\skill-kit\assets"),
        (Join-Path $env:USERPROFILE ".qoder-cn\skills\skill-env-setup\assets\skill-kit")
    )
    foreach ($c in $candidates) {
        if (Test-Path (Join-Path $c "7za.exe")) { return $c }
    }
    return $null
}

$src = Find-AssetsRoot -Hint $AssetsRoot
if (-not $src) {
    Write-Error "skill-kit assets not found (need 7za.exe under assets/). See references/maintainer-bundle.md"
    exit 1
}

New-Item -ItemType Directory -Path $InstallRoot -Force | Out-Null
New-Item -ItemType Directory -Path (Join-Path $InstallRoot "state") -Force | Out-Null
New-Item -ItemType Directory -Path (Join-Path $InstallRoot "scripts") -Force | Out-Null

# Copy helper scripts to install root
$scriptNames = @(
    "resolve_tools.ps1",
    "init_skill_python.ps1",
    "run_python.ps1",
    "link_python_packages.py",
    "check_skill_kit_ready.ps1",
    "run_skill_script.ps1"
)
foreach ($name in $scriptNames) {
    $from = Join-Path $PSScriptRoot $name
    if (Test-Path $from) {
        Copy-Item -Path $from -Destination (Join-Path $InstallRoot "scripts\$name") -Force
    }
}

# 7za
$sevenZa = Join-Path $InstallRoot "7za.exe"
if (-not (Test-Path $sevenZa)) {
    Copy-Item -Path (Join-Path $src "7za.exe") -Destination $sevenZa -Force
}

# Python from python.7z
$pythonExe = Join-Path $InstallRoot "python\python.exe"
$pythonArchive = Join-Path $src "python.7z"
if (-not (Test-Path $pythonExe)) {
    if (-not (Test-Path $pythonArchive)) {
        Write-Error "python.7z not found in $src"
        exit 1
    }
    Write-Host "Extracting python.7z ..."
    & $sevenZa x $pythonArchive ("-o{0}" -f $InstallRoot) -y | Out-Null
    if (-not (Test-Path $pythonExe)) {
        Write-Error "python.exe not found after extracting python.7z"
        exit 1
    }
}

# Stdlib zip + ._pth (reference python.7z may not include python312.zip)
$pythonDir = Join-Path $InstallRoot "python"
$stdlibZip = Join-Path $src "python312.zip"
if (Test-Path $stdlibZip) {
    Copy-Item -Path $stdlibZip -Destination (Join-Path $pythonDir "python312.zip") -Force
} else {
    Write-Warning "python312.zip not found in assets; vendor imports may fail without stdlib zip"
}
$stdlibPth = Join-Path $src "python312._pth"
$pthDest = Join-Path $pythonDir "python312._pth"
if (Test-Path $stdlibPth) {
    Copy-Item -Path $stdlibPth -Destination $pthDest -Force
} elseif (-not (Test-Path $pthDest)) {
    @("python312.zip", ".", "DLLs", "Lib/site-packages", "import site") | Set-Content -Path $pthDest -Encoding ASCII
}

# MinGit
$gitExe = Join-Path $InstallRoot "git\cmd\git.exe"
if (-not (Test-Path $gitExe)) {
    $gitAssetDir = Join-Path $src "git"
    if (-not (Test-Path $gitAssetDir)) {
        $gitAssetDir = Join-Path (Split-Path $src -Parent) "git"
    }
    $mingit = Get-ChildItem -Path $gitAssetDir -Filter "MinGit-*-64-bit.zip" -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($mingit) {
        $gitDest = Join-Path $InstallRoot "git"
        New-Item -ItemType Directory -Path $gitDest -Force | Out-Null
        Expand-Archive -Path $mingit.FullName -DestinationPath $gitDest -Force
    }
}

# User PATH for git cmd (python invoked via QODER_PYTHON, not PATH)
$gitCmdDir = Join-Path $InstallRoot "git\cmd"
if (Test-Path $gitCmdDir) {
    $userPath = [Environment]::GetEnvironmentVariable("Path", "User")
    $parts = @()
    if ($userPath) { $parts = $userPath -split ";" | Where-Object { $_ -and ($_ -ne $gitCmdDir) } }
    $newPath = (@($gitCmdDir) + $parts) -join ";"
    [Environment]::SetEnvironmentVariable("Path", $newPath, "User")
    $env:Path = "$gitCmdDir;$env:Path"
}

[Environment]::SetEnvironmentVariable("QODER_TOOLS_ROOT", $InstallRoot, "User")
[Environment]::SetEnvironmentVariable("QODER_PYTHON", $pythonExe, "User")
if (Test-Path $gitExe) {
    [Environment]::SetEnvironmentVariable("QODER_GIT", $gitExe, "User")
}
$env:QODER_TOOLS_ROOT = $InstallRoot
$env:QODER_PYTHON = $pythonExe
if (Test-Path $gitExe) { $env:QODER_GIT = $gitExe }

Write-Host "skill-kit installed: $InstallRoot"
& $pythonExe -c "import sys; print(sys.version)"
if (Test-Path $gitExe) { & $gitExe --version }
