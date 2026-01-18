# Git Troubleshooting - When Things Go Wrong

## 🆘 Most Common Problems & Solutions

### Problem 1: "I made a mistake in my last commit message"
```bash
# Change the last commit message
git commit --amend -m "New, corrected message"

# If already pushed, you'll need to force push (be careful!)
git push --force
```

### Problem 2: "I want to undo changes before committing"
```bash
# Undo changes to one file
git checkout -- filename.txt

# Undo ALL changes (go back to last commit)
git reset --hard HEAD
```

### Problem 3: "I committed but want to undo it"
```bash
# Undo last commit but keep the changes
git reset --soft HEAD~1

# Undo last commit and discard changes
git reset --hard HEAD~1
```

### Problem 4: "My push was rejected"
```bash
# Usually means remote has changes you don't have
# Solution: Pull first, then push
git pull
# Fix any conflicts if they appear
git push
```

### Problem 5: "Merge conflict - HELP!"
```bash
# 1. Don't panic! Git stops and asks you to choose
# 2. Open the conflicted file(s) - git status shows them
# 3. Look for these markers:
<<<<<<< HEAD
Your changes
=======
Their changes
>>>>>>> branch-name

# 4. Edit the file to keep what you want
# 5. Remove the <<<, ===, >>> markers
# 6. Save the file
# 7. Complete the merge: 
git add .
git commit -m "Resolved merge conflict"
git push
```

### Problem 6: "I'm on the wrong branch!"
```bash
# Haven't committed yet?  Save your work and switch: 
git stash                    # Save changes temporarily
git checkout correct-branch  # Switch to right branch
git stash pop               # Bring your changes back
```

### Problem 7: "How do I see what changed?"
```bash
# See changes not yet staged
git diff

# See changes staged for commit
git diff --staged

# See commit history
git log

# See history with one line per commit
git log --oneline

# See changes in last commit
git show
```

## Emergency Commands

```bash
# See what happened (reflog = safety net)
git reflog

# Go back to a previous state
git reset --hard HEAD@{2}  # Go back 2 steps in reflog

# Abort a merge that's going badly
git merge --abort

# Abort a rebase
git rebase --abort
```

## Quick Reference
| Problem | Command |
|---------|---------|
| Undo unstaged changes | `git checkout -- file.txt` |
| Undo last commit | `git reset --soft HEAD~1` |
| See what I changed | `git diff` |
| See commit history | `git log --oneline` |
| Abort merge | `git merge --abort` |

---
**Notes Section** (Write problems you encounter):
- 
- 
```