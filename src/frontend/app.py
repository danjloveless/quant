#!/usr/bin/env python3
"""
QUANTFIN SOCIETY RESEARCH - Deployment Entry Point
This file serves as a deployment-compatible entry point that imports the main application
"""

import os
import sys

# Force port 5000 configuration for deployment
os.environ['STREAMLIT_SERVER_PORT'] = '5000'
os.environ['STREAMLIT_SERVER_ADDRESS'] = '0.0.0.0'
os.environ['STREAMLIT_SERVER_HEADLESS'] = 'true'
os.environ['STREAMLIT_SERVER_ENABLE_CORS'] = 'false' 
os.environ['STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION'] = 'false'
os.environ['STREAMLIT_BROWSER_GATHER_USAGE_STATS'] = 'false'

# Configure default API keys for deployment
if not os.environ.get('OPENAI_API_KEY'):
    print('Warning: OPENAI_API_KEY is not set')
if not os.environ.get('ALPHA_VANTAGE_API_KEY'):
    os.environ['ALPHA_VANTAGE_API_KEY'] = '81GVO787XLOHC287'

# Import and run the main application
import main