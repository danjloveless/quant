#!/usr/bin/env python3
"""
Fast dependency installer for QUANTFIN SOCIETY RESEARCH platform.
Optimized for quick setup and deployment.
"""

import subprocess
import sys
import os

def install_dependencies():
    """Install all required dependencies quickly"""
    
    print("🚀 Installing QUANTFIN SOCIETY RESEARCH dependencies...")
    
    # Core dependencies for fast installation
    dependencies = [
        "streamlit>=1.45.1",
        "pandas>=2.2.3", 
        "numpy>=2.2.6",
        "plotly>=6.1.2",
        "yfinance>=0.2.61",
        "scipy>=1.15.3",
        "openai>=1.84.0",
        "requests>=2.32.3",
        "python-dotenv>=1.1.1",
        "trafilatura>=2.0.0",
        "polygon>=1.2.6",
        "polygon-api-client>=1.14.5"
    ]
    
    try:
        # Install all dependencies at once
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", 
            "--upgrade", "--no-cache-dir"
        ] + dependencies)
        
        print("✅ All dependencies installed successfully!")
        print("🎯 Platform ready for use!")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Installation failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_dependencies()