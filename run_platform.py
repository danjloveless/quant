#!/usr/bin/env python3
"""
Fast platform launcher for QUANTFIN SOCIETY RESEARCH.
Optimized for quick startup and minimal overhead.
"""

import subprocess
import sys
import os
from pathlib import Path

def launch_platform():
    """Launch the platform with optimized settings"""
    
    print("🚀 Launching QUANTFIN SOCIETY RESEARCH platform...")
    
    # Set optimized environment variables
    os.environ.setdefault('STREAMLIT_SERVER_PORT', '5000')
    os.environ.setdefault('STREAMLIT_SERVER_ADDRESS', '0.0.0.0')
    os.environ.setdefault('STREAMLIT_SERVER_HEADLESS', 'true')
    os.environ.setdefault('STREAMLIT_SERVER_ENABLE_CORS', 'false')
    os.environ.setdefault('STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION', 'false')
    os.environ.setdefault('STREAMLIT_BROWSER_GATHER_USAGE_STATS', 'false')
    
    # Performance optimizations
    os.environ.setdefault('STREAMLIT_SERVER_MAX_UPLOAD_SIZE', '200')
    os.environ.setdefault('STREAMLIT_SERVER_FILE_WATCHER_TYPE', 'none')
    
    try:
        # Get main.py path
        main_path = Path(__file__).parent / 'main.py'
        
        if not main_path.exists():
            print(f"❌ Error: main.py not found at {main_path}")
            sys.exit(1)
        
        print(f"📁 Application: {main_path}")
        print(f"🌐 Port: {os.environ.get('STREAMLIT_SERVER_PORT', '5000')}")
        print("🎯 Starting platform...")
        
        # Launch Streamlit with optimized settings
        subprocess.run([
            sys.executable, '-m', 'streamlit', 'run', 
            str(main_path), '--server.port', os.environ.get('STREAMLIT_SERVER_PORT', '5000')
        ], check=True)
        
    except KeyboardInterrupt:
        print("\n👋 Platform stopped by user")
    except Exception as e:
        print(f"❌ Error launching platform: {e}")
        sys.exit(1)

if __name__ == "__main__":
    launch_platform()