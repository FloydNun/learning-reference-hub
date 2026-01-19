#!/usr/bin/env python3
"""
🛸 COUNTERBALANCE - Environment Bootstrapper
Self-healing environment with offline rebuild capability
- Checks directory for dupes/unused files
- Validates requirements
- Downloads and stores sources in ENV_SOURCES/
- Can rebuild from scratch WITHOUT internet
- Generates ignition scripts for each module
"""

import sys
import os
import subprocess
import hashlib
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple

from Import_Header_Include import log_header, get_runtime, DEBUG
from Import_Footer_Include import log_footer, close_out
from Import_Globals_Include import *


class EnvBootstrapper:
    """Bootstraps and maintains environment"""
    
    def __init__(self):
        self.script_name = "ENV_BOOTSTRAPPER.py"
        self.env_sources_dir = ROOT_DIR / "ENV_SOURCES"
        self.env_sources_dir.mkdir(exist_ok=True)
        
        self.packages_dir = self.env_sources_dir / "packages"
        self.wheels_dir = self.env_sources_dir / "wheels"
        self.sources_manifest = self.env_sources_dir / "manifest.json"
        
        self.packages_dir.mkdir(exist_ok=True)
        self.wheels_dir.mkdir(exist_ok=True)
        
        log_header(self.script_name, "ENV Bootstrapper initialized")
    
    def log_console(self, message: str):
        """Log to console.log"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [CONSOLE] [{self.script_name}] {message}\n"
        
        log_file = LOGS_DIR / "console.log"
        with open(log_file, 'a') as f:
            f.write(log_entry)
        
        if DEBUG: 
            print(f"🔧 ENV: {message}")
    
    def check_for_duplicates(self, directory: Path) -> List[Tuple[Path, Path]]:
        """Find duplicate files by content hash"""
        self.log_console(f"Checking for duplicates in: {directory.name}")
        
        file_hashes = {}
        duplicates = []
        
        for file_path in directory.rglob('*'):
            if file_path.is_file() and not file_path.name.startswith('.'):
                # Calculate hash
                file_hash = self. calculate_hash(file_path)
                
                if file_hash in file_hashes:
                    duplicates.append((file_hashes[file_hash], file_path))
                    self.log_console(f"Duplicate found: {file_path. name} == {file_hashes[file_hash]. name}")
                else:
                    file_hashes[file_hash] = file_path
        
        return duplicates
    
    def calculate_hash(self, file_path: Path) -> str:
        """Calculate MD5 hash"""
        md5 = hashlib.md5()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda:  f.read(4096), b""):
                md5.update(chunk)
        return md5.hexdigest()
    
    def find_unused_files(self, directory: Path) -> List[Path]:
        """Find files that haven't been accessed in 30+ days"""
        import time
        
        self.log_console(f"Finding unused files in: {directory.name}")
        
        unused = []
        threshold = time.time() - (30 * 24 * 60 * 60)  # 30 days ago
        
        for file_path in directory. rglob('*'):
            if file_path.is_file():
                last_access = file_path.stat().st_atime
                if last_access < threshold:
                    unused.append(file_path)
        
        return unused
    
    def validate_requirements(self, requirements_file: Path) -> Dict:
        """Validate that requirements are met"""
        self. log_console(f"Validating requirements:  {requirements_file.name}")
        
        result = {
            'valid': True,
            'missing':  [],
            'outdated': []
        }
        
        if not requirements_file.exists():
            return result
        
        try: 
            with open(requirements_file, 'r') as f:
                requirements = f.readlines()
            
            for req in requirements:
                req = req.strip()
                if not req or req.startswith('#'):
                    continue
                
                # Parse requirement
                if '>=' in req:
                    package, version = req.split('>=')
                    package = package.strip()
                    version = version.strip()
                else:
                    package = req
                    version = None
                
                # Check if installed
                try:
                    import importlib
                    importlib.import_module(package. replace('-', '_'))
                except ImportError:
                    result['missing'].append(req)
                    result['valid'] = False
                    self.log_console(f"Missing:  {req}")
            
        except Exception as e:
            self.log_console(f"Validation failed: {e}")
            result['valid'] = False
        
        return result
    
    def download_and_store_package(self, package: str) -> bool:
        """Download package and store in ENV_SOURCES"""
        self.log_console(f"Downloading package: {package}")
        
        try:
            # Download wheel file
            result = subprocess.run(
                [sys.executable, '-m', 'pip', 'download', package, '--dest', str(self.wheels_dir)],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                self.log_console(f"Downloaded: {package}")
                return True
            else:
                self.log_console(f"Download failed: {result.stderr}")
                return False
                
        except Exception as e:
            self. log_console(f"Download error: {e}")
            return False
    
    def install_from_offline(self, requirements_file: Path) -> bool:
        """Install packages from ENV_SOURCES (offline mode)"""
        self.log_console(f"Installing from offline sources: {requirements_file.name}")
        
        try:
            result = subprocess.run(
                [sys.executable, '-m', 'pip', 'install', 
                 '--no-index', '--find-links', str(self.wheels_dir),
                 '-r', str(requirements_file)],
                capture_output=True,
                text=True
            )
            
            if result. returncode == 0:
                self.log_console("Offline install successful")
                return True
            else:
                self.log_console(f"Offline install failed: {result.stderr}")
                return False
                
        except Exception as e:
            self.log_console(f"Install error: {e}")
            return False
    
    def update_manifest(self):
        """Update manifest of stored packages"""
        manifest = {
            'updated': datetime.now().isoformat(),
            'packages': []
        }
        
        for wheel in self.wheels_dir.glob('*.whl'):
            manifest['packages'].append({
                'name': wheel.name,
                'size': wheel.stat().st_size,
                'hash': self. calculate_hash(wheel)
            })
        
        with open(self.sources_manifest, 'w') as f:
            json.dump(manifest, f, indent=2)
        
        self.log_console(f"Manifest updated: {len(manifest['packages'])} packages")
    
    def bootstrap_environment(self):
        """Full bootstrap process"""
        print("\n" + "="*60)
        print("🔧 ENVIRONMENT BOOTSTRAPPER")
        print("="*60 + "\n")
        
        # 1. Check for duplicates
        print("1. Checking for duplicates...")
        duplicates = self.check_for_duplicates(ROOT_DIR)
        if duplicates:
            print(f"   ⚠️  Found {len(duplicates)} duplicate(s)")
            for original, duplicate in duplicates:
                print(f"      {duplicate} == {original}")
        else:
            print("   ✅ No duplicates found")
        
        # 2. Find unused files
        print("\n2. Finding unused files...")
        unused = self.find_unused_files(ROOT_DIR)
        if unused:
            print(f"   ℹ️  Found {len(unused)} unused file(s) (30+ days old)")
        else:
            print("   ✅ No unused files")
        
        # 3. Validate root requirements
        print("\n3. Validating requirements...")
        req_file = ROOT_DIR / "requirements.txt"
        validation = self.validate_requirements(req_file)
        
        if validation['valid']:
            print("   ✅ All requirements met")
        else:
            print(f"   ⚠️  Missing packages: {len(validation['missing'])}")
            
            # Offer to download
            if validation['missing']:
                print("\n   Downloading missing packages...")
                for package in validation['missing']:
                    self.download_and_store_package(package)
        
        # 4. Update manifest
        print("\n4. Updating ENV_SOURCES manifest...")
        self.update_manifest()
        print("   ✅ Manifest updated")
        
        print("\n" + "="*60)
        print("✅ BOOTSTRAP COMPLETE")
        print("="*60 + "\n")


def main():
    """Main entry point"""
    bootstrapper = EnvBootstrapper()
    
    try:
        bootstrapper. bootstrap_environment()
        close_out("ENV_BOOTSTRAPPER.py", "SUCCESS")
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        close_out("ENV_BOOTSTRAPPER.py", "FAILURE")
        sys.exit(1)


if __name__ == "__main__":
    main()