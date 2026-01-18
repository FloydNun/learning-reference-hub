# Linux Essentials - Command Line Power

## File System Navigation

### Understanding Linux Directory Structure
```
/                    Root directory (top of everything)
├── home/           User home directories
│   └── username/   Your personal files
├── etc/            Configuration files
├── var/            Variable data (logs, databases)
├── usr/            User programs and utilities
├── bin/            Essential command binaries
├── tmp/            Temporary files
└── opt/            Optional software packages
```

### Basic Navigation
```bash
# Where am I?
pwd                 # Print working directory

# List files
ls                  # Basic list
ls -l               # Long format (detailed)
ls -la              # Include hidden files (start with .)
ls -lh              # Human-readable sizes
ls -lt              # Sort by modification time

# Change directory
cd /path/to/folder  # Absolute path
cd folder           # Relative path
cd ..                # Go up one level
cd ~                # Go to home directory
cd -                # Go to previous directory
```

## File Operations

```bash
# Create
touch file.txt              # Create empty file
mkdir folder                # Create directory
mkdir -p path/to/folder     # Create nested directories

# View files
cat file.txt                # Display entire file
less file.txt               # View file (q to quit)
head file.txt               # First 10 lines
head -n 20 file.txt         # First 20 lines
tail file.txt               # Last 10 lines
tail -f log.txt             # Follow file (watch updates)

# Copy & Move
cp file.txt backup.txt      # Copy file
cp -r folder/ backup/       # Copy directory recursively
mv file.txt newname.txt     # Rename/move file
mv file.txt /path/to/       # Move to directory

# Delete
rm file.txt                 # Delete file
rm -r folder/               # Delete directory recursively
rm -rf folder/              # Force delete (BE CAREFUL!)
rmdir empty_folder/         # Remove empty directory only
```

## File Permissions

### Understanding Permissions
```bash
# View permissions
ls -l

# Output:  -rwxr-xr-- 1 user group 1234 Jan 08 12:00 file.txt
#         │││││││││
#         │││││││└└─ Others:  read
#         ││││││└─── Others: write (-)
#         │││││└──── Others: execute (-)
#         ││││└───── Group: read
#         │││└────── Group: write (-)
#         ││└─────── Group: execute
#         │└──────── Owner: read
#         └───────── Owner: write, execute

# Change permissions
chmod 755 file.txt          # rwxr-xr-x
chmod +x script.sh          # Add execute permission
chmod -w file.txt           # Remove write permission
chmod u+x,g+x script.sh     # Add execute for user and group

# Change owner
sudo chown user:group file.txt
sudo chown -R user:group folder/
```

## Package Management

### Ubuntu/Debian (apt)
```bash
# Update package list
sudo apt update

# Upgrade all packages
sudo apt upgrade

# Install package
sudo apt install package-name
sudo apt install python3 git nodejs

# Remove package
sudo apt remove package-name
sudo apt autoremove         # Remove unused dependencies

# Search for package
apt search keyword

# Show package info
apt show package-name
```

### Red Hat/CentOS/Fedora (dnf/yum)
```bash
# Update
sudo dnf update

# Install
sudo dnf install package-name

# Remove
sudo dnf remove package-name

# Search
dnf search keyword
```

## Process Management

```bash
# See running processes
ps                          # Your processes
ps aux                      # All processes
top                         # Interactive process viewer (q to quit)
htop                        # Better top (if installed)

# Find process
ps aux | grep process-name
pgrep process-name

# Kill process
kill PID                    # Graceful stop
kill -9 PID                 # Force kill
killall process-name        # Kill by name
pkill process-name          # Kill by pattern

# Background & Foreground
command &                   # Run in background
jobs                        # List background jobs
fg %1                       # Bring job 1 to foreground
bg %1                       # Resume job 1 in background
Ctrl + Z                    # Suspend current process
Ctrl + C                    # Kill current process
```

## System Information

