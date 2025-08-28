#!/usr/bin/env python3
"""
QUANTFIN SOCIETY RESEARCH - Cross-Platform Installation Script
Supports both Mac and Windows environments
"""

import subprocess
import sys
import os
import platform

def install_package(package):
    """Install a single package with error handling"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✅ Successfully installed: {package}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install {package}: {e}")
        return False

def main():
    """Main installation function"""
    print("🚀 QUANTFIN SOCIETY RESEARCH - Platform Installation")
    print(f"Platform: {platform.system()} {platform.release()}")
    print(f"Python: {sys.version}")
    print("-" * 50)
    
    # Essential packages for cross-platform compatibility
    packages = [
        "streamlit>=1.45.1",
        "pandas>=2.2.3", 
        "numpy>=2.2.6",
        "plotly>=6.1.2",
        "scipy>=1.15.3",
        "yfinance>=0.2.61",
        "openai>=1.84.0",
        "requests>=2.32.3",
        "trafilatura>=2.0.0",
        "python-dotenv>=1.1.1",
        "polygon>=1.2.6",
        "polygon-api-client>=1.14.5"
    ]
    
    # Update pip first
    print("📦 Updating pip...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    
    # Install packages
    print("📥 Installing required packages...")
    success_count = 0
    
    for package in packages:
        if install_package(package):
            success_count += 1
    
    # Summary
    print("\n" + "=" * 50)
    print(f"Installation Complete: {success_count}/{len(packages)} packages installed")
    
    if success_count == len(packages):
        print("✅ All packages installed successfully!")
        print("\n🚀 Ready to launch! Run: streamlit run main.py --server.port 5000")
    else:
        print("⚠️  Some packages failed to install. Check errors above.")
        
    # Create .env template if it doesn't exist
    if not os.path.exists('.env'):
        with open('.env', 'w') as f:
            f.write("# QUANTFIN SOCIETY RESEARCH - API Configuration\n")
            f.write("# Add your API keys here\n\n")
            f.write("OPENAI_API_KEY=your_openai_api_key_here\n")
            f.write("ALPHA_VANTAGE_API_KEY=your_alpha_vantage_key_here\n")
            f.write("POLYGON_API_KEY=your_polygon_api_key_here\n")
            f.write("NEWSAPI_KEY=your_newsapi_key_here\n")
        print("📝 Created .env template file")

if __name__ == "__main__":
    main()