# Command Line Basics - Terminal Navigation

## Essential Commands (Works on Mac/Linux/Windows Git Bash)

### Navigation
```bash
# WHERE AM I?
pwd                    # Print working directory (shows current location)

# LIST FILES
ls                     # List files in current folder
ls -la                 # List all files with details (including hidden)
ls -lh                 # List with human-readable file sizes

# CHANGE DIRECTORY
cd folder-name         # Go into a folder
cd ..                  # Go up one level
cd ~                   # Go to home directory
cd /                   # Go to root directory
cd -                   # Go back to previous directory
```

### File Operations
```bash
# CREATE
touch filename.txt     # Create empty file
mkdir folder-name      # Create directory
mkdir -p path/to/folder # Create nested directories

# VIEW FILES
cat filename.txt       # Show entire file
less filename.txt      # View file (q to quit)
head filename.txt      # Show first 10 lines
tail filename.txt      # Show last 10 lines

# COPY & MOVE
cp file. txt newfile.txt        # Copy file
cp -r folder/ newfolder/       # Copy folder
mv file.txt newfolder/         # Move file
mv oldname.txt newname.txt     # Rename file

# DELETE (BE CAREFUL!)
rm filename.txt        # Delete file
rm -r folder/          # Delete folder and contents
```

### Searching
```bash
# FIND TEXT IN FILES
grep "search term" filename.txt          # Search in one file
grep -r "search term" .                   # Search in all files
grep -i "search term" file.txt           # Case-insensitive search

# FIND FILES
find . -name "*.txt"                     # Find all .txt files
find . -type d -name "folder*"           # Find folders
```

### Useful Shortcuts
```bash
# COMMAND LINE SHORTCUTS
Tab                    # Auto-complete
Ctrl + C              # Cancel current command
Ctrl + L              # Clear screen (or type 'clear')
↑ (up arrow)          # Previous command
Ctrl + R              # Search command history

# Get help
command --help        # Show help for a command
man command           # Manual page (q to quit)
```

## Windows-Specific (Command Prompt/PowerShell)
```cmd
# If you're on Windows CMD (not Git Bash):
dir                   # List files (instead of ls)
cd                    # Change directory (same)
copy                  # Copy files (instead of cp)
move                  # Move files (instead of mv)
del                   # Delete files (instead of rm)
cls                   # Clear screen (instead of clear)
```

## Quick Reference
| Task | Command |
|------|---------|
| Show current location | `pwd` |
| List files | `ls` or `ls -la` |
| Go into folder | `cd folder-name` |
| Go up one level | `cd ..` |
| Create file | `touch file.txt` |
| Create folder | `mkdir folder-name` |
| View file | `cat file.txt` |
| Copy file | `cp file.txt newfile.txt` |
| Delete file | `rm file.txt` |

## 🎯 Practice Path
```bash
# Try this sequence:
pwd                           # Where am I?
ls                            # What's here?
mkdir practice                # Make a practice folder
cd practice                   # Go into it
touch test.txt                # Create a file
ls                            # See your file
cd ..                         # Go back up
```

---
**Notes Section**: 
- 
- 
```