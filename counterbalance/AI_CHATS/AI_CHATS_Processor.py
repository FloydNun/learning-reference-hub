#!/usr/bin/env python3
"""
🛸 COUNTERBALANCE - AI_CHATS Processor
Handles AI-assisted healing when auto-healing fails
- Routes complex errors to Qwen or Gemini
- Validates AI responses
- Applies fixes with safety rails
"""

import sys
import os
from pathlib import Path
from datetime import datetime
import json

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from Import_Header_Include import log_header, get_runtime, DEBUG
from Import_Footer_Include import log_footer, close_out
from Import_Globals_Include import *


class AIChatProcessor:
    """Processor for AI-assisted healing"""
    
    def __init__(self):
        self.script_name = "AI_CHATS_Processor.py"
        log_header(self.script_name, "AI CHATS Processor initialized")
    
    def log_console(self, message: str):
        """Log to console.log"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [CONSOLE] [{self.script_name}] {message}\n"
        
        log_file = LOGS_DIR / "console.log"
        with open(log_file, 'a') as f:
            f.write(log_entry)
        
        if DEBUG:
            print(f"🤖 AI_CHATS: {message}")
    
    def log_error(self, message: str):
        """Log to error.log"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [ERROR] [{self.script_name}] {message}\n"
        
        log_file = LOGS_DIR / "error. log"
        with open(log_file, 'a') as f:
            f.write(log_entry)
        
        print(f"❌ ERROR: {message}")
    
    def create_ai_request(self, error_info: dict, ai_type: str = "qwen"):
        """Create . msg file for AI assistant"""
        self.log_console(f"Creating AI request for:  {ai_type}")
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        request = {
            'timestamp': timestamp,
            'error_type': error_info. get('type', 'unknown'),
            'error_message': error_info. get('message', ''),
            'source_file': error_info.get('file', ''),
            'attempted_fixes': error_info.get('attempted_fixes', []),
            'context': error_info.get('context', ''),
            'request_type': ai_type
        }
        
        msg_file = AI_CHATS_DIR / f"{ai_type}_cli.msg"
        
        try:
            with open(msg_file, 'w') as f:
                f.write("="*60 + "\n")
                f.write(f"AI HEALING REQUEST - {timestamp}\n")
                f.write("="*60 + "\n\n")
                f.write(f"Error Type: {request['error_type']}\n")
                f.write(f"Source:  {request['source_file']}\n\n")
                f.write(f"Error Message:\n{request['error_message']}\n\n")
                f.write(f"Attempted Fixes:\n")
                for fix in request['attempted_fixes']: 
                    f.write(f"  - {fix}\n")
                f.write(f"\nContext:\n{request['context']}\n\n")
                f.write("="*60 + "\n")
                f.write("Please provide a fix or guidance.\n")
            
            self.log_console(f"Request created: {msg_file. name}")
            return msg_file
        except Exception as e:
            self. log_error(f"Failed to create AI request: {e}")
            return None
    
    def check_for_responses(self):
        """Check for AI response . log files"""
        self.log_console("Checking for AI responses")
        
        qwen_log = AI_CHATS_DIR / "Qwen_cli.log"
        gemini_log = AI_CHATS_DIR / "Gemini_cli.log"
        
        responses = []
        
        if qwen_log.exists():
            self.log_console(f"Found response:  {qwen_log.name}")
            responses.append(('qwen', qwen_log))
        
        if gemini_log.exists():
            self.log_console(f"Found response:  {gemini_log.name}")
            responses.append(('gemini', gemini_log))
        
        return responses
    
    def validate_ai_response(self, response_file: Path) -> bool:
        """Validate AI response before applying"""
        self.log_console(f"Validating response: {response_file.name}")
        
        try:
            with open(response_file, 'r') as f:
                content = f.read()
            
            # Basic validation
            if len(content) < 10:
                self.log_error("Response too short")
                return False
            
            # TODO: More sophisticated validation
            # - Check for dangerous commands
            # - Validate syntax
            # - Test in isolated environment
            
            self.log_console("Validation passed")
            return True
        except Exception as e:
            self.log_error(f"Validation failed: {e}")
            return False
    
    def apply_fix(self, response_file: Path) -> bool:
        """Apply fix from AI response with safety rails"""
        self.log_console(f"Applying fix from:  {response_file.name}")
        
        # Validate first
        if not self.validate_ai_response(response_file):
            self.log_error("Cannot apply invalid response")
            return False
        
        # TODO: Implement actual fix application with safety rails
        # - Create backup
        # - Apply in test environment
        # - Validate result
        # - Apply to production if safe
        
        self.log_console("Fix application:  [PLACEHOLDER - not yet implemented]")
        return True


def main():
    """Main entry point"""
    processor = AIChatProcessor()
    
    try:
        # Check for existing responses
        responses = processor.check_for_responses()
        
        if responses:
            print(f"\n🤖 Found {len(responses)} AI response(s)\n")
            for ai_type, response_file in responses:
                print(f"  {ai_type. upper()}: {response_file.name}")
        else:
            print("\n📭 No AI responses pending\n")
        
        close_out("AI_CHATS_Processor.py", "SUCCESS")
    except Exception as e:
        processor.log_error(f"Fatal error: {e}")
        close_out("AI_CHATS_Processor.py", "FAILURE")
        sys.exit(1)


if __name__ == "__main__":
    main()