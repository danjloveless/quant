#!/bin/bash
# Fast deployment script for QUANTFIN SOCIETY RESEARCH platform
# Optimized for quick deployment with minimal overhead

echo "🚀 Deploying QUANTFIN SOCIETY RESEARCH platform..."

# Set optimized environment variables
export STREAMLIT_SERVER_PORT=${PORT:-5000}
export STREAMLIT_SERVER_ADDRESS=0.0.0.0
export STREAMLIT_SERVER_HEADLESS=true
export STREAMLIT_SERVER_ENABLE_CORS=false
export STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION=false
export STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Performance optimizations
export STREAMLIT_SERVER_MAX_UPLOAD_SIZE=200
export STREAMLIT_SERVER_FILE_WATCHER_TYPE=none

# Validate API keys
if [ -z "$OPENAI_API_KEY" ]; then
    echo "⚠️  Warning: OPENAI_API_KEY not set"
fi

if [ -z "$ALPHA_VANTAGE_API_KEY" ]; then
    echo "⚠️  Warning: ALPHA_VANTAGE_API_KEY not set"
fi

echo "🌐 Starting platform on port $STREAMLIT_SERVER_PORT..."

# Start the application
streamlit run main.py