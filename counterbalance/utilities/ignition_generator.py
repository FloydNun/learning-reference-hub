#!/usr/bin/env python3
"""
🛸 COUNTERBALANCE - Ignition Generator
Generates PowerShell ignition scripts for each module
- One script per module for true modularity
- Can initialize module from scratch
- Rollback capability
- Stored in GENESIS_IGNITION/
"""

import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent.parent))

from Import_Header_Include import log_header, get_runtime, DEBUG
from Import_Footer_Include import log_footer, close_out
from Import_Globals_Include import *


class IgnitionGenerator:
    """Generates ignition scripts for modules"""
    
    def __init__(self):
        self.script_name = "ignition_generator.py"
        self.ignition_dir = ROOT_DIR / "GENESIS_IGNITION"
        self.ignition_dir.mkdir(exist_ok=True)
        
        log_header(self.script_name, "Ignition Generator initialized")
    
    def generate_module_ignition(self, module_name: str, module_path:  Path):
        """Generate PowerShell ignition script for module"""
        
        ignition_content = f'''# 🛸 COUNTERBALANCE - Ignition Script
# Module: {module_name}
# Generated: {datetime.now().isoformat()}
# Purpose: Initialize {module_name} module from scratch

Write-Host "🚀 IGNITING MODULE: {module_name}" -ForegroundColor Cyan
Write-Host ("=" * 60)

# Module configuration
$MODULE_NAME = "{module_name}"
$MODULE_PATH = "{module_path}"
$VENV_PATH = "$MODULE_PATH\\. venv"
$REQUIREMENTS = "$MODULE_PATH\\requirements.txt"

# Step 1: Validate module directory
Write-Host "`n1. Validating module directory..." -ForegroundColor Yellow
if (-Not (Test-Path $MODULE_PATH)) {{
    Write-Host "   ❌ Module directory not found:  $MODULE_PATH" -ForegroundColor Red
    exit 1
}}
Write-Host "   ✅ Module directory exists" -ForegroundColor Green

# Step 2: Create virtual environment
Write-Host "`n2. Creating virtual environment..." -ForegroundColor Yellow
if (Test-Path $VENV_PATH) {{
    Write-Host "   ⏭️  venv already exists" -ForegroundColor Gray
}} else {{
    python -m venv $VENV_PATH
    if ($LASTEXITCODE -eq 0) {{
        Write-Host "   ✅ Virtual environment created" -ForegroundColor Green
    }} else {{
        Write-Host "   ❌ Failed to create venv" -ForegroundColor Red
        exit 1
    }}
}}

# Step 3: Activate virtual environment
Write-Host "`n3. Activating virtual environment..." -ForegroundColor Yellow
& "$VENV_PATH\\Scripts\\Activate.ps1"
Write-Host "   ✅ Virtual environment activated" -ForegroundColor Green

# Step 4: Install requirements
Write-Host "`n4. Installing requirements..." -ForegroundColor Yellow
if (Test-Path $REQUIREMENTS) {{
    # Try offline first
    $ENV_SOURCES = "{ROOT_DIR}\\ENV_SOURCES\\wheels"
    if (Test-Path $ENV_SOURCES) {{
        Write-Host "   Attempting offline install..." -ForegroundColor Gray
        python -m pip install --no-index --find-links $ENV_SOURCES -r $REQUIREMENTS
    }} else {{
        Write-Host "   Installing from PyPI..." -ForegroundColor Gray
        python -m pip install -r $REQUIREMENTS
    }}
    
    if ($LASTEXITCODE -eq 0) {{
        Write-Host "   ✅ Requirements installed" -ForegroundColor Green
    }} else {{
        Write-Host "   ⚠️  Some packages may have failed" -ForegroundColor Yellow
    }}
}} else {{
    Write-Host "   ⏭️  No requirements. txt found" -ForegroundColor Gray
}}

# Step 5:  Validate module processor
Write-Host "`n5. Validating module processor..." -ForegroundColor Yellow
$PROCESSOR = "$MODULE_PATH\\${{MODULE_NAME}}_Processor.py"
if (Test-Path $PROCESSOR) {{
    Write-Host "   ✅ Processor found:  ${{MODULE_NAME}}_Processor. py" -ForegroundColor Green
    
    # Test processor
    Write-Host "   Testing processor..." -ForegroundColor Gray
    python $PROCESSOR
    
    if ($LASTEXITCODE -eq 0) {{
        Write-Host "   ✅ Processor test passed" -ForegroundColor Green
    }} else {{
        Write-Host "   ⚠️  Processor test failed (may need data)" -ForegroundColor Yellow
    }}
}} else {{
    Write-Host "   ⚠️  No processor found" -ForegroundColor Yellow
}}

# Step 6: Summary
Write-Host "`n" ("=" * 60)
Write-Host "✅ MODULE IGNITION COMPLETE:  {module_name}" -ForegroundColor Green
Write-Host ("=" * 60)

Write-Host "`nModule is ready for use!" -ForegroundColor Cyan
Write-Host "Location: $MODULE_PATH" -ForegroundColor Gray

# Keep window open
Read-Host -Prompt "`nPress Enter to exit"
'''
        
        ignition_file = self.ignition_dir / f"ignition_{module_name}.ps1"
        
        with open(ignition_file, 'w', encoding='utf-8') as f:
            f.write(ignition_content)
        
        print(f"✅ Generated:  {ignition_file.name}")
        return ignition_file
    
    def generate_all_ignitions(self):
        """Generate ignition scripts for all modules"""
        print("\n🚀 GENERATING IGNITION SCRIPTS\n")
        
        modules_dir = MODULES_DIR
        
        if not modules_dir.exists():
            print("❌ MODULES directory not found")
            return
        
        generated = []
        
        for module_path in modules_dir.iterdir():
            if module_path.is_dir() and not module_path.name.startswith('.'):
                module_name = module_path.name
                ignition_file = self.generate_module_ignition(module_name, module_path)
                generated.append(ignition_file)
        
        print(f"\n✅ Generated {len(generated)} ignition script(s)")
        print(f"   Location: {self.ignition_dir}")
        
        return generated


def main():
    """Main entry point"""
    generator = IgnitionGenerator()
    
    try:
        generator.generate_all_ignitions()
        close_out("ignition_generator.py", "SUCCESS")
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        close_out("ignition_generator.py", "FAILURE")
        sys.exit(1)


if __name__ == "__main__":
    main()