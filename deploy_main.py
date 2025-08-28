#!/usr/bin/env python3
"""
Production deployment entry point for QUANTFIN SOCIETY RESEARCH platform.
Configures environment variables and starts the Streamlit application.
"""

import os
import sys
import subprocess
from pathlib import Path

def setup_production_environment():
    """Configure production environment variables and settings."""
    
    # Set production environment variables
    os.environ.setdefault('STREAMLIT_SERVER_PORT', '5000')
    os.environ.setdefault('STREAMLIT_SERVER_ADDRESS', '0.0.0.0')
    os.environ.setdefault('STREAMLIT_SERVER_HEADLESS', 'true')
    os.environ.setdefault('STREAMLIT_SERVER_ENABLE_CORS', 'false')
    os.environ.setdefault('STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION', 'false')
    os.environ.setdefault('STREAMLIT_BROWSER_GATHER_USAGE_STATS', 'false')
    
    # Validate API keys
    if not os.environ.get('OPENAI_API_KEY'):
        print('Warning: OPENAI_API_KEY not set')
    if not os.environ.get('ALPHA_VANTAGE_API_KEY'):
        print('Warning: ALPHA_VANTAGE_API_KEY not set')

def main():
    """Main entry point for production deployment."""
    try:
        # Setup production environment
        setup_production_environment()
        
        # Get the directory containing this script
        script_dir = Path(__file__).parent
        main_app_path = script_dir / 'main.py'
        
        # Verify main.py exists
        if not main_app_path.exists():
            print(f"Error: main.py not found at {main_app_path}")
            sys.exit(1)
        
        # Start Streamlit application
        print("Starting QUANTFIN SOCIETY RESEARCH platform...")
        subprocess.run([sys.executable, '-m', 'streamlit', 'run', str(main_app_path)], check=True)
        
    except KeyboardInterrupt:
        print("\nApplication stopped by user")
    except Exception as e:
        print(f"Error starting application: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()