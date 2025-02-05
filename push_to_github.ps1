# Simplified Git push automation
$repoPath = "C:\Users\ASUS\CascadeProjects\CVBeta3"
$configPath = "$env:USERPROFILE\.cvbeta3_gitconfig"
$repoUrl = "https://github.com/belalmunsh/CVBeta3"

Set-Location $repoPath

if (-not (Test-Path .git)) {
    git init
}

# Secure PAT handling
$pat = Read-Host "Enter GitHub PAT" -AsSecureString
$patText = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($pat))

$repoUrl = "https://${patText}@github.com/belalmunsh/CVBeta3"

if (-not (git remote show origin)) {
    git remote add origin $repoUrl
} else {
    git remote set-url origin $repoUrl
}

if (-not (git rev-parse --verify master)) {
    git checkout -b master
}

git config --global core.autocrlf true
git config --global core.safecrlf false
git config --global credential.helper "store"

git add .
git commit -m "Auto-commit: $(Get-Date -Format 'yyyyMMdd_HHmmss')"

git push $repoUrl master --force
