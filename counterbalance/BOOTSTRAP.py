#!/usr/bin/env python3
"""
🛸 COUNTERBALANCE - Bootstrap Setup Script
Professional grade initialization with validation and error handling
"""

import os
import sys
import subprocess
import platform
from pathlib import Path
from typing import List, Tuple

# ASCII Art Banner
BANNER = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   ██████╗ ██████╗ ██╗   ██╗███╗   ██╗████████╗███████╗██████╗
║  ██╔════╝██╔═══██╗██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
║  ██║     ██║   ██║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
║  ██║     ██║   ██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
║  ╚██████╗╚██████╔╝╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
║   ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
║                                                              ║
║            BALANCE - Bootstrap Setup v1.0.0                 ║
║                                                              ║
║     Self-Healing Modular Workspace for Alien Learners  🛸   ║
╚══════════════════════════════════════════════════════════════╝
"""

# Folder structure
FOLDERS = [
    "INBOX",
    "System_Logs",
    "AI_CHATS",
    "__Scrap_Pile",
    "CODE_REFINERY",
    "MODULES",
    "MODULES/CHATS",
    "MODULES/SNIPPETS",
    "MODULES/CODE_PLAYGROUND",
    "MODULES/NOTEBOOKS",
]

# Files to create
ROOT_FILES = [
    "Import_Header_Include.py",
    "Import_Footer_Include.py",
    "Import_Globals_Include.py",
    "Root_Processor.py",
    "Overwatch_Processor.py",
    "auto_function_doc.py",
    "requirements.txt",
    ".env. template",
]

def print_section(title: str):
    """Print a formatted section header"""
    print(f"\n{'━' * 60}")
    print(f"  {title}")
    print(f"{'━' * 60}")

def check_python_version() -> Tuple[bool, str]:
    """Validate Python version (3.8+)"""
    version = sys.version_info
    version_str = f"{version.major}.{version. minor}.{version.micro}"
    
    if version.major >= 3 and version.minor >= 8:
        return True, version_str
    return False, version_str

def create_folders():
    """Create folder structure"""
    print_section("📁 Creating Folder Structure")
    
    for folder in FOLDERS:
        path = Path(folder)
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            print(f"  ✅ Created: {folder}/")
            
            # Create README.md in each folder
            readme_path = path / "README.md"
            if not readme_path.exists():
                with open(readme_path, 'w') as f:
                    f.write(f"# {path.name}\n\n*Module documentation coming soon*\n")
        else:
            print(f"  ⏭️  Exists: {folder}/")

def create_venv(path: Path, name: str = ". venv"):
    """Create virtual environment"""
    venv_path = path / name
    
    if venv_path.exists():
        print(f"  ⏭️  venv exists: {path}/{name}")
        return True
    
    try:
        subprocess.run(
            [sys. executable, "-m", "venv", str(venv_path)],
            check=True,
            capture_output=True
        )
        print(f"  ✅ Created venv: {path}/{name}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"  ❌ Failed to create venv:  {e}")
        return False

def create_requirements_txt(path: Path, content: str):
    """Create requirements.txt file"""
    req_file = path / "requirements.txt"
    
    if req_file.exists():
        print(f"  ⏭️  Exists: {path}/requirements.txt")
        return
    
    with open(req_file, 'w') as f:
        f.write(content)
    print(f"  ✅ Created:  {path}/requirements.txt")

def create_placeholder_files():
    """Create placeholder Python files"""
    print_section("📄 Creating System Files")
    
    placeholders = {
        "Import_Header_Include.py": '''"""
🛸 COUNTERBALANCE - Standard Header Include
Imported by all scripts for logging, debug, and globals
"""

import sys
import os
from pathlib import Path
from datetime import datetime

# Import globals
from Import_Globals_Include import *

# Debug mode (set via environment or override in script)
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

# Logging setup
def log_header(script_name: str, message: str):
    """Log to header. log with timestamp and origin"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [HEADER] [{script_name}] {message}\\n"
    
    log_file = Path("System_Logs/header.log")
    with open(log_file, 'a') as f:
        f.write(log_entry)
    
    if DEBUG:
        print(f"🔷 HEADER: {message}")

# System call time tracking
SCRIPT_START_TIME = datetime.now()

def get_runtime():
    """Get elapsed time since script start"""
    return (datetime.now() - SCRIPT_START_TIME).total_seconds()
''',
        
        "Import_Footer_Include. py": '''"""
🛸 COUNTERBALANCE - Standard Footer Include
Imported by all scripts for close-out, logging, and escalation
"""

