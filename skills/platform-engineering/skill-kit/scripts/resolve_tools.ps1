# Resolve portable tool paths into env vars (dot-source this file)
$InstallRoot = $env:QODER_TOOLS_ROOT
if (-not $InstallRoot) {
    $InstallRoot = Join-Path $env:USERPROFILE ".qoder-cn\tools\skill-kit"
}

$pythonExe = Join-Path $InstallRoot "python\python.exe"
$gitExe = Join-Path $InstallRoot "git\cmd\git.exe"
$sevenZa = Join-Path $InstallRoot "7za.exe"

if (Test-Path $pythonExe) { $env:QODER_PYTHON = $pythonExe }
if (Test-Path $gitExe) { $env:QODER_GIT = $gitExe }
if (Test-Path $sevenZa) { $env:QODER_SEVENZIP = $sevenZa }
$env:QODER_TOOLS_ROOT = $InstallRoot

function Get-QoderPython {
    if (-not (Test-Path $pythonExe)) {
        throw "Portable Python not installed. Run install_skill_kit.ps1 first."
    }
    return $pythonExe
}

function Get-QoderGit {
    if (-not (Test-Path $gitExe)) {
        throw "Portable Git not installed. Run install_skill_kit.ps1 first."
    }
    return $gitExe
}
