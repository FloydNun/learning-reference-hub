# Raspberry Pi 5 & ARM - Setup and Commands

## Initial Raspberry Pi Setup

### First Boot
```bash
# Default credentials (if not using Imager setup)
Username: pi
Password: raspberry

# IMMEDIATELY change password
passwd

# Update system
sudo apt update
sudo apt upgrade -y

# Install essential tools
sudo apt install -y git curl wget nano htop

# Configure system
sudo raspi-config
```

### Raspi-Config Menu
```
1. System Options
   - Change hostname
   - Change password
   - Boot options

2. Interface Options
   - Enable SSH (remote access)
   - Enable VNC (remote desktop)
   - Enable I2C, SPI (for hardware projects)

3. Performance Options
   - Overclock (Pi 5 has options)
   - GPU Memory

4. Localization
   - Set locale, timezone, keyboard
```

## SSH Access (Remote Access)

### Enable SSH
```bash
# On Pi: 
sudo systemctl enable ssh
sudo systemctl start ssh

# Find Pi's IP address
hostname -I
ip addr show

# From another computer:
ssh pi@192.168.1.100
# Replace with your Pi's IP
```

### SSH without Password (Key-based)
```bash
# On your computer:
ssh-keygen -t ed25519

# Copy key to Pi:
ssh-copy-id pi@192.168.1.100

# Now you can SSH without password
ssh pi@192.168.1.100
```

## System Monitoring

```bash
# CPU temperature
vcgencmd measure_temp

# CPU frequency
vcgencmd measure_clock arm

# Voltage
vcgencmd measure_volts

# Memory
free -h

# Disk usage
df -h

# System info
cat /proc/cpuinfo
cat /proc/meminfo

# Continuous monitoring
htop
# or
sudo apt install glances
glances
```

## GPIO (Hardware Control)

### Install GPIO Libraries

#### Python
```bash
# Install GPIO library
sudo apt install python3-gpiozero python3-rpi.gpio

# Example: Blink LED
python3 << EOF
from gpiozero import LED
from time import sleep

led = LED(17)  # GPIO pin 17

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
EOF
```

#### Command Line
```bash
# Install WiringPi
sudo apt install wiringpi

# Set GPIO pin 17 as output
gpio -g mode 17 out

# Turn on
gpio -g write 17 1

# Turn off
gpio -g write 17 0

# Read input
gpio -g mode 17 in
gpio -g read 17
```

## Running LLMs on Raspberry Pi

### Ollama on Pi 5

```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Check if running
systemctl status ollama

# Run a model (smaller ones work best)
ollama run phi                    # Microsoft Phi (lightweight)
ollama run tinyllama              # TinyLlama (very light)
ollama run llama3.2:1b           # Llama 3.2 1B (good balance)

# List installed models
ollama list

# Remove a model
ollama rm model-name

# Check resource usage while running
htop
```

### Optimizing for ARM

```bash
# Check ARM architecture
uname -m
# Output: aarch64 (64-bit ARM)

# Monitor during model run
watch -n 1 vcgencmd measure_temp
# Keep an eye on temperature! 

# Add cooling if needed: 
# - Active cooling fan (recommended for Pi 5)
# - Heatsinks
# - Case with ventilation
```

### Lightweight LLM Options for Pi 5

```bash
# TinyLlama (1. 1B parameters) - Runs well
ollama run tinyllama

# Phi-2 (2.7B parameters) - Good performance
ollama run phi

# Llama 3.2 1B - Latest small model
ollama run llama3.2:1b

# For text generation tasks, quantized models work best
# Check model size before downloading: 
ollama show model-name
```

## Docker on Raspberry Pi

```bash
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add user to docker group
sudo usermod -aG docker pi

# Log out and back in, then test: 
docker run hello-world

# Useful Docker commands
docker ps                         # Running containers
docker ps -a                      # All containers
docker images                     # Downloaded images
docker stop container-id          # Stop container
docker rm container-id            # Remove container
```

## Networking