from datetime import datetime
from pathlib import Path
import os

DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

def log_footer(script_name: str, message: str):
    """Log to footer.log with timestamp and origin"""
    timestamp = datetime. now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [FOOTER] [{script_name}] {message}\\n"
    
    log_file = Path("System_Logs/footer.log")
    with open(log_file, 'a') as f:
        f.write(log_entry)
    
    if DEBUG:
        print(f"🔶 FOOTER: {message}")

def close_out(script_name: str, status: str = "SUCCESS"):
    """Standard close-out procedure"""
    log_footer(script_name, f"Execution completed:  {status}")
''',
        
        "Import_Globals_Include.py": '''"""
🛸 COUNTERBALANCE - Global Configuration
NO HARD-CODED PATHS - All paths discovered dynamically
"""

import os
from pathlib import Path

# Discover root directory dynamically
ROOT_DIR = Path(__file__).parent.absolute()

# Dynamic folder paths
INBOX_DIR = ROOT_DIR / "INBOX"
LOGS_DIR = ROOT_DIR / "System_Logs"
AI_CHATS_DIR = ROOT_DIR / "AI_CHATS"
MODULES_DIR = ROOT_DIR / "MODULES"
SCRAP_DIR = ROOT_DIR / "__Scrap_Pile"
REFINERY_DIR = ROOT_DIR / "CODE_REFINERY"

# System configuration
SYSTEM_NAME = "COUNTERBALANCE"
VERSION = "1.0.0"

# Debug mode
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
''',
    }
    
    for filename, content in placeholders.items():
        filepath = Path(filename)
        if not filepath.exists():
            with open(filepath, 'w') as f:
                f.write(content)
            print(f"  ✅ Created: {filename}")
        else:
            print(f"  ⏭️  Exists: {filename}")

def create_env_template():
    """Create .env. template"""
    print_section("🔐 Creating Environment Template")
    
    template_path = Path(".env.template")
    if template_path.exists():
        print("  ⏭️  . env.template exists")
        return
    
    content = """# 🛸 COUNTERBALANCE - Environment Configuration
# Copy this to .env and fill in your values

# System Configuration
DEBUG=False

# API Keys (if needed)
# QWEN_API_KEY=your_key_here
# GEMINI_API_KEY=your_key_here

# GitHub Configuration (for automation)
# GITHUB_TOKEN=your_token_here
"""
    
    with open(template_path, 'w') as f:
        f.write(content)
    print("  ✅ Created .env.template")

def main():
    """Main bootstrap process"""
    print(BANNER)
    
    # Check Python version
    print_section("🐍 Validating Python Version")
    valid, version = check_python_version()
    if valid:
        print(f"  ✅ Python {version} detected")
    else:
        print(f"  ❌ Python {version} - Need 3.8+")
        sys.exit(1)
    
    # Create folders
    create_folders()
    
    # Create system files
    create_placeholder_files()
    
    # Create . env.template
    create_env_template()
    
    # Create root requirements.txt
    print_section("📦 Setting Up Dependencies")
    root_reqs = """# Root level dependencies
watchdog>=3.0.0
python-dotenv>=1.0.0
GitPython>=3.1.40
"""
    create_requirements_txt(Path(". "), root_reqs)
    
    # Create root venv
    print_section("🔧 Creating Root Virtual Environment")
    create_venv(Path("."))
    
    # Create module-specific venvs and requirements
    print_section("📦 Setting Up Modules")
    
    module_requirements = {
        "CHATS": "markdown>=3.5\nbeautifulsoup4>=4.12\n",
        "SNIPPETS":  "pygments>=2.17\njinja2>=3.1\n",
        "CODE_PLAYGROUND": "# monaco-editor integration\n",
        "NOTEBOOKS": "jupyter>=1.0\nnbconvert>=7.0\n",
    }
    
    for module, reqs in module_requirements.items():
        module_path = Path(f"MODULES/{module}")
        create_requirements_txt(module_path, reqs)
        create_venv(module_path)
    
    # Final summary
    print_section("✅ BOOTSTRAP COMPLETE")
    print("""
🎉 COUNTERBALANCE is ready! 

Next steps:
  1. Review . env.template and create . env (if needed)
  2. Activate root venv: 
     - Windows: .venv\\Scripts\\activate
     - Unix:     source .venv/bin/activate
  3. Install root dependencies:  pip install -r requirements.txt
  4. Drop files in INBOX/ to test
  5. Run processors or Overwatch

Documentation:  BUILD_SPEC.md
    """)

if __name__ == "__main__":
    main()