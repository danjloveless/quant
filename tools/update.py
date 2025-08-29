#!/usr/bin/env python3
"""
Fast update utility for QUANTFIN SOCIETY RESEARCH platform.
Quick dependency updates and platform maintenance.
"""

import subprocess
import sys
import os
from pathlib import Path

def update_dependencies():
    """Update all dependencies to latest versions"""
    
    print("🔄 Updating QUANTFIN SOCIETY RESEARCH dependencies...")
    
    try:
        # Update pip first
        print("📦 Updating pip...")
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "--upgrade", "pip"
        ])
        
        # Update all dependencies
        print("📦 Updating dependencies...")
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "--upgrade", 
            "streamlit", "pandas", "numpy", "plotly", "yfinance", 
            "scipy", "openai", "requests", "trafilatura", 
            "python-dotenv", "polygon", "polygon-api-client"
        ])
        
        print("✅ Dependencies updated successfully!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Update failed: {e}")
        return False

def clean_cache():
    """Clean pip cache and temporary files"""
    
    print("🧹 Cleaning cache and temporary files...")
    
    try:
        # Clean pip cache
        subprocess.check_call([
            sys.executable, "-m", "pip", "cache", "purge"
        ])
        
        # Remove __pycache__ directories
        for root, dirs, files in os.walk('.'):
            for dir_name in dirs:
                if dir_name == '__pycache__':
                    cache_path = os.path.join(root, dir_name)
                    subprocess.run(['rm', '-rf', cache_path])
                    print(f"  🗑️  Removed: {cache_path}")
        
        print("✅ Cache cleaned successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Cache cleaning failed: {e}")
        return False

def check_updates():
    """Check for available updates"""
    
    print("🔍 Checking for updates...")
    
    try:
        # Check outdated packages
        result = subprocess.run([
            sys.executable, "-m", "pip", "list", "--outdated"
        ], capture_output=True, text=True)
        
        if result.stdout.strip():
            print("📦 Outdated packages found:")
            print(result.stdout)
        else:
            print("✅ All packages are up to date!")
        
        return True
        
    except Exception as e:
        print(f"❌ Update check failed: {e}")
        return False

def optimize_performance():
    """Optimize platform performance"""
    
    print("⚡ Optimizing platform performance...")
    
    # Create optimized .streamlit/config.toml
    config_dir = Path(".streamlit")
    config_dir.mkdir(exist_ok=True)
    
    config_content = """[server]
port = 5000
address = "0.0.0.0"
headless = true
enableCORS = false
enableXsrfProtection = false
maxUploadSize = 200
fileWatcherType = "none"

[browser]
gatherUsageStats = false

[theme]
base = "light"
"""
    
    config_file = config_dir / "config.toml"
    config_file.write_text(config_content)
    
    print("✅ Performance optimizations applied!")
    return True

def main():
    """Main update utility"""
    
    if len(sys.argv) < 2:
        print("🚀 QUANTFIN SOCIETY RESEARCH - Update Utility")
        print("Usage:")
        print("  python update.py dependencies - Update dependencies")
        print("  python update.py cache       - Clean cache")
        print("  python update.py check       - Check for updates")
        print("  python update.py optimize    - Optimize performance")
        print("  python update.py all         - Run all updates")
        return
    
    command = sys.argv[1]
    
    if command == "dependencies":
        update_dependencies()
    elif command == "cache":
        clean_cache()
    elif command == "check":
        check_updates()
    elif command == "optimize":
        optimize_performance()
    elif command == "all":
        print("🔄 Running all updates...")
        update_dependencies()
        clean_cache()
        check_updates()
        optimize_performance()
        print("✅ All updates completed!")
    else:
        print(f"❌ Unknown command: {command}")

if __name__ == "__main__":
    main()
