#!/usr/bin/env python3
"""
Fast backup utility for QUANTFIN SOCIETY RESEARCH platform.
Quick backup and restore functionality.
"""

import os
import sys
import shutil
import zipfile
from datetime import datetime
from pathlib import Path

def create_backup():
    """Create a backup of the platform"""
    
    print("💾 Creating QUANTFIN SOCIETY RESEARCH backup...")
    
    # Define backup directory
    backup_dir = Path("backups")
    backup_dir.mkdir(exist_ok=True)
    
    # Create backup filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"quantfin_backup_{timestamp}.zip"
    backup_path = backup_dir / backup_name
    
    # Files to backup
    files_to_backup = [
        'main.py',
        'startup.py',
        'deploy_main.py',
        'requirements.txt',
        'README.md',
        'Procfile',
        'startup_render.sh',
        'deploy.sh',
        'pyproject.toml',
        '.gitignore'
    ]
    
    # Directories to backup
    dirs_to_backup = [
        'static',
        'mobile'
    ]
    
    try:
        with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            
            # Add files
            for file in files_to_backup:
                if os.path.exists(file):
                    zipf.write(file)
                    print(f"  ✅ Added: {file}")
                else:
                    print(f"  ⚠️  Missing: {file}")
            
            # Add directories
            for dir_name in dirs_to_backup:
                if os.path.exists(dir_name):
                    for root, dirs, files in os.walk(dir_name):
                        for file in files:
                            file_path = os.path.join(root, file)
                            arc_name = os.path.relpath(file_path)
                            zipf.write(file_path, arc_name)
                            print(f"  ✅ Added: {arc_name}")
                else:
                    print(f"  ⚠️  Missing directory: {dir_name}")
        
        print(f"\n✅ Backup created: {backup_path}")
        print(f"📦 Size: {backup_path.stat().st_size / 1024:.1f} KB")
        
        return backup_path
        
    except Exception as e:
        print(f"❌ Backup failed: {e}")
        return None

def restore_backup(backup_path):
    """Restore from backup"""
    
    print(f"🔄 Restoring from backup: {backup_path}")
    
    if not os.path.exists(backup_path):
        print("❌ Backup file not found")
        return False
    
    try:
        with zipfile.ZipFile(backup_path, 'r') as zipf:
            zipf.extractall('.')
        
        print("✅ Backup restored successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Restore failed: {e}")
        return False

def list_backups():
    """List available backups"""
    
    backup_dir = Path("backups")
    
    if not backup_dir.exists():
        print("📁 No backups directory found")
        return
    
    backups = list(backup_dir.glob("quantfin_backup_*.zip"))
    
    if not backups:
        print("📁 No backups found")
        return
    
    print("📦 Available backups:")
    for backup in sorted(backups, reverse=True):
        size = backup.stat().st_size / 1024
        date = datetime.fromtimestamp(backup.stat().st_mtime)
        print(f"  {backup.name} ({size:.1f} KB) - {date.strftime('%Y-%m-%d %H:%M:%S')}")

def main():
    """Main backup utility"""
    
    if len(sys.argv) < 2:
        print("🚀 QUANTFIN SOCIETY RESEARCH - Backup Utility")
        print("Usage:")
        print("  python backup.py create    - Create backup")
        print("  python backup.py restore <file> - Restore from backup")
        print("  python backup.py list      - List backups")
        return
    
    command = sys.argv[1]
    
    if command == "create":
        create_backup()
    elif command == "restore":
        if len(sys.argv) < 3:
            print("❌ Please specify backup file")
            return
        restore_backup(sys.argv[2])
    elif command == "list":
        list_backups()
    else:
        print(f"❌ Unknown command: {command}")

if __name__ == "__main__":
    main()
