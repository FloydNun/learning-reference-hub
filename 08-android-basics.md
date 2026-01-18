# Android Essentials - Development & ADB Commands

## Android Debug Bridge (ADB)

### Setup ADB

#### On Windows
```powershell
# Install via Winget
winget install Google.PlatformTools

# Or download from: 
# https://developer.android.com/studio/releases/platform-tools

# Add to PATH (replace with your path)
$env:PATH += ";C:\platform-tools"
```

#### On Linux
```bash
# Ubuntu/Debian
sudo apt install android-tools-adb android-tools-fastboot

# Or download platform-tools
wget https://dl.google.com/android/repository/platform-tools-latest-linux.zip
unzip platform-tools-latest-linux.zip
sudo mv platform-tools /usr/local/
echo 'export PATH=$PATH:/usr/local/platform-tools' >> ~/.bashrc
```

### Enable Developer Options on Android

```
1. Settings → About Phone
2. Tap "Build Number" 7 times
3. Go back → Developer Options
4. Enable "USB Debugging"
5. Connect phone via USB
```

## Essential ADB Commands

### Device Connection
```bash
# Check if device is connected
adb devices

# Connect via WiFi (device and computer on same network)
adb tcpip 5555                          # On USB first
adb connect 192.168.1.100:5555          # Replace with phone's IP

# Disconnect
adb disconnect

# Restart ADB server
adb kill-server
adb start-server
```

### File Management
```bash
# Push file to device
adb push file.txt /sdcard/
adb push app.apk /sdcard/Download/

# Pull file from device
adb pull /sdcard/photo.jpg ./
adb pull /sdcard/Download/file.txt ./desktop/

# List files on device
adb shell ls /sdcard/
adb shell ls -la /sdcard/Download/

# Delete file
adb shell rm /sdcard/file.txt
```

### App Management
```bash
# Install APK
adb install app.apk
adb install -r app.apk                  # Reinstall existing app

# Uninstall app
adb uninstall com.package.name

# List installed packages
adb shell pm list packages              # All packages
adb shell pm list packages -3           # Third-party apps only
adb shell pm list packages | grep keyword

# Get package info
adb shell pm path com.package.name      # Get APK path
adb shell dumpsys package com.package.name

# Clear app data
adb shell pm clear com. package.name

# Start app
adb shell am start -n com.package.name/. MainActivity
```

### System Information
```bash
# Device info
adb shell getprop                       # All properties
adb shell getprop ro.product.model      # Device model
adb shell getprop ro.build.version.release # Android version

# Battery info
adb shell dumpsys battery

# Display info
adb shell wm size                       # Screen resolution
adb shell wm density                    # Screen density

# Memory info
adb shell cat /proc/meminfo
adb shell dumpsys meminfo

# CPU info
adb shell cat /proc/cpuinfo
```

### Screen & Input
```bash
# Take screenshot
adb shell screencap /sdcard/screen.png
adb pull /sdcard/screen.png

# Record screen
adb shell screenrecord /sdcard/demo.mp4
# Press Ctrl+C to stop, then: 
adb pull /sdcard/demo.mp4

# Input text
adb shell input text "Hello%sWorld"    # %s = space

# Tap screen (x, y coordinates)
adb shell input tap 500 1000

# Swipe
adb shell input swipe 300 1000 300 500 # x1 y1 x2 y2

# Press keys
adb shell input keyevent 3             # Home button
adb shell input keyevent 4             # Back button
adb shell input keyevent 26            # Power button
adb shell input keyevent 24            # Volume up
adb shell input keyevent 25            # Volume down
```

### Logcat (View Logs)
```bash
# View all logs
adb logcat

# Clear logs
adb logcat -c

# Filter by tag
adb logcat -s TAG_NAME

# Filter by priority (V=Verbose, D=Debug, I=Info, W=Warning, E=Error, F=Fatal)
adb logcat *:E                         # Show only errors
adb logcat *:W                         # Show warnings and errors

# Save to file
adb logcat > logfile.txt

# Filter by app
adb logcat | grep "com.myapp"
```

### System Control
```bash
# Reboot
adb reboot
adb reboot bootloader                  # Reboot to bootloader
adb reboot recovery                    # Reboot to recovery

# Power off
adb shell reboot -p

# Get into shell
adb shell                              # Interactive shell
adb shell "command"                    # Single command

# Root shell (if device is rooted)
adb root
adb shell
su
```

## Termux (Linux Terminal on Android)

### Installing Termux
```
Download from F-Droid (recommended):
https://f-droid.org/en/packages/com. termux/

NOT from Play Store (outdated)
```

### Basic Termux Setup
```bash
# Update packages
pkg update && pkg upgrade

# Install essential tools
pkg install git
pkg install python
pkg install nodejs
pkg install openssh
pkg install nano
pkg install wget
pkg install curl

# Storage access
termux-setup-storage

# Now you can access: 
# ~/storage/shared = Internal storage
# ~/storage/downloads = Downloads folder
```

### Useful Termux Commands
```bash
# Package management
pkg search package-name
pkg install package-name
pkg uninstall package-name
pkg list-installed

# SSH server (access from computer)
pkg install openssh
sshd                               # Start SSH server
whoami                             # Your username
# From computer: ssh user@phone-ip -p 8022

# Python
pkg install python
python script.py
pip install package

# Git
git clone https://github.com/user/repo
cd repo

# Text editor
nano file.txt
# Ctrl+O to save, Ctrl+X to exit
```

### Termux: API (Phone Functions)
```bash
# Install Termux: API app from F-Droid first

pkg install termux-api

# Examples:
termux-battery-status              # Battery info
termux-camera-photo photo.jpg      # Take photo
termux-location                    # Get GPS coordinates
termux-notification --title "Hi"   # Send notification
termux-toast "Hello"               # Show toast message
termux-tts-speak "Hello world"     # Text to speech
termux-vibrate                     # Vibrate phone
termux-wifi-connectioninfo         # WiFi info
```

## Android File System

```
/sdcard/                           Internal storage (main)
├── Download/                      Downloads
├── DCIM/                          Camera photos
├── Documents/                     Documents
├── Pictures/                      Pictures
└── Android/
    └── data/                      App data

/data/data/                        App private data (needs root)
/system/                           System files (needs root)
/cache/                            Cache
```

## Common ADB Issues

### Device Not Found
```bash
# Check USB debugging is enabled
# Try different USB cable
# Restart ADB
adb kill-server
adb start-server

# Windows: Install device drivers
# Linux: Add udev rules
```

### Unauthorized Device
```
1.  Disconnect device
2. Revoke USB debugging authorizations in Developer Options
3. Reconnect device
4. Accept authorization popup
```

## Quick Reference

| Task | Command |
|------|---------|
| List devices | `adb devices` |
| Install APK | `adb install app.apk` |
| Push file | `adb push local. txt /sdcard/` |
| Pull file | `adb pull /sdcard/file.txt` |
| Screenshot | `adb shell screencap -p /sdcard/s.png` |
| View logs | `adb logcat` |
| Shell access | `adb shell` |
| Reboot | `adb reboot` |

---
**Notes Section**: 
- My device IP: 
- Common packages: 
- 
```