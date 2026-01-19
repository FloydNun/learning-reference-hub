#!/usr/bin/env python3
"""
🛸 COUNTERBALANCE - HTML_SHOWCASE Processor
Manages standalone HTML files with gallery preview
- Validates HTML files (standalone, React, Firebase)
- Generates thumbnails/previews
- Creates horizontal scrolling gallery
- Integrates Floyd's utilities
"""

import sys
import os
from pathlib import Path
from datetime import datetime
import json
import shutil
import re

# Add parent directories to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from Import_Header_Include import log_header, get_runtime, DEBUG
from Import_Footer_Include import log_footer, close_out
from Import_Globals_Include import *


class HTMLShowcaseProcessor: 
    """Processor for HTML_SHOWCASE module"""
    
    def __init__(self):
        self.script_name = "HTML_SHOWCASE_Processor. py"
        self.module_dir = Path(__file__).parent
        self.previews_dir = self.module_dir / "previews"
        self.utilities_dir = self.module_dir / "utilities"
        self. metadata_dir = self.module_dir / ". metadata"
        
        # Create directories
        self.previews_dir. mkdir(exist_ok=True)
        self.utilities_dir. mkdir(exist_ok=True)
        self.metadata_dir. mkdir(exist_ok=True)
        
        log_header(self.script_name, "HTML_SHOWCASE Processor initialized")
    
    def log_console(self, message: str):
        """Log to console. log"""
        timestamp = datetime. now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [CONSOLE] [{self.script_name}] {message}\n"
        
        log_file = LOGS_DIR / "console.log"
        with open(log_file, 'a') as f:
            f.write(log_entry)
        
        if DEBUG: 
            print(f"🎨 SHOWCASE: {message}")
    
    def log_error(self, message: str):
        """Log to error.log"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [ERROR] [{self.script_name}] {message}\n"
        
        log_file = LOGS_DIR / "error.log"
        with open(log_file, 'a') as f:
            f.write(log_entry)
        
        print(f"❌ ERROR: {message}")
    
    def detect_html_type(self, content: str) -> dict:
        """Detect HTML type (standalone, React, Firebase, etc.)"""
        result = {
            'type': 'standalone',
            'framework': None,
            'dependencies': [],
            'features': []
        }
        
        content_lower = content.lower()
        
        # Detect React
        if 'react' in content_lower or 'reactdom' in content_lower: 
            result['type'] = 'react'
            result['framework'] = 'React'
            result['dependencies']. append('React')
        
        # Detect Firebase
        if 'firebase' in content_lower: 
            result['features'].append('Firebase')
            result['dependencies'].append('Firebase')
        
        # Detect Vue
        if 'vue' in content_lower and 'vue. js' in content_lower:
            result['type'] = 'vue'
            result['framework'] = 'Vue.js'
            result['dependencies'].append('Vue')
        
        # Detect D3.js
        if 'd3.js' in content_lower or 'd3.min.js' in content_lower:
            result['features'].append('D3.js')
            result['dependencies'].append('D3')
        
        # Detect Bootstrap
        if 'bootstrap' in content_lower: 
            result['features'].append('Bootstrap')
        
        # Detect jQuery
        if 'jquery' in content_lower:
            result['features'].append('jQuery')
        
        return result
    
    def extract_metadata(self, file_path: Path) -> dict:
        """Extract metadata from HTML file"""
        self.log_console(f"Extracting metadata:  {file_path.name}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            metadata = {
                'filename': file_path.name,
                'created': datetime.now().isoformat(),
                'size': len(content),
                'valid': False,
                'title': 'Untitled',
                'description':  '',
                'type': 'standalone',
                'framework': None,
                'dependencies': [],
                'features': []
            }
            
            # Extract title
            title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
            if title_match:
                metadata['title'] = title_match.group(1).strip()
            
            # Extract meta description
            desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE)
            if desc_match:
                metadata['description'] = desc_match.group(1).strip()
            
            # Detect type and features
            html_type = self.detect_html_type(content)
            metadata. update(html_type)
            
            # Validate basic HTML structure
            if '<html' in content. lower() or '<!doctype' in content.lower():
                metadata['valid'] = True
            
            return metadata
            
        except Exception as e:
            self.log_error(f"Failed to extract metadata: {e}")
            return None
    
    def create_preview(self, file_path: Path, metadata: dict) -> bool:
        """Create preview entry for gallery"""
        self.log_console(f"Creating preview for: {file_path.name}")
        
        try:
            preview_data = {
                'filename': file_path.name,
                'title': metadata['title'],
                'description': metadata['description'],
                'type': metadata['type'],
                'framework': metadata['framework'],
                'features': metadata['features'],
                'created': metadata['created']
            }
            
            preview_file = self.metadata_dir / f"{file_path.stem}.json"
            with open(preview_file, 'w') as f:
                json.dump(preview_data, f, indent=2)
            
            self.log_console(f"Preview created: {preview_file.name}")
            return True
            
        except Exception as e: 
            self.log_error(f"Failed to create preview: {e}")
            return False
    
    def process_html(self, file_path: Path) -> bool:
        """Process an HTML file for showcase"""
        self.log_console(f"Processing HTML: {file_path.name}")
        
        # Extract metadata
        metadata = self.extract_metadata(file_path)
        if not metadata:
            return False
        
        if not metadata['valid']:
            self.log_error(f"Invalid HTML structure: {file_path.name}")
            return False
        
        # Create preview entry
        if not self.create_preview(file_path, metadata):
            return False
        
        # Copy to showcase directory
        dest_path = self.module_dir / file_path.name
        try:
            shutil.copy2(file_path, dest_path)
            self.log_console(f"HTML file added to showcase: {file_path. name}")
            return True
        except Exception as e:
            self.log_error(f"Failed to copy HTML: {e}")
            return False
    
    def generate_gallery_index(self):
        """Generate the showcase gallery HTML"""
        self.log_console("Generating gallery index")
        
        # Load all previews
        previews = []
        for preview_file in self.metadata_dir.glob("*.json"):
            try:
                with open(preview_file, 'r') as f:
                    preview = json.load(f)
                previews.append(preview)
            except Exception as e:
                self.log_error(f"Failed to load preview: {e}")
        
        # Sort by date (newest first)
        previews.sort(key=lambda x: x['created'], reverse=True)
        
        # Generate HTML (will create showcase_indexer.html)
        self.log_console(f"Found {len(previews)} items for gallery")
        
        return previews
    
    def list_showcase_items(self):
        """List all items in showcase"""
        self.log_console("Listing showcase items")
        
        previews = self.generate_gallery_index()
        
        if not previews:
            print("\n🎨 HTML_SHOWCASE is empty\n")
            return
        
        print(f"\n🎨 HTML_SHOWCASE contains {len(previews)} item(s):\n")
        
        for preview in previews:
            print(f"  🌐 {preview['title']}")
            print(f"     File: {preview['filename']}")
            print(f"     Type:  {preview['type']}")
            if preview['framework']:
                print(f"     Framework: {preview['framework']}")
            if preview['features']:
                print(f"     Features: {', '.join(preview['features'])}")
            print()


def main():
    """Main entry point"""
    processor = HTMLShowcaseProcessor()
    
    try:
        processor.list_showcase_items()
        close_out("HTML_SHOWCASE_Processor.py", "SUCCESS")
    except Exception as e: 
        processor.log_error(f"Fatal error: {e}")
        close_out("HTML_SHOWCASE_Processor.py", "FAILURE")
        sys.exit(1)


if __name__ == "__main__":
    main()