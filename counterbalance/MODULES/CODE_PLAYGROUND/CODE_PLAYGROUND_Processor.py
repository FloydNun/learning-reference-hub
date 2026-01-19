#!/usr/bin/env python3
"""
🛸 COUNTERBALANCE - CODE_PLAYGROUND Processor
Manages interactive code playground with version history
- Validates code files
- Tracks edit history
- Creates version timeline
- Integrates with Monaco Editor
"""

import sys
import os
from pathlib import Path
from datetime import datetime
import json
import shutil

# Add parent directories to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent. parent))

from Import_Header_Include import log_header, get_runtime, DEBUG
from Import_Footer_Include import log_footer, close_out
from Import_Globals_Include import *


class CodePlaygroundProcessor:
    """Processor for CODE_PLAYGROUND module"""
    
    def __init__(self):
        self.script_name = "CODE_PLAYGROUND_Processor. py"
        self.module_dir = Path(__file__).parent
        self.versions_dir = self.module_dir / "versions"
        self.versions_dir.mkdir(exist_ok=True)
        
        log_header(self.script_name, "CODE_PLAYGROUND Processor initialized")
    
    def log_console(self, message:  str):
        """Log to console. log"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [CONSOLE] [{self.script_name}] {message}\n"
        
        log_file = LOGS_DIR / "console.log"
        with open(log_file, 'a') as f:
            f.write(log_entry)
        
        if DEBUG:
            print(f"🎮 PLAYGROUND: {message}")
    
    def log_error(self, message: str):
        """Log to error.log"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [ERROR] [{self.script_name}] {message}\n"
        
        log_file = LOGS_DIR / "error.log"
        with open(log_file, 'a') as f:
            f.write(log_entry)
        
        print(f"❌ ERROR:  {message}")
    
    def create_version(self, file_path: Path, content: str, metadata: dict = None) -> bool:
        """Create a version snapshot of code"""
        self.log_console(f"Creating version for:  {file_path. name}")
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        version_name = f"{file_path.stem}_v{timestamp}{file_path.suffix}"
        version_path = self.versions_dir / file_path.stem / version_name
        version_path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            # Save code version
            with open(version_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # Save metadata
            meta_path = version_path.with_suffix('.meta. json')
            meta = {
                'timestamp': timestamp,
                'original_name': file_path.name,
                'version':  version_name,
                'size': len(content),
                'lines': content.count('\n') + 1,
            }
            if metadata:
                meta.update(metadata)
            
            with open(meta_path, 'w') as f:
                json.dump(meta, f, indent=2)
            
            self.log_console(f"Version created:  {version_name}")
            return True
        except Exception as e:
            self.log_error(f"Failed to create version: {e}")
            return False
    
    def get_version_history(self, file_stem: str) -> list:
        """Get all versions of a file"""
        version_folder = self.versions_dir / file_stem
        
        if not version_folder.exists():
            return []
        
        versions = []
        for meta_file in sorted(version_folder.glob("*. meta.json")):
            try:
                with open(meta_file, 'r') as f:
                    meta = json.load(f)
                versions.append(meta)
            except Exception as e:
                self.log_error(f"Failed to read metadata: {e}")
        
        return versions
    
    def validate_code(self, file_path: Path) -> dict:
        """Validate code syntax"""
        self.log_console(f"Validating:  {file_path.name}")
        
        result = {
            'valid': False,
            'language': None,
            'errors': []
        }
        
        suffix = file_path.suffix.lower()
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Python validation
            if suffix == '.py': 
                result['language'] = 'python'
                try:
                    compile(content, file_path. name, 'exec')
                    result['valid'] = True
                except SyntaxError as e: 
                    result['errors'].append(f"Line {e.lineno}: {e.msg}")
            
            # JavaScript basic validation (check for syntax errors)
            elif suffix in ['.js', '.jsx']: 
                result['language'] = 'javascript'
                # Basic check - just ensure it's not empty
                if content. strip():
                    result['valid'] = True
                else:
                    result['errors'].append("File is empty")
            
            # HTML validation
            elif suffix in ['.html', '.htm']: 
                result['language'] = 'html'
                if '<html' in content. lower() or '<! doctype' in content.lower():
                    result['valid'] = True
                else:
                    result['errors'].append("Missing HTML structure")
            
            # CSS validation
            elif suffix == '.css':
                result['language'] = 'css'
                result['valid'] = True  # Basic acceptance
            
            else:
                result['language'] = 'unknown'
                result['valid'] = True  # Accept unknown types
            
            self.log_console(f"Validation:  {result['language']} - {'✅ Valid' if result['valid'] else '❌ Invalid'}")
            return result
            
        except Exception as e:
            self.log_error(f"Validation failed: {e}")
            result['errors'].append(str(e))
            return result
    
    def process_file(self, file_path: Path) -> bool:
        """Process a file for playground"""
        self.log_console(f"Processing for playground: {file_path.name}")
        
        # Validate
        validation = self.validate_code(file_path)
        
        if not validation['valid']:
            self. log_error(f"Validation failed:  {', '.join(validation['errors'])}")
            return False
        
        # Read content
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            self.log_error(f"Failed to read file: {e}")
            return False
        
        # Create initial version
        metadata = {
            'language': validation['language'],
            'source': 'inbox',
            'validated': True
        }
        
        if not self.create_version(file_path, content, metadata):
            return False
        
        # Copy to playground directory
        dest_path = self.module_dir / file_path.name
        try:
            shutil.copy2(file_path, dest_path)
            self.log_console(f"File ready in playground: {file_path.name}")
            return True
        except Exception as e:
            self. log_error(f"Failed to copy file: {e}")
            return False
    
    def list_playground_files(self):
        """List all files in playground"""
        self.log_console("Listing playground files")
        
        files = [f for f in self.module_dir.iterdir() 
                if f.is_file() 
                and f.suffix not in ['.py', '.md', '.json']
                and not f.name. startswith('.')]
        
        if not files:
            print("\n🎮 CODE_PLAYGROUND is empty\n")
            return
        
        print(f"\n🎮 CODE_PLAYGROUND contains {len(files)} file(s):\n")
        
        for file_path in files:
            versions = self.get_version_history(file_path.stem)
            print(f"  📄 {file_path.name}")
            print(f"     Versions: {len(versions)}")
            if versions:
                latest = versions[-1]
                print(f"     Last edited: {latest. get('timestamp', 'unknown')}")
            print()


def main():
    """Main entry point"""
    processor = CodePlaygroundProcessor()
    
    try:
        processor.list_playground_files()
        close_out("CODE_PLAYGROUND_Processor.py", "SUCCESS")
    except Exception as e: 
        processor.log_error(f"Fatal error: {e}")
        close_out("CODE_PLAYGROUND_Processor.py", "FAILURE")
        sys.exit(1)


if __name__ == "__main__":
    main()