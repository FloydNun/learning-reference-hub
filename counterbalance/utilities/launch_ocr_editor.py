#!/usr/bin/env python3
"""
🛸 COUNTERBALANCE - OCR Editor Launcher
Launches the OCR editor web interface
"""

import sys
import os
import http.server
import socketserver
import webbrowser
from pathlib import Path

# Add parent directory to path
sys.path. insert(0, str(Path(__file__).parent.parent))

from Import_Header_Include import log_header
from Import_Footer_Include import close_out

PORT = 8888

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(Path(__file__).parent), **kwargs)

def main():
    log_header("launch_ocr_editor.py", "Launching OCR Editor")
    
    print("\n" + "="*60)
    print("📄 OCR EDITOR - COUNTERBALANCE")
    print("="*60)
    print(f"\n🌐 Starting server on http://localhost:{PORT}")
    print(f"📁 Serving from: {Path(__file__).parent}")
    print("\nPress Ctrl+C to stop\n")
    print("="*60 + "\n")
    
    # Open browser
    webbrowser.open(f"http://localhost:{PORT}/ocr_editor. html")
    
    # Start server
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n📄 OCR Editor shut down\n")
            close_out("launch_ocr_editor.py", "SUCCESS")

if __name__ == "__main__":
    main()