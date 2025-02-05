# Basic push script from CVBeta2
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

# Validate PAT format
if (-not ($patText -match '^ghp_[a-zA-Z0-9]{36}$')) {
    Write-Error "Invalid PAT format"
    exit 1
}

# Validate PAT before operations
try {
    $testAuth = git ls-remote $repoUrl -q
    if (-not $?) {
        throw "Authentication failed"
    }
} catch {
    Write-Error "Invalid PAT or repository access"
    exit 1
}

# Test GitHub connection
$response = Invoke-WebRequest -Uri "https://api.github.com" -Headers @{"Authorization" = "token $patText"}
if ($response.StatusCode -ne 200) {
    Write-Error "Invalid PAT or permissions"
    exit 1
}

git add .
git commit -m "Auto-commit: $(Get-Date -Format 'yyyyMMdd_HHmmss')"
git push https://github.com/belalmunsh/CVBeta3 master
