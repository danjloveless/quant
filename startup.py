#!/usr/bin/env python3
"""
QUANTFIN SOCIETY RESEARCH - Production Startup Script
Configures environment for Replit Deployments with Autoscale
"""

import os
import subprocess
import sys

def setup_production_environment():
    """Configure production environment variables"""
    
    # Streamlit production settings
    os.environ.update({
        'STREAMLIT_SERVER_PORT': '5000',
        'STREAMLIT_SERVER_ADDRESS': '0.0.0.0',
        'STREAMLIT_SERVER_HEADLESS': 'true',
        'STREAMLIT_SERVER_ENABLE_CORS': 'false',
        'STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION': 'false',
        'STREAMLIT_BROWSER_GATHER_USAGE_STATS': 'false',
        'STREAMLIT_GLOBAL_DEVELOPMENT_MODE': 'false'
    })
    
    # Configure default API keys if not provided
    if not os.environ.get('OPENAI_API_KEY'):
        print('Warning: OPENAI_API_KEY is not set')
    
    if not os.environ.get('ALPHA_VANTAGE_API_KEY'):
        os.environ['ALPHA_VANTAGE_API_KEY'] = '81GVO787XLOHC287'

def start_streamlit_app():
    """Start Streamlit application with production settings"""
    
    # Get port from environment or use default
    port = os.environ.get('PORT', '5000')
    
    # Build command with production flags
    cmd = [
        sys.executable, '-m', 'streamlit', 'run', 'main.py',
        '--server.port', port,
        '--server.address', '0.0.0.0',
        '--server.headless', 'true',
        '--server.enableCORS', 'false',
        '--server.enableXsrfProtection', 'false',
        '--browser.gatherUsageStats', 'false'
    ]
    
    print(f"🚀 Starting QUANTFIN SOCIETY RESEARCH on port {port}")
    print(f"🔧 Command: {' '.join(cmd)}")
    
    try:
        subprocess.run(cmd, check=True)
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    setup_production_environment()
    start_streamlit_app()