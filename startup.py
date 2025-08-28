#!/usr/bin/env python3
"""
Production startup script for QUANTFIN SOCIETY RESEARCH platform.
Configures environment variables and starts the application with proper settings.
"""

import os
import sys
import subprocess
from pathlib import Path

def configure_environment():
    """Configure production environment variables."""
    
    # Streamlit server configuration
    os.environ.setdefault('STREAMLIT_SERVER_PORT', '5000')
    os.environ.setdefault('STREAMLIT_SERVER_ADDRESS', '0.0.0.0')
    os.environ.setdefault('STREAMLIT_SERVER_HEADLESS', 'true')
    os.environ.setdefault('STREAMLIT_SERVER_ENABLE_CORS', 'false')
    os.environ.setdefault('STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION', 'false')
    os.environ.setdefault('STREAMLIT_BROWSER_GATHER_USAGE_STATS', 'false')
    
    # Validate required API keys
    if not os.environ.get('OPENAI_API_KEY'):
        print('Warning: OPENAI_API_KEY is not set')
    
    if not os.environ.get('ALPHA_VANTAGE_API_KEY'):
        print('Warning: ALPHA_VANTAGE_API_KEY is not set')

def start_application():
    """Start the Streamlit application."""
    try:
        # Configure environment
        configure_environment()
        
        # Get application path
        app_dir = Path(__file__).parent
        main_app = app_dir / 'main.py'
        
        if not main_app.exists():
            print(f"Error: main.py not found at {main_app}")
            sys.exit(1)
        
        print("Starting QUANTFIN SOCIETY RESEARCH platform...")
        print(f"Application path: {main_app}")
        print(f"Server port: {os.environ.get('STREAMLIT_SERVER_PORT', '5000')}")
        
        # Start Streamlit
        subprocess.run([
            sys.executable, '-m', 'streamlit', 'run', 
            str(main_app), '--server.port', os.environ.get('STREAMLIT_SERVER_PORT', '5000')
        ], check=True)
        
    except KeyboardInterrupt:
        print("\nApplication stopped by user")
    except Exception as e:
        print(f"Error starting application: {e}")
        sys.exit(1)

if __name__ == '__main__':
    start_application()