# 🛸 COUNTERBALANCE - Quick GitHub Push Script (Windows)

Write-Host "🛸 COUNTERBALANCE - GitHub Push" -ForegroundColor Cyan
Write-Host "==============================" -ForegroundColor Cyan
Write-Host ""

# Check if git is initialized
if (-Not (Test-Path . git)) {
    Write-Host "Initializing git repository..." -ForegroundColor Yellow
    git init
}

# Add all files
Write-Host "Adding files..." -ForegroundColor Yellow
git add .

# Show status
Write-Host ""
Write-Host "Files to be committed:" -ForegroundColor Yellow
git status --short

# Prompt for commit message
Write-Host ""
$commit_msg = Read-Host "Commit message (or press Enter for default)"

if ([string]::IsNullOrWhiteSpace($commit_msg)) {
    $commit_msg = "🛸 Update COUNTERBALANCE system"
}

# Commit
Write-Host ""
Write-Host "Committing..." -ForegroundColor Yellow
git commit -m $commit_msg

# Check if remote exists
$remote = git remote

if ($remote -contains "origin") {
    Write-Host ""
    Write-Host "Pushing to GitHub..." -ForegroundColor Yellow
    git push
} else {
    Write-Host ""
    Write-Host "⚠️  No remote 'origin' found" -ForegroundColor Red
    Write-Host "Set up remote with:" -ForegroundColor Yellow
    Write-Host "  git remote add origin https://github.com/FloydNun/counterbalance.git"
    Write-Host "  git push -u origin main"
}

Write-Host ""
Write-Host "✅ Done!" -ForegroundColor Green