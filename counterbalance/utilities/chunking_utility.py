#!/usr/bin/env python3
"""
🛸 COUNTERBALANCE - Chunking Utility
Breaks large files into manageable chunks
- Size-based chunking
- Semantic chunking (by headers, paragraphs)
- Preserves context
- Outputs numbered chunks
"""

import sys
from pathlib import Path
from datetime import datetime
from typing import List, Dict

sys.path.insert(0, str(Path(__file__).parent.parent))

from Import_Header_Include import log_header, get_runtime, DEBUG
from Import_Footer_Include import log_footer, close_out
from Import_Globals_Include import *


class Chunker:
    """Chunks large files into manageable pieces"""
    
    def __init__(self, max_chunk_size: int = 50000):  # 50KB default
        self.max_chunk_size = max_chunk_size
        self.output_dir = ROOT_DIR / "CODE_REFINERY" / "chunked"
        self.output_dir. mkdir(parents=True, exist_ok=True)
    
    def chunk_by_size(self, content: str, overlap: int = 500) -> List[str]:
        """Chunk by size with overlap for context"""
        chunks = []
        start = 0
        
        while start < len(content):
            end = start + self.max_chunk_size
            chunk = content[start:end]
            chunks.append(chunk)
            start = end - overlap  # Overlap for context
        
        return chunks
    
    def chunk_by_headers(self, content: str) -> List[Dict]:
        """Chunk by markdown headers (semantic)"""
        import re
        
        # Find all headers
        header_pattern = r'^(#{1,6})\s+(.+)$'
        lines = content.split('\n')
        
        chunks = []
        current_chunk = []
        current_header = "Introduction"
        
        for line in lines:
            match = re.match(header_pattern, line)
            if match: 
                # Save previous chunk
                if current_chunk:
                    chunks.append({
                        'title': current_header,
                        'content': '\n'.join(current_chunk).strip()
                    })
                
                # Start new chunk
                current_header = match.group(2)
                current_chunk = [line]
            else:
                current_chunk.append(line)
        
        # Save last chunk
        if current_chunk: 
            chunks.append({
                'title': current_header,
                'content': '\n'.join(current_chunk).strip()
            })
        
        return chunks
    
    def save_chunks(self, file_path: Path, chunks: List, format: str = 'md'):
        """Save chunks as separate files"""
        chunk_dir = self.output_dir / file_path.stem
        chunk_dir.mkdir(exist_ok=True)
        
        for i, chunk in enumerate(chunks, 1):
            chunk_file = chunk_dir / f"chunk_{i: 03d}.{format}"
            
            with open(chunk_file, 'w', encoding='utf-8') as f:
                if isinstance(chunk, dict):
                    f.write(f"# {chunk['title']}\n\n")
                    f.write(chunk['content'])
                else:
                    f.write(chunk)
            
            print(f"Saved:  {chunk_file.name}")