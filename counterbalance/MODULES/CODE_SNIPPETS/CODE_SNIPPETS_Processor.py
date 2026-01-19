#!/usr/bin/env python3
"""
🛸 COUNTERBALANCE - CODE_SNIPPETS Processor
Manages validated single scripts in Jupyter notebook style
- Validates and stores snippets
- Generates Jupyter-style presentation
- Links back to source references
- Allows running and testing
"""

import sys
import os
from pathlib import Path
from datetime import datetime
import json
import hashlib

# Add parent directories to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from Import_Header_Include import log_header, get_runtime, DEBUG
from Import_Footer_Include import log_footer, close_out
from Import_Globals_Include import *


class CodeSnippetsProcessor: 
    """Processor for CODE_SNIPPETS module"""
    
    def __init__(self):
        self.script_name = "CODE_SNIPPETS_Processor. py"
        self.module_dir = Path(__file__).parent
        self.metadata_dir = self.module_dir / ". metadata"
        self.metadata_dir.mkdir(exist_ok=True)
        
        log_header(self.script_name, "CODE_SNIPPETS Processor initialized")
    
    def log_console(self, message: str):
        """Log to console. log"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [CONSOLE] [{self.script_name}] {message}\n"
        
        log_file = LOGS_DIR / "console.log"
        with open(log_file, 'a') as f:
            f.write(log_entry)
        
        if DEBUG: 
            print(f"📦 SNIPPETS: {message}")
    
    def log_error(self, message: str):
        """Log to error.log"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [ERROR] [{self.script_name}] {message}\n"
        
        log_file = LOGS_DIR / "error.log"
        with open(log_file, 'a') as f:
            f.write(log_entry)
        
        print(f"❌ ERROR: {message}")
    
    def validate_snippet(self, file_path: Path) -> dict:
        """Validate snippet code"""
        self.log_console(f"Validating snippet: {file_path.name}")
        
        result = {
            'valid': False,
            'language': None,
            'errors': [],
            'functions': [],
            'imports': []
        }
        
        suffix = file_path.suffix.lower()
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Python validation
            if suffix == '.py': 
                result['language'] = 'python'
                try:
                    import ast
                    tree = ast.parse(content)
                    result['valid'] = True
                    
                    # Extract functions
                    for node in ast.walk(tree):
                        if isinstance(node, ast.FunctionDef):
                            result['functions'].append(node.name)
                        elif isinstance(node, (ast.Import, ast.ImportFrom)):
                            if isinstance(node, ast.Import):
                                for alias in node.names:
                                    result['imports'].append(alias.name)
                            else:
                                result['imports'].append(node.module)
                
                except SyntaxError as e:
                    result['errors'].append(f"Line {e.lineno}: {e.msg}")
            
            # JavaScript
            elif suffix in ['.js', '.jsx']: 
                result['language'] = 'javascript'
                if content.strip():
                    result['valid'] = True
                    # Basic function extraction (regex)
                    import re
                    func_pattern = r'function\s+(\w+)'
                    result['functions'] = re.findall(func_pattern, content)
            
            # Shell scripts
            elif suffix in ['.sh', '.bash']: 
                result['language'] = 'bash'
                if content. strip():
                    result['valid'] = True
            
            # Other languages
            else:
                result['language'] = 'unknown'
                result['valid'] = True if content.strip() else False
            
            return result
            
        except Exception as e:
            self.log_error(f"Validation failed:  {e}")
            result['errors'].append(str(e))
            return result
    
    def create_metadata(self, file_path: Path, validation:  dict) -> bool:
        """Create metadata for snippet"""
        self.log_console(f"Creating metadata for:  {file_path.name}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f. read()
            
            # Generate hash
            file_hash = hashlib.md5(content.encode()).hexdigest()
            
            metadata = {
                'filename': file_path.name,
                'created': datetime.now().isoformat(),
                'language': validation['language'],
                'valid': validation['valid'],
                'functions': validation['functions'],
                'imports': validation['imports'],
                'hash': file_hash,
                'source': 'unknown',  # Will be populated if from playground
                'tags': [],
                'notes': ''
            }
            
            meta_file = self.metadata_dir / f"{file_path.stem}.json"
            with open(meta_file, 'w') as f:
                json.dump(metadata, f, indent=2)
            
            self.log_console(f"Metadata created: {meta_file.name}")
            return True
            
        except Exception as e:
            self.log_error(f"Failed to create metadata: {e}")
            return False
    
    def process_snippet(self, file_path: Path) -> bool:
        """Process a code snippet"""
        self.log_console(f"Processing snippet: {file_path.name}")
        
        # Validate
        validation = self. validate_snippet(file_path)
        
        if not validation['valid']:
            self.log_error(f"Invalid snippet: {', '.join(validation['errors'])}")
            return False
        
        # Create metadata
        if not self.create_metadata(file_path, validation):
            return False
        
        # Copy to snippets directory
        dest_path = self.module_dir / file_path.name
        try:
            import shutil
            shutil.copy2(file_path, dest_path)
            self.log_console(f"Snippet saved:  {file_path.name}")
            return True
        except Exception as e:
            self.log_error(f"Failed to save snippet: {e}")
            return False
    
    def list_snippets(self):
        """List all snippets with metadata"""
        self.log_console("Listing snippets")
        
        snippets = []
        for meta_file in self.metadata_dir. glob("*.json"):
            try:
                with open(meta_file, 'r') as f:
                    meta = json.load(f)
                snippets.append(meta)
            except Exception as e:
                self.log_error(f"Failed to read metadata: {e}")
        
        if not snippets:
            print("\n📦 CODE_SNIPPETS is empty\n")
            return
        
        print(f"\n📦 CODE_SNIPPETS contains {len(snippets)} snippet(s):\n")
        
        for snippet in sorted(snippets, key=lambda x: x['created'], reverse=True):
            print(f"  📄 {snippet['filename']}")
            print(f"     Language: {snippet['language']}")
            if snippet['functions']:
                print(f"     Functions: {', '.join(snippet['functions'][:3])}")
            print(f"     Created: {snippet['created'][: 10]}")
            print()


def main():
    """Main entry point"""
    processor = CodeSnippetsProcessor()
    
    try:
        processor.list_snippets()
        close_out("CODE_SNIPPETS_Processor.py", "SUCCESS")
    except Exception as e: 
        processor.log_error(f"Fatal error: {e}")
        close_out("CODE_SNIPPETS_Processor.py", "FAILURE")
        sys.exit(1)


if __name__ == "__main__":
    main()