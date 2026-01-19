#!/usr/bin/env python3
"""
🛸 COUNTERBALANCE - DOCS_INBOX Processor
Manages documents with OCR for images and PDFs
- Deduplicates by hash + filename
- OCR for images (png, jpg, jpeg, gif)
- OCR for PDFs
- Indexes searchable content
- Processes to DOCS_PROCESSED, IMAGES_PROCESSED, PDFs_PROCESSED
"""

import sys
import os
from pathlib import Path
from datetime import datetime
import json
import hashlib
import shutil

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from Import_Header_Include import log_header, get_runtime, DEBUG
from Import_Footer_Include import log_footer, close_out
from Import_Globals_Include import *


class DocsInboxProcessor:
    """Processor for DOCS_INBOX module"""
    
    def __init__(self):
        self.script_name = "DOCS_INBOX_Processor. py"
        self.inbox_dir = Path(__file__).parent
        self.processed_dirs = {
            'docs': ROOT_DIR / "DOCS_PROCESSED",
            'images': ROOT_DIR / "IMAGES_PROCESSED",
            'images_ocr': ROOT_DIR / "IMAGES_OCR_DONE",
            'pdfs':  ROOT_DIR / "PDFs_PROCESSED",
            'pdfs_ocr': ROOT_DIR / "PDFs_OCR_DONE"
        }
        self.index_dir = self.inbox_dir / ". index"
        self.hashes_file = self.index_dir / "file_hashes.json"
        
        # Create directories
        for dir_path in self.processed_dirs.values():
            dir_path.mkdir(parents=True, exist_ok=True)
        self.index_dir.mkdir(exist_ok=True)
        
        # Load existing hashes
        self.file_hashes = self.load_hashes()
        
        log_header(self. script_name, "DOCS_INBOX Processor initialized")
    
    def log_console(self, message: str):
        """Log to console.log"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [CONSOLE] [{self.script_name}] {message}\n"
        
        log_file = LOGS_DIR / "console.log"
        with open(log_file, 'a') as f:
            f.write(log_entry)
        
        if DEBUG:
            print(f"📄 DOCS: {message}")
    
    def log_error(self, message: str):
        """Log to error.log"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [ERROR] [{self.script_name}] {message}\n"
        
        log_file = LOGS_DIR / "error.log"
        with open(log_file, 'a') as f:
            f.write(log_entry)
        
        print(f"❌ ERROR: {message}")
    
    def load_hashes(self) -> dict:
        """Load existing file hashes"""
        if self.hashes_file.exists():
            try:
                with open(self.hashes_file, 'r') as f:
                    return json.load(f)
            except Exception as e: 
                self.log_error(f"Failed to load hashes:  {e}")
                return {}
        return {}
    
    def save_hashes(self):
        """Save file hashes"""
        try: 
            with open(self.hashes_file, 'w') as f:
                json.dump(self.file_hashes, f, indent=2)
        except Exception as e:
            self.log_error(f"Failed to save hashes: {e}")
    
    def calculate_hash(self, file_path: Path) -> str:
        """Calculate MD5 hash of file"""
        md5 = hashlib.md5()
        try:
            with open(file_path, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    md5.update(chunk)
            return md5.hexdigest()
        except Exception as e:
            self. log_error(f"Hash calculation failed: {e}")
            return None
    
    def is_duplicate(self, file_path: Path, file_hash: str) -> bool:
        """Check if file is duplicate by hash + filename"""
        filename = file_path.name
        
        # Check hash
        if file_hash in self.file_hashes. values():
            self.log_console(f"Duplicate by hash: {filename}")
            return True
        
        # Check filename
        if filename in self.file_hashes.keys():
            self.log_console(f"Duplicate by filename:  {filename}")
            return True
        
        return False
    
    def ocr_image(self, image_path: Path) -> dict:
        """Perform OCR on image"""
        self.log_console(f"OCR processing: {image_path.name}")
        
        result = {
            'success': False,
            'text': '',
            'error': None
        }
        
        try:
            # Try to import OCR library
            try:
                import pytesseract
                from PIL import Image
            except ImportError:
                result['error'] = "pytesseract or PIL not installed"
                self.log_error("OCR libraries not available.  Install:  pip install pytesseract pillow")
                return result
            
            # Perform OCR
            image = Image.open(image_path)
            text = pytesseract.image_to_string(image)
            
            result['success'] = True
            result['text'] = text. strip()
            self.log_console(f"OCR extracted {len(result['text'])} characters")
            
        except Exception as e: 
            result['error'] = str(e)
            self.log_error(f"OCR failed:  {e}")
        
        return result
    
    def ocr_pdf(self, pdf_path: Path) -> dict:
        """Perform OCR on PDF"""
        self.log_console(f"PDF OCR processing: {pdf_path.name}")
        
        result = {
            'success': False,
            'text': '',
            'pages': 0,
            'error': None
        }
        
        try:
            # Try to import PDF libraries
            try:
                import PyPDF2
                import pytesseract
                from pdf2image import convert_from_path
                from PIL import Image
            except ImportError:
                result['error'] = "PDF/OCR libraries not installed"
                self.log_error("PDF OCR libraries not available. Install: pip install PyPDF2 pdf2image pytesseract pillow")
                return result
            
            # First try text extraction
            with open(pdf_path, 'rb') as f:
                pdf_reader = PyPDF2.PdfReader(f)
                result['pages'] = len(pdf_reader.pages)
                
                text_parts = []
                for page in pdf_reader.pages:
                    page_text = page.extract_text()
                    if page_text. strip():
                        text_parts.append(page_text)
                
                # If text extraction worked, use it
                if text_parts: 
                    result['text'] = '\n\n'.join(text_parts)
                    result['success'] = True
                    self.log_console(f"PDF text extracted:  {len(result['text'])} characters")
                    return result
            
            # If no text, try OCR on images
            self.log_console("PDF has no text, attempting OCR...")
            images = convert_from_path(pdf_path)
            
            text_parts = []
            for i, image in enumerate(images):
                page_text = pytesseract.image_to_string(image)
                if page_text.strip():
                    text_parts.append(page_text)
                self.log_console(f"OCR page {i+1}/{len(images)}")
            
            result['text'] = '\n\n'.join(text_parts)
            result['success'] = True
            self.log_console(f"PDF OCR extracted {len(result['text'])} characters")
            
        except Exception as e:
            result['error'] = str(e)
            self.log_error(f"PDF OCR failed: {e}")
        
        return result
    
    def save_ocr_result(self, original_path: Path, ocr_text: str, destination: str):
        """Save OCR text to file"""
        ocr_dir = self.processed_dirs[destination]
        ocr_file = ocr_dir / f"{original_path.stem}.txt"
        
        try:
            with open(ocr_file, 'w', encoding='utf-8') as f:
                f.write(f"# OCR Result from:  {original_path.name}\n")
                f.write(f"# Processed: {datetime.now().isoformat()}\n\n")
                f.write(ocr_text)
            
            self.log_console(f"OCR saved:  {ocr_file.name}")
            return True
        except Exception as e:
            self.log_error(f"Failed to save OCR:  {e}")
            return False
    
    def create_searchable_index(self, file_path: Path, content: str, file_type: str):
        """Create searchable index entry"""
        index_entry = {
            'filename': file_path.name,
            'type': file_type,
            'indexed_at': datetime.now().isoformat(),
            'content': content,
            'hash': self.calculate_hash(file_path),
            'size': file_path.stat().st_size
        }
        
        index_file = self.index_dir / f"{file_path.stem}.json"
        try:
            with open(index_file, 'w') as f:
                json.dump(index_entry, f, indent=2)
            self.log_console(f"Index created: {index_file.name}")
            return True
        except Exception as e:
            self.log_error(f"Failed to create index: {e}")
            return False
    
    def process_image(self, file_path: Path) -> bool:
        """Process image file with OCR"""
        self.log_console(f"Processing image:  {file_path.name}")
        
        # Calculate hash
        file_hash = self.calculate_hash(file_path)
        if not file_hash:
            return False
        
        # Check duplicate
        if self.is_duplicate(file_path, file_hash):
            self.log_console(f"Skipping duplicate: {file_path. name}")
            return False
        
        # Perform OCR
        ocr_result = self.ocr_image(file_path)
        
        # Copy to IMAGES_PROCESSED
        dest_path = self.processed_dirs['images'] / file_path.name
        try:
            shutil.copy2(file_path, dest_path)
            self.log_console(f"Image copied to IMAGES_PROCESSED")
        except Exception as e:
            self.log_error(f"Failed to copy image: {e}")
            return False
        
        # If OCR successful, save result
        if ocr_result['success'] and ocr_result['text']: 
            self.save_ocr_result(file_path, ocr_result['text'], 'images_ocr')
            self.create_searchable_index(file_path, ocr_result['text'], 'image')
        else:
            self.log_console(f"No text extracted from image (may be blank or OCR unavailable)")
        
        # Record hash
        self.file_hashes[file_path.name] = file_hash
        self.save_hashes()
        
        return True
    
    def process_pdf(self, file_path: Path) -> bool:
        """Process PDF file with OCR"""
        self.log_console(f"Processing PDF: {file_path.name}")
        
        # Calculate hash
        file_hash = self.calculate_hash(file_path)
        if not file_hash:
            return False
        
        # Check duplicate
        if self.is_duplicate(file_path, file_hash):
            self.log_console(f"Skipping duplicate:  {file_path.name}")
            return False
        
        # Perform OCR/text extraction
        ocr_result = self.ocr_pdf(file_path)
        
        # Copy to PDFs_PROCESSED
        dest_path = self.processed_dirs['pdfs'] / file_path. name
        try:
            shutil.copy2(file_path, dest_path)
            self.log_console(f"PDF copied to PDFs_PROCESSED")
        except Exception as e: 
            self.log_error(f"Failed to copy PDF: {e}")
            return False
        
        # If text extracted, save result
        if ocr_result['success'] and ocr_result['text']:
            self.save_ocr_result(file_path, ocr_result['text'], 'pdfs_ocr')
            self.create_searchable_index(file_path, ocr_result['text'], 'pdf')
        else:
            self.log_console(f"No text extracted from PDF")
        
        # Record hash
        self.file_hashes[file_path.name] = file_hash
        self.save_hashes()
        
        return True
    
    def process_document(self, file_path:  Path) -> bool:
        """Process text document"""
        self.log_console(f"Processing document: {file_path.name}")
        
        # Calculate hash
        file_hash = self.calculate_hash(file_path)
        if not file_hash:
            return False
        
        # Check duplicate
        if self.is_duplicate(file_path, file_hash):
            self.log_console(f"Skipping duplicate: {file_path.name}")
            return False
        
        # Read content
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            self.log_error(f"Failed to read document: {e}")
            return False
        
        # Copy to DOCS_PROCESSED
        dest_path = self.processed_dirs['docs'] / file_path.name
        try:
            shutil.copy2(file_path, dest_path)
            self.log_console(f"Document copied to DOCS_PROCESSED")
        except Exception as e: 
            self.log_error(f"Failed to copy document: {e}")
            return False
        
        # Create searchable index
        self.create_searchable_index(file_path, content, 'document')
        
        # Record hash
        self.file_hashes[file_path.name] = file_hash
        self.save_hashes()
        
        return True
    
    def process_file(self, file_path: Path) -> bool:
        """Route file to appropriate processor"""
        suffix = file_path.suffix.lower()
        
        # Images
        if suffix in ['.png', '.jpg', '.jpeg', '. gif', '.bmp', '.tiff']: 
            return self.process_image(file_path)
        
        # PDFs
        elif suffix == '.pdf':
            return self. process_pdf(file_path)
        
        # Documents
        elif suffix in ['.txt', '.md', '. doc', '.docx']:
            return self.process_document(file_path)
        
        else:
            self.log_console(f"Unknown file type: {suffix}")
            return False
    
    def scan_inbox(self):
        """Scan and process DOCS_INBOX"""
        self.log_console("Scanning DOCS_INBOX")
        
        files = [f for f in self.inbox_dir.iterdir() 
                if f.is_file() 
                and f.name != 'README.md'
                and not f.name.startswith('.')]
        
        if not files:
            print("\n📄 DOCS_INBOX is empty\n")
            return
        
        print(f"\n📄 DOCS_INBOX contains {len(files)} file(s):\n")
        
        for file_path in files:
            print(f"  Processing: {file_path.name}")
            success = self.process_file(file_path)
            if success: 
                print(f"    ✅ Processed successfully")
            else:
                print(f"    ❌ Failed to process")
        
        print(f"\nTotal files indexed: {len(self.file_hashes)}\n")


def main():
    """Main entry point"""
    processor = DocsInboxProcessor()
    
    try:
        processor.scan_inbox()
        close_out("DOCS_INBOX_Processor. py", "SUCCESS")
    except Exception as e: 
        processor.log_error(f"Fatal error: {e}")
        close_out("DOCS_INBOX_Processor.py", "FAILURE")
        sys.exit(1)


if __name__ == "__main__": 
    main()