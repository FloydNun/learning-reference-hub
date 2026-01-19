#!/usr/bin/env python3
"""
🛸 COUNTERBALANCE - Deduplication Utility
Shared utility for hash-based duplicate detection
Used by ALL processors to prevent duplicate processing
"""

import hashlib
import json
from pathlib import Path
from typing import Optional

from Import_Header_Include import log_header, get_runtime, DEBUG
from Import_Footer_Include import log_footer, close_out
from Import_Globals_Include import *


class DedupManager:
    """Manages file deduplication across all processors"""
    
    def __init__(self, processor_name: str):
        self.processor_name = processor_name
        self.hashes_dir = ROOT_DIR / "System_Logs" / "hashes"
        self.hashes_dir.mkdir(parents=True, exist_ok=True)
        self.hashes_file = self.hashes_dir / f"{processor_name}_hashes.json"
        self.hashes = self.load_hashes()
    
    def load_hashes(self) -> dict:
        """Load existing hashes"""
        if self.hashes_file.exists():
            try:
                with open(self.hashes_file, 'r') as f:
                    return json.load(f)
            except Exception: 
                return {}
        return {}
    
    def save_hashes(self):
        """Save hashes to file"""
        try:
            with open(self.hashes_file, 'w') as f:
                json.dump(self.hashes, f, indent=2)
        except Exception as e:
            print(f"Failed to save hashes: {e}")
    
    def calculate_hash(self, file_path: Path) -> Optional[str]:
        """Calculate MD5 hash of file"""
        md5 = hashlib.md5()
        try:
            with open(file_path, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    md5.update(chunk)
            return md5.hexdigest()
        except Exception:
            return None
    
    def is_duplicate(self, file_path:  Path, file_hash: str = None) -> bool:
        """
        Check if file is duplicate by: 
        1. Content hash (MD5)
        2. Filename
        
        Returns True if duplicate found
        """
        filename = file_path.name
        
        # Calculate hash if not provided
        if file_hash is None:
            file_hash = self.calculate_hash(file_path)
            if file_hash is None:
                return False
        
        # Check by hash (same content)
        for stored_name, stored_hash in self.hashes.items():
            if stored_hash == file_hash: 
                if DEBUG:
                    print(f"Duplicate by hash: {filename} == {stored_name}")
                return True
        
        # Check by filename (same name)
        if filename in self.hashes:
            if DEBUG:
                print(f"Duplicate by filename: {filename}")
            return True
        
        return False
    
    def register_file(self, file_path: Path, file_hash: str = None):
        """Register file in dedup database"""
        filename = file_path.name
        
        if file_hash is None:
            file_hash = self.calculate_hash(file_path)
        
        if file_hash: 
            self.hashes[filename] = file_hash
            self.save_hashes()
            
            if DEBUG:
                print(f"Registered: {filename} ({file_hash[: 8]}...)")


# Example usage in any processor: 
"""
from dedup_utility import DedupManager

class MyProcessor:
    def __init__(self):
        self.dedup = DedupManager("MyProcessor")
    
    def process_file(self, file_path):
        # Check duplicate
        if self.dedup.is_duplicate(file_path):
            print(f"Skipping duplicate: {file_path.name}")
            return False
        
        # ...  process file ... 
        
        # Register after successful processing
        self.dedup. register_file(file_path)
        return True
"""