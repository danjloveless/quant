#!/usr/bin/env python3
"""
Ultra-fast launcher for QUANTFIN SOCIETY RESEARCH platform.
One-command setup and launch for maximum speed.
"""

import os
import sys
import subprocess
from pathlib import Path

def quick_setup():
    """Ultra-fast platform setup"""
    
    print("⚡ QUANTFIN SOCIETY RESEARCH - Ultra-Fast Setup")
    print("=" * 60)
    
    # Check Python version
    if sys.version_info < (3, 11):
        print("❌ Python 3.11+ required")
        sys.exit(1)
    
    print("✅ Python version OK")
    
    # Install dependencies
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt", 
            "--quiet", "--no-cache-dir"
        ])
        print("✅ Dependencies installed")
    except subprocess.CalledProcessError:
        print("❌ Dependency installation failed")
        sys.exit(1)
    
    # Create .env template
    if not os.path.exists('.env'):
        print("🔧 Creating .env template...")
        with open('.env', 'w') as f:
            f.write("""# QUANTFIN SOCIETY RESEARCH - API Configuration
# Add your API keys here

OPENAI_API_KEY=your_openai_api_key_here
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_key_here
""")
        print("✅ .env template created")
    
    # Create optimized config
    print("⚡ Optimizing configuration...")
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
    print("✅ Configuration optimized")
    
    print("\n🎯 Setup complete! Platform ready to launch.")
    return True

def quick_launch():
    """Ultra-fast platform launch"""
    
    print("🚀 Launching QUANTFIN SOCIETY RESEARCH platform...")
    
    # Set optimized environment
    os.environ.setdefault('STREAMLIT_SERVER_PORT', '5000')
    os.environ.setdefault('STREAMLIT_SERVER_ADDRESS', '0.0.0.0')
    os.environ.setdefault('STREAMLIT_SERVER_HEADLESS', 'true')
    os.environ.setdefault('STREAMLIT_SERVER_ENABLE_CORS', 'false')
    os.environ.setdefault('STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION', 'false')
    os.environ.setdefault('STREAMLIT_BROWSER_GATHER_USAGE_STATS', 'false')
    os.environ.setdefault('STREAMLIT_SERVER_MAX_UPLOAD_SIZE', '200')
    os.environ.setdefault('STREAMLIT_SERVER_FILE_WATCHER_TYPE', 'none')
    
    try:
        # Launch platform
        subprocess.run([
            sys.executable, '-m', 'streamlit', 'run', 'main.py',
            '--server.port', '5000'
        ], check=True)
    except KeyboardInterrupt:
        print("\n👋 Platform stopped by user")
    except Exception as e:
        print(f"❌ Launch failed: {e}")
        sys.exit(1)

def quick_test():
    """Quick platform test"""
    
    print("🧪 Quick platform test...")
    
    # Test imports
    try:
        import streamlit, pandas, numpy, plotly, yfinance, openai
        print("✅ All dependencies available")
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        return False
    
    # Test main.py
    if not os.path.exists('main.py'):
        print("❌ main.py not found")
        return False
    
    print("✅ Platform test passed")
    return True

def main():
    """Main quick launcher"""
    
    if len(sys.argv) < 2:
        print("⚡ QUANTFIN SOCIETY RESEARCH - Ultra-Fast Launcher")
        print("Usage:")
        print("  python quick_start.py setup  - Quick setup")
        print("  python quick_start.py launch - Quick launch")
        print("  python quick_start.py test   - Quick test")
        print("  python quick_start.py all    - Setup + test + launch")
        return
    
    command = sys.argv[1]
    
    if command == "setup":
        quick_setup()
    elif command == "launch":
        quick_launch()
    elif command == "test":
        quick_test()
    elif command == "all":
        print("⚡ Running complete quick setup...")
        if quick_setup() and quick_test():
            print("\n🚀 Starting platform...")
            quick_launch()
    else:
        print(f"❌ Unknown command: {command}")

if __name__ == "__main__":
    main()
