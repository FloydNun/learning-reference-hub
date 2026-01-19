#!/usr/bin/env python3
"""
🛸 COUNTERBALANCE - Overwatch Processor
Watches for file changes and triggers appropriate processors
- Monitors INBOX for new files
- Monitors modules for errors
- Triggers healing processes
"""

import sys
import time
from pathlib import Path
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from Import_Header_Include import log_header, get_runtime, DEBUG
from Import_Footer_Include import log_footer, close_out
from Import_Globals_Include import *


class OverwatchHandler(FileSystemEventHandler):
    """File system event handler for Overwatch"""
    
    def __init__(self):
        self.script_name = "Overwatch_Processor.py"
        log_header(self.script_name, "Overwatch Handler initialized")
        self.processing = set()  # Track files being processed
    
    def log_console(self, message: str):
        """Log to console. log"""
        timestamp = datetime. now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [CONSOLE] [{self.script_name}] {message}\n"
        
        log_file = LOGS_DIR / "console.log"
        with open(log_file, 'a') as f:
            f.write(log_entry)
        
        if DEBUG:
            print(f"👁️  OVERWATCH: {message}")
    
    def on_created(self, event):
        """Handle file creation events"""
        if event.is_directory:
            return
        
        file_path = Path(event.src_path)
        
        # Ignore certain files
        if file_path.name in ['README.md', '. gitkeep'] or file_path.name.startswith('.'):
            return
        
        # Ignore if already processing
        if str(file_path) in self.processing:
            return
        
        self.processing.add(str(file_path))
        self.log_console(f"New file detected: {file_path. name}")
        
        # Determine action
        if INBOX_DIR in file_path.parents:
            self.log_console(f"INBOX file detected: {file_path.name}")
            self.log_console("  → Trigger:  Run Root_Processor. py")
            # In full system, would call:  subprocess.run(['python', 'Root_Processor.py'])
        
        elif LOGS_DIR in file_path.parents and 'error' in file_path.name:
            self.log_console("Error log updated - checking for healing triggers")
            # In full system, would analyze error log and trigger healing
        
        self.processing.discard(str(file_path))
    
    def on_modified(self, event):
        """Handle file modification events"""
        if event.is_directory:
            return
        
        file_path = Path(event.src_path)
        
        # Watch for error log changes
        if file_path. name == 'error.log': 
            self.log_console("Error log modified - monitoring for failures")


class OverwatchProcessor:
    """Main Overwatch processor"""
    
    def __init__(self):
        self.script_name = "Overwatch_Processor.py"
        log_header(self. script_name, "Overwatch Processor starting")
        self.observer = Observer()
        self.handler = OverwatchHandler()
    
    def start_watching(self):
        """Start watching directories"""
        print("\n" + "="*60)
        print("👁️  OVERWATCH ACTIVATED")
        print("="*60)
        print("\nWatching:")
        print(f"  📥 INBOX:       {INBOX_DIR}")
        print(f"  📊 Logs:       {LOGS_DIR}")
        print(f"  📦 Modules:    {MODULES_DIR}")
        print("\nPress Ctrl+C to stop\n")
        print("="*60 + "\n")
        
        # Schedule watchers
        self.observer.schedule(self.handler, str(INBOX_DIR), recursive=False)
        self.observer. schedule(self.handler, str(LOGS_DIR), recursive=False)
        self.observer.schedule(self.handler, str(MODULES_DIR), recursive=True)
        
        # Start observer
        self.observer.start()
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n\n👁️  OVERWATCH SHUTTING DOWN.. .\n")
            self.observer.stop()
        
        self.observer.join()
        close_out(self.script_name, "SUCCESS")


def main():
    """Main entry point"""
    try:
        processor = OverwatchProcessor()
        processor.start_watching()
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        close_out("Overwatch_Processor.py", "FAILURE")
        sys.exit(1)


if __name__ == "__main__": 
    main()