# Basic CVBeta2-style push script
git add .
git commit -m "Auto-commit: $(Get-Date -Format 'yyyyMMdd_HHmmss')"
git push https://github.com/belalmunsh/CVBeta3 master