```bash
# System info
uname -a                    # Kernel info
lsb_release -a              # Distribution info
hostnamectl                 # System info

# Disk usage
df -h                       # Disk space (human-readable)
du -sh folder/              # Folder size
du -h --max-depth=1         # Size of subdirectories

# Memory usage
free -h                     # RAM usage
cat /proc/meminfo           # Detailed memory info

# CPU info
lscpu                       # CPU details
cat /proc/cpuinfo           # Detailed CPU info

# Network
ip addr                     # Network interfaces
ifconfig                    # Old way (still works)
netstat -tuln               # Listening ports
ss -tuln                    # Modern netstat
```

## Text Processing

```bash
# Search in files
grep "search term" file.txt
grep -r "search" folder/    # Recursive search
grep -i "term" file.txt     # Case-insensitive
grep -n "term" file. txt     # Show line numbers
grep -v "term" file.txt     # Invert match (exclude)

# Find files
find . -name "*.txt"        # Find by name
find . -type f -name "*.log"# Find files
find . -type d -name "src"  # Find directories
find . -mtime -7            # Modified in last 7 days
find . -size +100M          # Larger than 100MB

# Text manipulation
cat file.txt | grep "term"  # Pipe to grep
sort file.txt               # Sort lines
uniq file.txt               # Remove duplicates
wc file.txt                 # Word/line/char count
wc -l file.txt              # Line count
head -n 5 file.txt          # First 5 lines
tail -n 5 file.txt          # Last 5 lines

# Replace text
sed 's/old/new/g' file.txt  # Replace (display)
sed -i 's/old/new/g' file. txt # Replace (in-place)
```

## Networking

```bash
# Download files
wget https://example.com/file.zip
curl -O https://example.com/file.zip
curl https://api.github.com/users/github

# Test connection
ping google.com
ping -c 4 google.com        # Ping 4 times only

# Check ports
nc -zv host. com 80          # Test if port is open
telnet host.com 80          # Connect to port

# SSH
ssh user@hostname           # Connect to remote
ssh -i key.pem user@host    # Use SSH key
scp file.txt user@host:~/   # Copy file to remote
scp user@host:~/file.txt .   # Copy from remote
```

## User Management

```bash
# Current user
whoami                      # Your username
id                          # Your user ID and groups

# User info
who                         # Logged in users
w                           # Who's doing what
last                        # Login history

# Switch user
su username                 # Switch user
su -                        # Switch to root
sudo command                # Run as superuser

# Add user (requires sudo)
sudo adduser newuser
sudo useradd -m newuser

# Change password
passwd                      # Your password
sudo passwd username        # Other user's password
```

## Shortcuts & Tips

```bash
# Command line shortcuts
Ctrl + C                    # Kill current process
Ctrl + Z                    # Suspend process
Ctrl + D                    # Exit shell
Ctrl + L                    # Clear screen
Ctrl + A                    # Go to start of line
Ctrl + E                    # Go to end of line
Ctrl + U                    # Delete to start of line
Ctrl + K                    # Delete to end of line
Ctrl + R                    # Search command history
!!                           # Repeat last command
!$                          # Last argument of previous command
Tab                         # Auto-complete
Tab Tab                     # Show all completions

# Useful aliases (add to ~/.bashrc)
alias ll='ls -la'
alias .. ='cd ..'
alias gs='git status'
alias update='sudo apt update && sudo apt upgrade'
```

## Quick Reference

| Task | Command |
|------|---------|
| List files | `ls -la` |
| Change directory | `cd /path/to/folder` |
| Copy file | `cp source dest` |
| Move/rename | `mv source dest` |
| Delete file | `rm file. txt` |
| View file | `cat file.txt` or `less file.txt` |
| Search in file | `grep "term" file.txt` |
| Find files | `find . -name "*.txt"` |
| Check processes | `ps aux` or `top` |
| Disk space | `df -h` |
| Install package | `sudo apt install package` |

---
**Notes Section**:
- 
- 
```