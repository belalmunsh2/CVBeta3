Write-Host "Starting to pull latest changes from origin/master..." -ForegroundColor Green

# Git pull command to fetch and merge changes from remote 'origin' branch 'master'
git pull origin master

Write-Host "Git pull completed." -ForegroundColor Green
Write-Host "--- Git Status after Pull ---" -ForegroundColor Cyan
git status

Write-Host "Finished pull_from_github.ps1 script." -ForegroundColor Green
