<#
Sets repository secrets from a local `.env` file using GitHub CLI (`gh`).
Requires: `gh` installed and authenticated (gh auth login), and you run this from the repo root.

Usage: .\scripts\set-github-secrets.ps1 -EnvFile .\.env
#>

param(
    [string]$EnvFile = ".\.env",
    [string]$Repo = "$env:GITHUB_REPOSITORY"
)

if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    Write-Error "gh CLI is not installed or not in PATH. Please install gh from https://cli.github.com/."
    exit 1
}

if (-not (Test-Path $EnvFile)) {
    Write-Error "$EnvFile not found. Copy .env.example to .env and fill values first."
    exit 1
}

Get-Content $EnvFile | ForEach-Object {
    if ($_ -match "^\s*([^#=]+)=(.*)$") {
        $k = $matches[1].Trim()
        $v = $matches[2].Trim().Trim('"')
        if ($v -ne "") {
            Write-Host "Setting secret: $k"
            # gh secret set reads value from stdin
            $v | gh secret set $k --repo $Repo
        }
    }
}

Write-Host "Done. Verify secrets at https://github.com/$Repo/settings/secrets/actions"
