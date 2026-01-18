# Git Basics - Your First Commands

## Setup (Do Once)
```bash
# Set your name (this appears in your commits)
git config --global user.name "Your Name"

# Set your email (use your GitHub email)
git config --global user.email "your.email@example.com"

# Check your settings
git config --list
```

## Starting a Project

### Option A: Clone an existing repository
```bash
# Copy a repository from GitHub to your computer
git clone https://github.com/username/repository-name.git

# Move into the repository folder
cd repository-name
```

### Option B: Create a new repository
```bash
# Create a new folder
mkdir my-project
cd my-project

# Initialize Git in this folder
git init
```

## Daily Workflow - The Big 4 Commands

```bash
# 1. CHECK STATUS - See what's changed
git status

# 2. ADD FILES - Stage files for commit
git add filename.txt          # Add one file
git add .                      # Add all changed files

# 3. COMMIT - Save your changes with a message
git commit -m "Describe what you changed"

# 4. PUSH - Send your changes to GitHub
git push
```

## Quick Reference
| Command | What It Does |
|---------|--------------|
| `git status` | Shows what files have changed |
| `git add .` | Prepares all changes to be saved |
| `git commit -m "message"` | Saves changes with a description |
| `git push` | Uploads your changes to GitHub |
| `git pull` | Downloads latest changes from GitHub |

## 💡 Practice Exercise
1. Make a change to any file
2. Run `git status` - see your change
3. Run `git add .` - stage the change
4. Run `git commit -m "my first commit"` - save it
5. Run `git push` - send to GitHub

---
**Notes Section** (Write your own discoveries here):
- 
- 
- 
```