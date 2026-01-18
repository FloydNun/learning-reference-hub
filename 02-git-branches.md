# Git Branches - Working on Different Features

## What's a Branch?
Think of branches like copies of your project where you can experiment without breaking the main version.

## Branch Commands

```bash
# SEE ALL BRANCHES
git branch                    # List branches (* shows current)
git branch -a                 # List all branches (including remote)

# CREATE A NEW BRANCH
git branch feature-name       # Create branch
git checkout feature-name     # Switch to that branch

# SHORTCUT: Create and switch in one command
git checkout -b feature-name

# SWITCH BETWEEN BRANCHES
git checkout main             # Go back to main branch
git checkout feature-name     # Go to feature branch

# DELETE A BRANCH (after you're done with it)
git branch -d feature-name    # Safe delete (only if merged)
git branch -D feature-name    # Force delete
```

## Typical Workflow

```bash
# 1. Start from main branch
git checkout main

# 2. Get latest changes
git pull

# 3. Create new branch for your work
git checkout -b add-new-feature

# 4. Make your changes, then... 
git add .
git commit -m "Added new feature"

# 5. Push your branch to GitHub
git push -u origin add-new-feature

# 6. Go to GitHub and create a Pull Request
# (We'll cover this in the GitHub sheet)

# 7. After merge, clean up
git checkout main
git pull
git branch -d add-new-feature
```

## Quick Reference
| Command | What It Does |
|---------|--------------|
| `git branch` | Show all branches |
| `git checkout -b name` | Create and switch to new branch |
| `git checkout main` | Switch back to main branch |
| `git merge branch-name` | Combine branch into current branch |
| `git push -u origin branch-name` | Push new branch to GitHub |

## 🎯 Mental Model
```
main branch:       A---B---C---F---G
                       \       /
feature branch:         D-----E
```
- Create branch at B
- Work on D and E
- Merge back at F

---
**Notes Section**:
- 
- 
```