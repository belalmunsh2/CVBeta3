# Simplified Git push automation
$repoPath = "C:\Users\ASUS\CascadeProjects\CVBeta3"
$configPath = "$env:USERPROFILE\.cvbeta3_gitconfig"
$repoUrl = "https://github.com/belalmunsh/CVBeta3"

Set-Location $repoPath

if (-not (Test-Path .git)) {
    git init
}

# Secure PAT handling
if (-not (Test-Path $configPath)) {
    $pat = Read-Host "Enter GitHub PAT" -AsSecureString
    $patText = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($pat))
    $patText | ConvertTo-SecureString -AsPlainText -Force | ConvertFrom-SecureString | Set-Content $configPath
}

$securePat = Get-Content $configPath | ConvertTo-SecureString
$credential = New-Object System.Management.Automation.PSCredential("PAT", $securePat)
$patText = $credential.GetNetworkCredential().Password

$authUrl = $repoUrl.Replace("https://", "https://${patText}@")

if (-not (git remote show origin)) {
    git remote add origin $authUrl
} else {
    git remote set-url origin $authUrl
}

git add .
git commit -m "Auto-commit: $(Get-Date -Format 'yyyyMMdd_HHmmss')"

git push -u origin main --force
