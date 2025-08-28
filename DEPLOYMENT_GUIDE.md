# QUANTFIN SOCIETY RESEARCH - Deployment Guide

## Replit Deployments Configuration

This application is optimized for Replit Deployments with Autoscale configuration.

### Entry Points
The application supports multiple entry points for maximum deployment compatibility:

1. **main.py** - Primary application file ✅
2. **app.py** - Deployment compatibility layer ✅ 
3. **streamlit_app.py** - Alternative entry point ✅
4. **startup.py** - Production startup script ✅

### Configuration Files

- **Procfile** - Deployment process configuration
- **.streamlit/config.toml** - Streamlit production settings
- **pyproject.toml** - Python dependencies

### Recommended Deployment Settings

For **Autoscale** deployment with your current configuration:
- 4 vCPUs, 8 GiB RAM per machine
- Max 10 machines
- 880 compute units/s at max traffic

### Deployment Command Options

The application can be started with any of these commands:
```bash
streamlit run main.py --server.port=5000 --server.address=0.0.0.0 --server.headless=true
streamlit run app.py --server.port=5000 --server.address=0.0.0.0 --server.headless=true  
streamlit run streamlit_app.py --server.port=5000 --server.address=0.0.0.0 --server.headless=true
python startup.py
```

### Recommended Run Command for Replit Deployments

Copy this exact command into the "Run command" field:
```
streamlit run main.py --server.port=5000 --server.address=0.0.0.0 --server.headless=true --server.enableCORS=false --server.enableXsrfProtection=false
```

**Note**: This matches the internal port 5000 configuration, which is forwarded to external port 80 by Replit's port forwarding.

### Environment Variables

The application includes default API keys for immediate deployment:
- OPENAI_API_KEY - Configured for GPT-4o market analysis
- ALPHA_VANTAGE_API_KEY - Configured for market data

### Production Optimizations

- Headless server mode enabled
- CORS and XSRF protection disabled for deployment
- Usage stats collection disabled
- Development mode disabled
- Production environment variables configured

### Troubleshooting Deployment Issues

If experiencing deployment failures or white screen:

1. **IMPORTANT**: Use port 5000 for Replit Deployments (matches port forwarding configuration)
2. **Run Command**: Use `streamlit run main.py --server.port=5000 --server.address=0.0.0.0 --server.headless=true`
3. Verify all production environment variables are set (especially STREAMLIT_SERVER_PORT=5000)
4. Check that the deployment uses one of the supported entry points (main.py, app.py, deploy_main.py)
5. Confirm Streamlit outputs "URL: http://0.0.0.0:5000" in logs
6. Ensure .streamlit/config.toml has port = 5000

The application is now fully configured for successful deployment on Replit Deployments with Autoscale.