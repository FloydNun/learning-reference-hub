#!/usr/bin/env python3
"""
🛸 COUNTERBALANCE - Code Artifact Extractor
Extracts code blocks and artifacts from ANY file type
- Extracts from:  PDFs, web grabs, chats, docs, images (via OCR)
- Detects code by patterns (indentation, syntax, keywords)
- Preserves language identification
- Outputs individual code files
"""

import sys
import os
from pathlib import Path
from datetime import datetime
import re
from typing import List, Dict, Tuple

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from Import_Header_Include import log_header, get_runtime, DEBUG
from Import_Footer_Include import log_footer, close_out
from Import_Globals_Include import *


class CodeArtifactExtractor: 
    """Extracts code artifacts from any file type"""
    
    def __init__(self):
        self.script_name = "code_artifact_extractor.py"
        self.output_dir = ROOT_DIR / "CODE_REFINERY" / "extracted_code"
        self.output_dir. mkdir(parents=True, exist_ok=True)
        
        log_header(self.script_name, "Code Artifact Extractor initialized")
        
        # Code detection patterns
        self.language_patterns = {
            'python': [
                r'def\s+\w+\s*\(',
                r'class\s+\w+\s*[:\(]',
                r'import\s+\w+',
                r'from\s+\w+\s+import',
            ],
            'javascript': [
                r'function\s+\w+\s*\(',
                r'const\s+\w+\s*=',
                r'let\s+\w+\s*=',
                r'=>',
                r'console\.log',
            ],
            'java': [
                r'public\s+class',
                r'private\s+\w+',
                r'System\.out\.println',
            ],
            'bash': [
                r'#!/bin/(bash|sh)',
                r'\$\w+',
                r'echo\s+',
            ],
            'sql': [
                r'SELECT\s+',
                r'FROM\s+\w+',
                r'WHERE\s+',
                r'INSERT\s+INTO',
            ],
            'html': [
                r'<html',
                r'<div',
                r'<script',
            ],
            'css': [
                r'\.\w+\s*\{',
                r'#\w+\s*\{',
                r':\s*\w+;',
            ]
        }
    
    def log_console(self, message:  str):
        """Log to console.log"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [CONSOLE] [{self.script_name}] {message}\n"
        
        log_file = LOGS_DIR / "console. log"
        with open(log_file, 'a') as f:
            f.write(log_entry)
        
        if DEBUG:
            print(f"🔍 CODE_EXTRACT: {message}")
    
    def extract_from_markdown(self, content: str) -> List[Dict]:
        """Extract code blocks from Markdown (```language ...  ```)"""
        pattern = r'```(\w+)?\n(.*?)```'
        matches = re.findall(pattern, content, re.DOTALL)
        
        code_blocks = []
        for i, (language, code) in enumerate(matches, 1):
            code_blocks.append({
                'index': i,
                'language':  language or self.detect_language(code),
                'code': code. strip(),
                'source': 'markdown'
            })
        
        return code_blocks
    
    def extract_from_text(self, content: str) -> List[Dict]:
        """Extract code-like blocks from plain text"""
        # Split by blank lines
        blocks = re.split(r'\n\s*\n', content)
        
        code_blocks = []
        for i, block in enumerate(blocks, 1):
            if self. looks_like_code(block):
                language = self.detect_language(block)
                code_blocks.append({
                    'index': i,
                    'language': language,
                    'code': block. strip(),
                    'source':  'text_detection'
                })
        
        return code_blocks
    
    def looks_like_code(self, text: str) -> bool:
        """Heuristic to detect if text looks like code"""
        lines = text.split('\n')
        
        # Check for code indicators
        indicators = 0
        
        # 1. Multiple lines with consistent indentation
        indented = sum(1 for line in lines if line.startswith((' ', '\t')))
        if indented > len(lines) * 0.3:  # 30% of lines indented
            indicators += 1
        
        # 2. Contains special characters common in code
        special_chars = ['{', '}', '(', ')', '[', ']', ';', '=', '==', '!=']
        if any(char in text for char in special_chars):
            indicators += 1
        
        # 3. Contains language keywords
        if self.detect_language(text) != 'unknown':
            indicators += 1
        
        # 4. Has < 10% of text as natural language words
        words = re.findall(r'\b[a-zA-Z]{4,}\b', text)
        if len(words) < len(text. split()) * 0.1:
            indicators += 1
        
        return indicators >= 2
    
    def detect_language(self, code: str) -> str:
        """Detect programming language from code content"""
        scores = {}
        
        for language, patterns in self.language_patterns.items():
            score = 0
            for pattern in patterns:
                if re.search(pattern, code, re. IGNORECASE | re.MULTILINE):
                    score += 1
            scores[language] = score
        
        if scores:
            best_match = max(scores. items(), key=lambda x: x[1])
            if best_match[1] > 0:
                return best_match[0]
        
        return 'unknown'
    
    def extract_from_file(self, file_path: Path) -> List[Dict]:
        """Extract code artifacts from any file"""
        self.log_console(f"Extracting code from: {file_path.name}")
        
        try: 
            # Read file content
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Try markdown extraction first
            code_blocks = self. extract_from_markdown(content)
            
            # If no markdown blocks, try text detection
            if not code_blocks: 
                code_blocks = self. extract_from_text(content)
            
            self.log_console(f"Found {len(code_blocks)} code artifact(s)")
            return code_blocks
            
        except Exception as e:
            self.log_console(f"Extraction failed: {e}")
            return []
    
    def save_artifacts(self, file_path: Path, artifacts: List[Dict]) -> List[Path]:
        """Save extracted code artifacts as separate files"""
        if not artifacts:
            return []
        
        # Create subdirectory for this source file
        source_dir = self.output_dir / file_path.stem
        source_dir.mkdir(exist_ok=True)
        
        saved_files = []
        
        for artifact in artifacts:
            # Determine file extension
            ext_map = {
                'python': '.py',
                'javascript': '.js',
                'java': '.java',
                'bash': '.sh',
                'sql': '.sql',
                'html': '.html',
                'css': '.css',
                'unknown': '. txt'
            }
            ext = ext_map.get(artifact['language'], '.txt')
            
            # Create filename
            filename = f"artifact_{artifact['index']: 02d}_{artifact['language']}{ext}"
            output_path = source_dir / filename
            
            try:
                with open(output_path, 'w', encoding='utf-8') as f:
                    f. write(f"# Extracted from:  {file_path.name}\n")
                    f.write(f"# Language: {artifact['language']}\n")
                    f.write(f"# Index: {artifact['index']}\n")
                    f.write(f"# Source: {artifact['source']}\n\n")
                    f.write(artifact['code'])
                
                saved_files.append(output_path)
                self.log_console(f"Saved artifact: {filename}")
                
            except Exception as e:
                self.log_console(f"Failed to save artifact {artifact['index']}: {e}")
        
        return saved_files
    
    def process_file(self, file_path: Path) -> bool:
        """Main processing:  extract and save artifacts"""
        self.log_console(f"Processing: {file_path.name}")
        
        artifacts = self.extract_from_file(file_path)
        
        if artifacts:
            saved = self.save_artifacts(file_path, artifacts)
            self.log_console(f"Saved {len(saved)} artifact(s) from {file_path.name}")
            return True
        else:
            self.log_console(f"No code artifacts found in {file_path.name}")
            return False


# Example usage
if __name__ == "__main__":
    extractor = CodeArtifactExtractor()
    
    # Process a file
    # extractor.process_file(Path("chat_transcript.md"))
    # extractor.process_file(Path("document.txt"))
    
    print("Code Artifact Extractor ready. Import and use in your processors.")