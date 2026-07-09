# 将 GitLab Access Token 写入当前用户环境变量（持久化，供后续 GitLab 操作使用）
param(
    [Parameter(Mandatory = $true)]
    [string]$Token
)

$ErrorActionPreference = 'Stop'
[System.Environment]::SetEnvironmentVariable('GITLAB_TOKEN', $Token, 'User')

# 同步到当前会话，便于立即使用
$env:GITLAB_TOKEN = $Token

$val = [System.Environment]::GetEnvironmentVariable('GITLAB_TOKEN', 'User')
if ([string]::IsNullOrWhiteSpace($val)) {
    Write-Error 'GITLAB_TOKEN 写入用户环境变量失败'
    exit 1
}

Write-Host 'GITLAB_TOKEN 已写入用户环境变量。新开的终端将自动生效。'
