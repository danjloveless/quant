#!/bin/bash
# Optimized startup script for Render deployment
# Fast initialization with minimal overhead

# Set Streamlit environment variables for fast startup
export STREAMLIT_SERVER_PORT=$PORT
export STREAMLIT_SERVER_ADDRESS=0.0.0.0
export STREAMLIT_SERVER_HEADLESS=true
export STREAMLIT_SERVER_ENABLE_CORS=false
export STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION=false
export STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Performance optimizations
export STREAMLIT_SERVER_MAX_UPLOAD_SIZE=200
export STREAMLIT_SERVER_FILE_WATCHER_TYPE=none

# Start application
streamlit run main.py