```bash
# Show network interfaces
ip addr show

# WiFi configuration
sudo nmcli dev wifi list          # List networks
sudo nmcli dev wifi connect "SSID" password "PASSWORD"

# Or edit directly: 
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

# Static IP (using nmcli)
sudo nmcli con mod "Wired connection 1" ipv4.addresses 192.168.1.100/24
sudo nmcli con mod "Wired connection 1" ipv4.gateway 192.168.1.1
sudo nmcli con mod "Wired connection 1" ipv4.dns "8.8.8.8"
sudo nmcli con mod "Wired connection 1" ipv4.method manual
```

## Storage & Performance

```bash
# Check SD card health
sudo smartctl -a /dev/mmcblk0

# Expand filesystem (if not auto-expanded)
sudo raspi-config
# Choose:  Advanced Options → Expand Filesystem

# Move swap to USB drive (save SD card life)
sudo dphys-swapfile swapoff
sudo nano /etc/dphys-swapfile
# Change CONF_SWAPFILE=/var/swap to USB path
sudo dphys-swapfile setup
sudo dphys-swapfile swapon

# Benchmark SD card
sudo apt install agnostics
sudo agnostics /dev/mmcblk0
```

## Auto-Start Programs

### Using systemd (Recommended)

```bash
# Create service file
sudo nano /etc/systemd/system/myapp.service

# Add content:
```

```ini
[Unit]
Description=My Application
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/pi/myapp.py
WorkingDirectory=/home/pi
StandardOutput=inherit
StandardError=inherit
Restart=always
User=pi

[Install]
WantedBy=multi-user. target
```

```bash
# Enable and start
sudo systemctl enable myapp.service
sudo systemctl start myapp.service

# Check status
sudo systemctl status myapp.service

# View logs
sudo journalctl -u myapp.service -f
```

## ARM-Specific Compilation

```bash
# Check ARM architecture
lscpu

# Compile with ARM optimizations
gcc -O3 -march=native -mtune=native program.c -o program

# Python packages for ARM
# Some packages need ARM-specific wheels
pip3 install package-name

# If compilation fails, try:
sudo apt install python3-dev
sudo apt install build-essential
```

## Useful Pi Projects Setup

### Web Server
```bash
sudo apt install nginx
sudo systemctl start nginx
# Visit http://pi-ip-address
```

### File Server (Samba)
```bash
sudo apt install samba samba-common-bin
sudo nano /etc/samba/smb.conf

# Add at end: 
# [share]
#   path = /home/pi/shared
#   browseable = yes
#   writable = yes
#   guest ok = yes

sudo systemctl restart smbd
```

### VNC (Remote Desktop)
```bash
sudo apt install realvnc-vnc-server
sudo systemctl enable vncserver-x11-serviced
sudo systemctl start vncserver-x11-serviced

# Or use built-in: 
sudo raspi-config
# Interface Options → VNC → Enable
```

## Power Management

```bash
# Shutdown
sudo shutdown -h now
sudo poweroff

# Reboot
sudo reboot

# Schedule shutdown
sudo shutdown -h +30          # Shutdown in 30 minutes
sudo shutdown -h 23:00        # Shutdown at 11 PM

# Cancel scheduled shutdown
sudo shutdown -c
```

## Quick Reference

| Task | Command |
|------|---------|
| Update system | `sudo apt update && sudo apt upgrade` |
| Check temperature | `vcgencmd measure_temp` |
| Configure system | `sudo raspi-config` |
| Enable SSH | `sudo systemctl enable ssh` |
| Find IP address | `hostname -I` |
| Run Ollama model | `ollama run phi` |
| System monitor | `htop` |
| Shutdown | `sudo shutdown -h now` |

## 🎯 Pi 5 Specific Features

```bash
# Pi 5 has PCIe slot! 
# Check PCIe devices: 
lspci

# Enable PCIe Gen 3 (experimental)
sudo nano /boot/firmware/config.txt
# Add: dtparam=pciex1_gen=3
sudo reboot

# Monitor power
vcgencmd get_throttled
# 0x0 = all good
# Any other = power/thermal issues
```

---
**Notes Section**:
- Pi IP address: 
- Running services:
- GPIO pin assignments:
- 
```