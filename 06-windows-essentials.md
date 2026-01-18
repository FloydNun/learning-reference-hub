# Windows 10/11 Essentials - Power User Commands

## PowerShell vs Command Prompt (CMD)

**PowerShell** = Modern, powerful (recommended)  
**CMD** = Old school, but still works

### How to Open Them
```
Windows Key + X → Choose: 
- Windows PowerShell (recommended)
- Command Prompt
- Windows Terminal (Win 11 - best option!)

Or:  
- Search bar → type "powershell" or "cmd"
- Shift + Right-click in folder → "Open PowerShell window here"
```

## Essential PowerShell Commands

### System Information
```powershell
# See system info
systeminfo

# Check Windows version
winver

# See all running processes
Get-Process

# Check disk space
Get-PSDrive

# Network info
ipconfig
ipconfig /all

# Test internet connection
Test-Connection google.com
ping google.com
```

### File & Folder Management
```powershell
# List files (like 'ls' in Linux)
Get-ChildItem
ls                          # Short version
dir                         # Classic version

# List with details
Get-ChildItem -Force        # Show hidden files
ls -Recurse                 # Show all files in subfolders

# Navigate
cd folder-name              # Change directory
cd ..                       # Go up one level
cd ~                        # Go to user home folder
pwd                         # Print working directory

# Create
New-Item -ItemType File -Name "test.txt"
New-Item -ItemType Directory -Name "newfolder"

# Copy & Move
Copy-Item file.txt backup.txt
Copy-Item -Recurse folder newfolder
Move-Item file.txt ./destination/
Rename-Item oldname.txt newname.txt

# Delete
Remove-Item file.txt
Remove-Item -Recurse folder/    # Delete folder
```

### Process Management
```powershell
# See what's running
Get-Process

# Kill a process
Stop-Process -Name "notepad"
Stop-Process -Id 1234

# Start a program
Start-Process notepad
Start-Process chrome "https://github.com"
```

### Network Commands
```powershell
# Test connection
Test-Connection github.com
ping github.com

# Check open ports
Get-NetTCPConnection

# DNS lookup
Resolve-DnsName github.com
nslookup github.com

# Show network adapters
Get-NetAdapter

# Release/renew IP
ipconfig /release
ipconfig /renew

# Flush DNS cache
ipconfig /flushdns
```

### Windows-Specific Tools
```powershell
# Open Windows Settings
start ms-settings: 

# Open Task Manager
taskmgr

# Check disk for errors
chkdsk C: /f

# System file checker
sfc /scannow

# Windows Update
Get-WindowsUpdate           # If module installed
wuauclt /detectnow         # Check for updates

# Environment variables
$env:PATH                   # Show PATH
$env:USERNAME              # Your username
$env:COMPUTERNAME          # Computer name
```

## Windows Subsystem for Linux (WSL)

### Installing WSL
```powershell
# Run as Administrator
wsl --install

# Install specific distro
wsl --install -d Ubuntu

# List available distros
wsl --list --online

# See installed distros
wsl --list --verbose

# Start WSL
wsl

# Run Linux command from PowerShell
wsl ls -la
```

### WSL File Navigation
```powershell
# Access Windows files from WSL
cd /mnt/c/Users/YourName/

# Access WSL files from Windows
\\wsl$\Ubuntu\home\username\
```

## Package Management

### Winget (Windows Package Manager)
```powershell
# Search for package
winget search "vscode"

# Install package
winget install Microsoft. VisualStudioCode
winget install Git.Git
winget install Python.Python.3.11

# List installed
winget list

# Upgrade all
winget upgrade --all

# Uninstall
winget uninstall "app name"
```

### Chocolatey (Alternative Package Manager)
```powershell
# Install Chocolatey first (run as Admin)
# Visit:  https://chocolatey.org/install

# Then use: 
choco install googlechrome
choco install nodejs
choco install python
choco upgrade all
```

## Quick Reference Table

| Task | PowerShell | CMD |
|------|-----------|-----|
| List files | `ls` or `Get-ChildItem` | `dir` |
| Change directory | `cd folder` | `cd folder` |
| Copy file | `Copy-Item file.txt new.txt` | `copy file.txt new.txt` |
| Delete file | `Remove-Item file.txt` | `del file.txt` |
| Create folder | `New-Item -ItemType Directory name` | `mkdir name` |
| Find text | `Select-String "text" file.txt` | `findstr "text" file.txt` |
| Clear screen | `Clear-Host` or `cls` | `cls` |
| Environment var | `$env:PATH` | `echo %PATH%` |

## Useful Shortcuts

```
Windows Key + X          = Power user menu
Windows Key + R          = Run dialog
Windows Key + E          = File Explorer
Windows Key + I          = Settings
Windows Key + .  (period) = Emoji picker
Ctrl + Shift + Esc       = Task Manager
Alt + Tab                = Switch windows
Windows Key + Tab        = Task view
Windows Key + V          = Clipboard history
```

## 💡 Pro Tips

```powershell
# Command history
Get-History
history

# Search command history
Ctrl + R (in PowerShell 7+)

# Create alias
Set-Alias -Name g -Value git

# See all aliases
Get-Alias

# Run as Administrator (right-click PowerShell icon)
# Or:  Ctrl + Shift + Enter when opening
```

---
**Notes Section**: 
- 
- 
```