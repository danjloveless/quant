#!/usr/bin/env python3
"""
QUANTFIN SOCIETY RESEARCH - Deployment-Ready Entry Point
Ensures port 5000 opens correctly for Replit deployment
"""

import os
import sys
import subprocess
import time

# Force port 5000 configuration
os.environ['STREAMLIT_SERVER_PORT'] = '5000'
os.environ['STREAMLIT_SERVER_ADDRESS'] = '0.0.0.0'
os.environ['STREAMLIT_SERVER_HEADLESS'] = 'true'
os.environ['STREAMLIT_SERVER_ENABLE_CORS'] = 'false'
os.environ['STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION'] = 'false'
os.environ['STREAMLIT_BROWSER_GATHER_USAGE_STATS'] = 'false'

# Configure API keys
if not os.environ.get('OPENAI_API_KEY'):
    print('Warning: OPENAI_API_KEY not set')
if not os.environ.get('ALPHA_VANTAGE_API_KEY'):
    os.environ['ALPHA_VANTAGE_API_KEY'] = '81GVO787XLOHC287'

# Import the main application after setting environment
import main