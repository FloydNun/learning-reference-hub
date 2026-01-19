#!/usr/bin/env python3
"""
🛸 COUNTERBALANCE - INBOX Processor (UPDATED)
First point of contact - NOW WITH GLOBAL DEDUPLICATION
- Detects file type and content
- CHECKS DEDUP BEFORE ROUTING (prevents duplicates everywhere)
- Routes to Root_Processor for preparation
- Handles special cases
"""

import sys
import os
from pathlib import Path
from datetime import datetime

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from Import_Header_Include import log_header, get_runtime, DEBUG
from Import_Footer_Include import log_footer, close_out
from Import_Globals_Include import *

# Import dedup utility
from utilities.dedup_utility import DedupManager


class InboxProcessor:
    """Processor for INBOX - routes files with deduplication"""
    
    def __init__(self):
        self.script_name = "INBOX_Processor. py"
        log_header(self.script_name, "INBOX Processor initialized")
        
        # Initialize GLOBAL dedup manager
        self.dedup = DedupManager("GLOBAL_INBOX")
        
    def log_console(self, message: str):
        """Log to console. log"""
        timestamp = datetime. now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [CONSOLE] [{self.script_name}] {message}\n"
        
        log_file = LOGS_DIR / "console.log"
        with open(log_file, 'a') as f:
            f.write(log_entry)
        
        if DEBUG:  
            print(f"📋 INBOX: {message}")
    
    def log_error(self, message: str):
        """Log to error.log"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [ERROR] [{self.script_name}] {message}\n"
        
        log_file = LOGS_DIR / "error.log"
        with open(log_file, 'a') as f:
            f.write(log_entry)
        
        print(f"❌ ERROR: {message}")
    
    def detect_file_type(self, file_path: Path) -> str:
        """Detect file type and processing needs"""
        suffix = file_path.suffix.lower()
        name = file_path.name. lower()
        
        # Python scripts
        if suffix == '.py':  
            return 'python_script'
        
        # Markdown files
        elif suffix == '.md':
            return 'markdown'
        
        # Jupyter notebooks
        elif suffix == '.ipynb':
            return 'notebook'
        
        # Web code
        elif suffix in ['.js', '.ts', '.jsx', '.tsx', '.html', '.css']: 
            return 'web_code'
        
        # Data files
        elif suffix in ['.json', '.yaml', '.yml', '.csv', '.xml']: 
            return 'data_file'
        
        # Images
        elif suffix in ['.png', '.jpg', '.jpeg', '. gif', '.svg', '.bmp']: 
            return 'image'
        
        # PDFs
        elif suffix == '.pdf':
            return 'pdf'
        
        # Documents
        elif suffix in ['.txt', '.doc', '.docx']: 
            return 'document'
        
        # ZIPs
        elif suffix in ['.zip', '.tar', '.gz', '. rar', '.7z']:
            return 'archive'
        
        # Unknown
        else:
            return 'unknown'
    
    def determine_destination(self, file_path: Path, file_type: str) -> str:
        """Determine where file should go"""
        
        # Documents and images go to DOCS_INBOX for OCR
        if file_type in ['image', 'pdf', 'document']:
            return 'DOCS_INBOX'
        
        # Archives go to ZIP_INBOX
        elif file_type == 'archive':
            return 'ZIP_INBOX'
        
        # Code files go through Root_Processor
        elif file_type in ['python_script', 'web_code']: 
            return 'ROOT_PROCESSOR'
        
        # Markdown (chats) go to CHATS module
        elif file_type == 'markdown':
            return 'MODULES/CHATS'
        
        # Data files go to CODE_REFINERY
        elif file_type == 'data_file':
            return 'CODE_REFINERY'
        
        # Unknown goes to MYSTERY_INBOX
        else: 
            return 'MYSTERY_INBOX'
    
    def process_file(self, file_path: Path) -> bool:
        """Process a single file with DEDUP CHECK"""
        self.log_console(f"Processing: {file_path.name}")
        
        # ========================================
        # DEDUP CHECK - HAPPENS FIRST! 
        # ========================================
        if self.dedup.is_duplicate(file_path):
            self.log_console(f"⚠️  DUPLICATE DETECTED:   {file_path.name}")
            self.log_console(f"   Moving to __Scrap_Pile/duplicates/")
            
            # Move to scrap pile
            dup_dir = ROOT_DIR / "__Scrap_Pile" / "duplicates"
            dup_dir.mkdir(parents=True, exist_ok=True)
            
            try:
                import shutil
                shutil.move(str(file_path), str(dup_dir / file_path.name))
                self.log_console(f"   Duplicate archived")
                return False
            except Exception as e: 
                self.log_error(f"Failed to move duplicate: {e}")
                return False
        
        # Not a duplicate - continue processing
        file_type = self.detect_file_type(file_path)
        self.log_console(f"File type:   {file_type}")
        
        destination = self.determine_destination(file_path, file_type)
        self.log_console(f"Destination: {destination}")
        
        # Register file in dedup database
        self.dedup.register_file(file_path)
        self.log_console(f"✅ Registered in dedup database")
        
        # TODO: Actually route file to destination
        # For now, just log what would happen
        self.log_console(f"Would route to: {destination}")
        
        return True
    
    def scan_inbox(self):
        """Scan INBOX and process files"""
        self.log_console("Scanning INBOX")
        
        files = [f for f in INBOX_DIR. iterdir() if f.is_file() and f.name != 'README.md']
        
        if not files:
            print("\n📭 INBOX is empty\n")
            return
        
        print(f"\n📬 INBOX contains {len(files)} file(s):\n")
        
        processed = 0
        duplicates = 0
        
        for file_path in files:  
            print(f"  📄 {file_path.name}")
            success = self.process_file(file_path)
            
            if success:
                processed += 1
                print(f"     ✅ Processed")
            else:
                duplicates += 1
                print(f"     ⚠️  Duplicate - archived")
        
        print(f"\n📊 Summary:")
        print(f"   Processed:  {processed}")
        print(f"   Duplicates: {duplicates}")
        print()


def main():
    """Main entry point"""
    processor = InboxProcessor()
    
    try:
        processor.scan_inbox()
        close_out("INBOX_Processor.py", "SUCCESS")
    except Exception as e:  
        processor.log_error(f"Fatal error: {e}")
        close_out("INBOX_Processor.py", "FAILURE")
        sys.exit(1)


if __name__ == "__main__":
    main()