#!/usr/bin/env python3
"""
🛸 COUNTERBALANCE - CHATS Processor
Archives AI chat conversations with indexing and code extraction
- Stores chat markdown files
- Extracts code blocks
- Indexes by date and topic
- Links to reference pages
"""

import sys
import os
from pathlib import Path
from datetime import datetime
import json
import re
import shutil

# Add parent directories to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from Import_Header_Include import log_header, get_runtime, DEBUG
from Import_Footer_Include import log_footer, close_out
from Import_Globals_Include import *


class ChatsProcessor:
    """Processor for CHATS module"""
    
    def __init__(self):
        self.script_name = "CHATS_Processor. py"
        self.module_dir = Path(__file__).parent
        self.code_blocks_dir = self.module_dir / "code_blocks"
        self.metadata_dir = self.module_dir / ".metadata"
        
        # Create directories
        self. code_blocks_dir.mkdir(exist_ok=True)
        self.metadata_dir.mkdir(exist_ok=True)
        
        log_header(self. script_name, "CHATS Processor initialized")
    
    def log_console(self, message: str):
        """Log to console.log"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [CONSOLE] [{self.script_name}] {message}\n"
        
        log_file = LOGS_DIR / "console.log"
        with open(log_file, 'a') as f:
            f.write(log_entry)
        
        if DEBUG:
            print(f"💬 CHATS: {message}")
    
    def log_error(self, message: str):
        """Log to error.log"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [ERROR] [{self.script_name}] {message}\n"
        
        log_file = LOGS_DIR / "error.log"
        with open(log_file, 'a') as f:
            f.write(log_entry)
        
        print(f"❌ ERROR: {message}")
    
    def extract_code_blocks(self, content: str) -> list:
        """Extract code blocks from markdown"""
        pattern = r'```(\w+)?\n(.*?)```'
        matches = re.findall(pattern, content, re.DOTALL)
        
        code_blocks = []
        for language, code in matches:
            code_blocks.append({
                'language': language or 'text',
                'code': code. strip()
            })
        
        return code_blocks
    
    def analyze_chat(self, file_path: Path) -> dict:
        """Analyze chat content"""
        self.log_console(f"Analyzing chat: {file_path.name}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f. read()
            
            # Extract code blocks
            code_blocks = self.extract_code_blocks(content)
            
            # Extract title (first # heading)
            title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            title = title_match.group(1) if title_match else file_path.stem
            
            # Extract topics (look for keywords)
            topics = []
            topic_keywords = ['git', 'react', 'python', 'javascript', 'docker', 'firebase', 'jupyter']
            content_lower = content.lower()
            for keyword in topic_keywords:
                if keyword in content_lower: 
                    topics.append(keyword)
            
            metadata = {
                'filename': file_path.name,
                'title': title,
                'created':  datetime.now().isoformat(),
                'code_blocks': len(code_blocks),
                'topics': topics,
                'size': len(content),
                'lines': content.count('\n') + 1
            }
            
            return {
                'metadata': metadata,
                'code_blocks': code_blocks
            }
            
        except Exception as e:
            self.log_error(f"Analysis failed: {e}")
            return None
    
    def save_code_blocks(self, chat_stem: str, code_blocks: list) -> bool:
        """Save extracted code blocks"""
        if not code_blocks:
            return True
        
        self.log_console(f"Saving {len(code_blocks)} code block(s) from: {chat_stem}")
        
        blocks_dir = self.code_blocks_dir / chat_stem
        blocks_dir.mkdir(exist_ok=True)
        
        try:
            for i, block in enumerate(code_blocks, 1):
                ext = {
                    'python': '.py',
                    'javascript': '.js',
                    'bash': '.sh',
                    'html': '.html',
                    'css': '.css',
                    'json': '.json'
                }.get(block['language'], '.txt')
                
                block_file = blocks_dir / f"block_{i: 02d}{ext}"
                with open(block_file, 'w', encoding='utf-8') as f:
                    f.write(block['code'])
            
            self.log_console(f"Code blocks saved to: {blocks_dir. name}")
            return True
            
        except Exception as e: 
            self.log_error(f"Failed to save code blocks: {e}")
            return False
    
    def process_chat(self, file_path: Path) -> bool:
        """Process a chat file"""
        self.log_console(f"Processing chat: {file_path.name}")
        
        # Analyze
        analysis = self.analyze_chat(file_path)
        if not analysis: 
            return False
        
        # Save code blocks
        if not self.save_code_blocks(file_path.stem, analysis['code_blocks']):
            return False
        
        # Save metadata
        meta_file = self.metadata_dir / f"{file_path.stem}.json"
        try:
            with open(meta_file, 'w') as f:
                json.dump(analysis['metadata'], f, indent=2)
            self.log_console(f"Metadata saved:  {meta_file.name}")
        except Exception as e:
            self.log_error(f"Failed to save metadata: {e}")
            return False
        
        # Copy to chats directory
        dest_path = self.module_dir / file_path.name
        try:
            shutil.copy2(file_path, dest_path)
            self.log_console(f"Chat archived: {file_path.name}")
            return True
        except Exception as e:
            self.log_error(f"Failed to copy chat: {e}")
            return False
    
    def list_chats(self):
        """List all archived chats"""
        self.log_console("Listing chats")
        
        chats = []
        for meta_file in self.metadata_dir.glob("*.json"):
            try:
                with open(meta_file, 'r') as f:
                    chat = json.load(f)
                chats.append(chat)
            except Exception as e:
                self.log_error(f"Failed to read metadata: {e}")
        
        if not chats:
            print("\n💬 CHATS is empty\n")
            return
        
        print(f"\n💬 CHATS contains {len(chats)} conversation(s):\n")
        
        for chat in sorted(chats, key=lambda x: x['created'], reverse=True):
            print(f"  📝 {chat['title']}")
            print(f"     File: {chat['filename']}")
            print(f"     Code blocks: {chat['code_blocks']}")
            if chat['topics']:
                print(f"     Topics: {', '. join(chat['topics'])}")
            print(f"     Created: {chat['created'][: 10]}")
            print()


def main():
    """Main entry point"""
    processor = ChatsProcessor()
    
    try:
        processor.list_chats()
        close_out("CHATS_Processor.py", "SUCCESS")
    except Exception as e:
        processor.log_error(f"Fatal error:  {e}")
        close_out("CHATS_Processor. py", "FAILURE")
        sys.exit(1)


if __name__ == "__main__": 
    main()