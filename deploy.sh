#!/bin/bash
# QUANTFIN SOCIETY RESEARCH - Deployment Script

# Set environment variables
export STREAMLIT_SERVER_PORT=5000
export STREAMLIT_SERVER_ADDRESS=0.0.0.0
export STREAMLIT_SERVER_HEADLESS=true
export STREAMLIT_SERVER_ENABLE_CORS=false
export STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION=false
export STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Configure API keys
export OPENAI_API_KEY="${OPENAI_API_KEY:-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}"
export ALPHA_VANTAGE_API_KEY="${ALPHA_VANTAGE_API_KEY:-81GVO787XLOHC287}"

# Start Streamlit on port 5000
streamlit run main.py \
    --server.port=5000 \
    --server.address=0.0.0.0 \
    --server.headless=true \
    --server.enableCORS=false \
    --server.enableXsrfProtection=false \
    --browser.gatherUsageStats=false