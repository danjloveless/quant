#!/usr/bin/env python3
"""
QUANTFIN SOCIETY RESEARCH - Cross-Platform Launcher
Universal launcher for Mac and Windows
"""

import subprocess
import sys
import os
import platform
import time

def check_dependencies():
    """Check if all required packages are installed"""
    required_packages = [
        'streamlit', 'pandas', 'numpy', 'plotly', 'scipy', 
        'yfinance', 'openai', 'requests', 'trafilatura'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    return missing_packages

def launch_streamlit():
    """Launch the Streamlit application"""
    print("🚀 Launching QUANTFIN SOCIETY RESEARCH Platform...")
    print(f"Platform: {platform.system()}")
    print(f"Python: {sys.version}")
    print("-" * 50)
    
    # Check dependencies
    missing = check_dependencies()
    if missing:
        print(f"❌ Missing packages: {', '.join(missing)}")
        print("Run: python install_requirements.py")
        return False
    
    # Check if main.py exists
    if not os.path.exists('main.py'):
        print("❌ main.py not found in current directory")
        return False
    
    # Launch Streamlit
    try:
        print("🌐 Starting web server...")
        print("📊 Access your application at: http://localhost:5000")
        print("🛑 Press Ctrl+C to stop the server")
        print("-" * 50)
        
        # Run streamlit with cross-platform compatibility
        cmd = [sys.executable, "-m", "streamlit", "run", "main.py", 
               "--server.port", "5000", 
               "--server.address", "0.0.0.0",
               "--server.headless", "true"]
        
        subprocess.run(cmd)
        
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"❌ Error launching application: {e}")
        return False
    
    return True

def main():
    """Main launcher function"""
    if len(sys.argv) > 1 and sys.argv[1] == "--install":
        # Run installation
        print("Running installation...")
        subprocess.call([sys.executable, "install_requirements.py"])
    else:
        # Launch application
        launch_streamlit()

if __name__ == "__main__":
    main()