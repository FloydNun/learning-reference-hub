#!/usr/bin/env python3
"""
🛸 COUNTERBALANCE - Dashboard Server
Central command center with auto-discovery of custom dashboards
- Main dashboard at /
- Auto-indexes custom dashboards in DASHBOARDS/
- Never breaks - experimental dashboards isolated
"""

import sys
import os
import http.server
import socketserver
import json
import webbrowser
from pathlib import Path
from urllib.parse import urlparse, parse_qs

from Import_Header_Include import log_header, get_runtime, DEBUG
from Import_Footer_Include import log_footer, close_out
from Import_Globals_Include import *

PORT = 8000


class DashboardHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler for dashboard requests"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT_DIR), **kwargs)
    
    def do_GET(self):
        """Handle GET requests"""
        parsed_path = urlparse(self.path)
        
        # API endpoints
        if parsed_path.path == '/api/status':
            self.send_json_response(self.get_system_status())
        elif parsed_path.path == '/api/inbox':
            self.send_json_response(self.get_inbox_status())
        elif parsed_path. path == '/api/modules':
            self.send_json_response(self.get_modules_status())
        elif parsed_path.path == '/api/search':
            query = parse_qs(parsed_path.query).get('q', [''])[0]
            self. send_json_response(self. search_content(query))
        elif parsed_path.path == '/api/dashboards':
            self.send_json_response(self.get_custom_dashboards())
        else:
            # Serve files normally
            super().do_GET()
    
    def send_json_response(self, data):
        """Send JSON response"""
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    def get_system_status(self):
        """Get overall system status"""
        return {
            'status': 'operational',
            'inbox_count': len(list(INBOX_DIR.glob('*'))) - 1,  # Exclude README
            'total_files': self.count_files(ROOT_DIR),
            'modules':  len(list(MODULES_DIR.iterdir())) if MODULES_DIR. exists() else 0
        }
    
    def get_inbox_status(self):
        """Get INBOX status"""
        files = [f for f in INBOX_DIR.iterdir() if f.is_file() and f.name != 'README. md']
        return {
            'count': len(files),
            'files': [{'name': f.name, 'size': f.stat().st_size} for f in files]
        }
    
    def get_modules_status(self):
        """Get modules status"""
        if not MODULES_DIR.exists():
            return {'modules': []}
        
        modules = []
        for module_dir in MODULES_DIR.iterdir():
            if module_dir.is_dir() and not module_dir.name.startswith('.'):
                file_count = len(list(module_dir.rglob('*')))
                modules.append({
                    'name': module_dir.name,
                    'files': file_count
                })
        
        return {'modules': modules}
    
    def search_content(self, query):
        """Search OCR'd content"""
        results = []
        
        # Search in OCR directories
        ocr_dirs = [
            ROOT_DIR / "IMAGES_OCR_DONE",
            ROOT_DIR / "PDFs_OCR_DONE"
        ]
        
        for ocr_dir in ocr_dirs:
            if ocr_dir.exists():
                for file_path in ocr_dir.rglob('*. txt'):
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        if query.lower() in content.lower():
                            results.append({
                                'file': file_path.name,
                                'path': str(file_path. relative_to(ROOT_DIR)),
                                'preview': self.get_preview(content, query)
                            })
                    except:
                        pass
        
        return {'results': results}
    
    def get_preview(self, content, query, context=100):
        """Get preview snippet with query highlighted"""
        pos = content.lower().find(query.lower())
        if pos == -1:
            return content[: 200]
        
        start = max(0, pos - context)
        end = min(len(content), pos + len(query) + context)
        
        return '.. .' + content[start:end] + '...'
    
    def get_custom_dashboards(self):
        """Get list of custom dashboards"""
        dashboards_dir = ROOT_DIR / "DASHBOARDS"
        if not dashboards_dir.exists():
            return {'dashboards': []}
        
        dashboards = []
        for file_path in dashboards_dir. glob('*. html'):
            dashboards.append({
                'name': file_path.stem,
                'title': self.extract_title(file_path),
                'path': f'/DASHBOARDS/{file_path.name}'
            })
        
        return {'dashboards': dashboards}
    
    def extract_title(self, html_path):
        """Extract title from HTML file"""
        try:
            with open(html_path, 'r', encoding='utf-8') as f:
                content = f.read(500)  # First 500 chars
            
            import re
            match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
            if match:
                return match.group(1)
        except:
            pass
        
        return html_path.stem
    
    def count_files(self, directory):
        """Count total files"""
        return sum(1 for _ in directory.rglob('*') if _.is_file())


def main():
    """Launch dashboard server"""
    log_header("dashboard.py", "Launching Dashboard")
    
    # Create DASHBOARDS directory
    dashboards_dir = ROOT_DIR / "DASHBOARDS"
    dashboards_dir.mkdir(exist_ok=True)
    
    print("\n" + "="*70)
    print("🛸 COUNTERBALANCE - DASHBOARD")
    print("="*70)
    print(f"\n🌐 Dashboard running at: http://localhost:{PORT}")
    print(f"📁 Serving from: {ROOT_DIR}")
    print(f"\n📊 Main Dashboard:       http://localhost:{PORT}/dashboard_main. html")
    print(f"🎨 Custom Dashboards:    Drop HTML files in DASHBOARDS/")
    print(f"\n💡 Tip: Custom dashboards auto-appear in the menu!")
    print("\nPress Ctrl+C to stop\n")
    print("="*70 + "\n")
    
    # Open browser
    webbrowser.open(f"http://localhost:{PORT}/dashboard_main.html")
    
    # Start server
    with socketserver.TCPServer(("", PORT), DashboardHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n🛸 Dashboard shut down\n")
            close_out("dashboard.py", "SUCCESS")


if __name__ == "__main__":
    main()