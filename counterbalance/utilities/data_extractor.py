#!/usr/bin/env python3
"""
🛸 COUNTERBALANCE - Data Extractor
Extracts specific data from structured files without altering originals
- JSON field extraction with filters
- XML/HTML content extraction
- CSV filtering by columns/conditions
- Date range filtering
- Keyword matching
- Outputs to MD or TXT
"""

import sys
import os
from pathlib import Path
from datetime import datetime
import json
import csv
import re
from typing import List, Dict, Any, Optional

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from Import_Header_Include import log_header, get_runtime, DEBUG
from Import_Footer_Include import log_footer, close_out
from Import_Globals_Include import *


class DataExtractor:
    """Extracts and filters data from structured files"""
    
    def __init__(self):
        self.script_name = "data_extractor. py"
        self.output_dir = ROOT_DIR / "CODE_REFINERY" / "extracted_data"
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        log_header(self.script_name, "Data Extractor initialized")
    
    def log_console(self, message: str):
        """Log to console. log"""
        timestamp = datetime. now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [CONSOLE] [{self.script_name}] {message}\n"
        
        log_file = LOGS_DIR / "console.log"
        with open(log_file, 'a') as f:
            f.write(log_entry)
        
        if DEBUG:
            print(f"🔬 EXTRACT: {message}")
    
    def extract_json_fields(self, json_path: Path, field_paths: List[str], 
                           filters: Dict = None) -> List[Dict]: 
        """
        Extract specific fields from JSON
        
        Args:
            json_path: Path to JSON file
            field_paths: List of dot-notation paths (e.g., ["user.name", "user.email"])
            filters: Dict of filter conditions (e.g., {"date": "2026-01", "keyword": "test"})
        
        Returns:
            List of extracted records
        """
        self.log_console(f"Extracting from JSON: {json_path.name}")
        
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Handle if data is a list of objects
            if isinstance(data, list):
                items = data
            elif isinstance(data, dict):
                # Try to find array in common locations
                items = (data.get('data') or 
                        data.get('items') or 
                        data. get('results') or 
                        [data])
            else:
                items = [data]
            
            extracted = []
            for item in items: 
                # Apply filters
                if filters:
                    if not self._matches_filters(item, filters):
                        continue
                
                # Extract fields
                record = {}
                for field_path in field_paths:
                    value = self._get_nested_value(item, field_path)
                    record[field_path] = value
                
                extracted.append(record)
            
            self.log_console(f"Extracted {len(extracted)} records from {len(items)} total")
            return extracted
            
        except Exception as e:
            self.log_console(f"JSON extraction failed: {e}")
            return []
    
    def _get_nested_value(self, obj: Dict, path: str) -> Any:
        """Get value from nested dict using dot notation"""
        keys = path.split('.')
        value = obj
        
        for key in keys:
            if isinstance(value, dict):
                value = value.get(key)
            elif isinstance(value, list) and key. isdigit():
                idx = int(key)
                value = value[idx] if idx < len(value) else None
            else:
                return None
            
            if value is None:
                return None
        
        return value
    
    def _matches_filters(self, item: Dict, filters: Dict) -> bool:
        """Check if item matches filter conditions"""
        # Keyword filter (search all text fields)
        if 'keyword' in filters:
            keyword = filters['keyword']. lower()
            item_text = json.dumps(item).lower()
            if keyword not in item_text: 
                return False
        
        # Date range filter
        if 'date_from' in filters or 'date_to' in filters:
            # Look for date fields
            date_value = (item.get('date') or 
                         item.get('created') or 
                         item.get('timestamp') or 
                         item. get('created_at'))
            
            if date_value:
                try:
                    if isinstance(date_value, str):
                        # Try to parse date
                        item_date = datetime.fromisoformat(date_value. replace('Z', '+00:00'))
                        
                        if 'date_from' in filters: 
                            from_date = datetime.fromisoformat(filters['date_from'])
                            if item_date < from_date:
                                return False
                        
                        if 'date_to' in filters:
                            to_date = datetime.fromisoformat(filters['date_to'])
                            if item_date > to_date:
                                return False
                except:
                    pass
        
        # Custom field filters
        for key, value in filters.items():
            if key not in ['keyword', 'date_from', 'date_to']: 
                if self._get_nested_value(item, key) != value:
                    return False
        
        return True
    
    def extract_html_content(self, html_path: Path, selectors: List[str] = None) -> str:
        """
        Extract text content from HTML
        
        Args:
            html_path: Path to HTML file
            selectors:  CSS selectors to extract (e.g., [".user-content", "#main"])
        
        Returns:
            Extracted text content
        """
        self.log_console(f"Extracting from HTML: {html_path.name}")
        
        try: 
            from bs4 import BeautifulSoup
            
            with open(html_path, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f. read(), 'html.parser')
            
            if selectors:
                # Extract specific elements
                content_parts = []
                for selector in selectors:
                    elements = soup.select(selector)
                    for elem in elements:
                        content_parts.append(elem.get_text(strip=True))
                content = '\n\n'.join(content_parts)
            else:
                # Extract all text
                content = soup.get_text(separator='\n', strip=True)
            
            self.log_console(f"Extracted {len(content)} characters")
            return content
            
        except ImportError:
            self.log_console("BeautifulSoup not installed.  Install:  pip install beautifulsoup4")
            return ""
        except Exception as e:
            self.log_console(f"HTML extraction failed: {e}")
            return ""
    
    def extract_csv_filtered(self, csv_path: Path, columns: List[str] = None,
                            filters: Dict = None) -> List[Dict]:
        """
        Extract filtered rows from CSV
        
        Args: 
            csv_path: Path to CSV file
            columns:  Columns to extract (None = all)
            filters: Dict of column: value filters
        
        Returns: 
            List of extracted rows
        """
        self.log_console(f"Extracting from CSV: {csv_path. name}")
        
        try: 
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                
                extracted = []
                for row in reader:
                    # Apply filters
                    if filters:
                        matches = all(
                            row.get(col, '').lower().find(val.lower()) >= 0 
                            for col, val in filters.items()
                        )
                        if not matches:
                            continue
                    
                    # Extract columns
                    if columns:
                        record = {col: row. get(col, '') for col in columns}
                    else:
                        record = row
                    
                    extracted.append(record)
            
            self.log_console(f"Extracted {len(extracted)} rows")
            return extracted
            
        except Exception as e:
            self.log_console(f"CSV extraction failed: {e}")
            return []
    
    def save_as_markdown(self, data: Any, output_name: str, title: str = None):
        """Save extracted data as Markdown"""
        output_path = self.output_dir / f"{output_name}.md"
        
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                # Header
                if title:
                    f.write(f"# {title}\n\n")
                
                f.write(f"*Extracted:  {datetime.now().isoformat()}*\n\n")
                f.write("---\n\n")
                
                # Content
                if isinstance(data, list):
                    for i, item in enumerate(data, 1):
                        f.write(f"## Record {i}\n\n")
                        if isinstance(item, dict):
                            for key, value in item. items():
                                f.write(f"**{key}:** {value}\n\n")
                        else:
                            f.write(f"{item}\n\n")
                        f.write("---\n\n")
                elif isinstance(data, str):
                    f.write(data)
                else:
                    f.write(str(data))
            
            self.log_console(f"Saved as Markdown:  {output_path.name}")
            return output_path
            
        except Exception as e:
            self.log_console(f"Failed to save Markdown: {e}")
            return None
    
    def save_as_text(self, data: Any, output_name: str):
        """Save extracted data as plain text"""
        output_path = self.output_dir / f"{output_name}.txt"
        
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                if isinstance(data, list):
                    for item in data:
                        if isinstance(item, dict):
                            f.write(json.dumps(item, indent=2))
                        else:
                            f.write(str(item))
                        f.write('\n\n---\n\n')
                elif isinstance(data, str):
                    f.write(data)
                else:
                    f. write(str(data))
            
            self.log_console(f"Saved as text: {output_path.name}")
            return output_path
            
        except Exception as e: 
            self.log_console(f"Failed to save text: {e}")
            return None


# Example usage
if __name__ == "__main__":
    extractor = DataExtractor()
    
    # Example 1: Extract from JSON with filters
    # data = extractor.extract_json_fields(
    #     Path("data.json"),
    #     field_paths=["user.name", "user.email", "content"],
    #     filters={"keyword": "important", "date_from": "2026-01-01"}
    # )
    # extractor.save_as_markdown(data, "filtered_users", "Filtered User Data")
    
    # Example 2: Extract HTML content
    # content = extractor.extract_html_content(
    #     Path("page.html"),
    #     selectors=[".article-content", ".user-comment"]
    # )
    # extractor.save_as_text(content, "extracted_content")
    
    print("Data Extractor ready.  Import and use in your scripts.")