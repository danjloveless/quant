# QUANTFIN SOCIETY RESEARCH - Essential Files

## Core Application Files

### Main Application
- `main.py` - Primary Streamlit application entry point
- `app.py` - Flask compatibility layer for HTTP servers
- `streamlit_app.py` - Alternative Streamlit entry point

### Analysis Modules
- `analysis.py` - CAPM event study calculations and statistical analysis
- `advanced_gpt_analyst.py` - AI-powered market analysis using GPT-4o
- `openai_market_analyst.py` - OpenAI integration for market insights
- `gpt_news_detector.py` - Automated news event detection
- `market.py` - Market data collection and processing
- `asset_search.py` - Universal asset search functionality
- `alpha_vantage_data.py` - Alternative market data source

### Deployment and Configuration
- `startup.py` - Production startup script
- `deploy_main.py` - Deployment entry point
- `startup_render.sh` - Render-specific startup script
- `deploy.sh` - Deployment shell script
- `install_requirements.py` - Dependency installation script
- `run_platform.py` - Platform launcher

### Configuration Files
- `pyproject.toml` - Python project dependencies and metadata
- `Procfile` - Heroku deployment configuration
- `.streamlit/config.toml` - Streamlit server configuration
- `.gitignore` - Git ignore patterns
- `manifest.json` - PWA manifest file
- `service-worker.js` - Progressive Web App service worker

### Documentation
- `README.md` - Main project documentation
- `DEPLOYMENT_GUIDE.md` - Cloud platform deployment instructions
- `FINAL_CHECKPOINT.md` - Project status and features summary

### Assets and Static Files
- `static/` - Static assets (icons, favicon)
- `attached_assets/` - Project images and screenshots
- `mobile/` - Mobile application files

## File Purposes

### Application Entry Points
- **main.py**: Primary application with full functionality
- **app.py**: HTTP server compatibility layer
- **startup.py**: Production environment configuration

### Analysis Engine
- **analysis.py**: Core quantitative analysis algorithms
- **advanced_gpt_analyst.py**: AI-powered market analysis
- **market.py**: Data collection and market operations

### Deployment
- **startup_render.sh**: Render cloud platform startup
- **deploy_main.py**: Production deployment entry point
- **Procfile**: Heroku process configuration

### Configuration
- **pyproject.toml**: Python dependencies and project metadata
- **.streamlit/config.toml**: Streamlit server settings
- **.gitignore**: Version control exclusions

## Development Workflow

1. **Local Development**: Use `python run_platform.py` or `streamlit run main.py`
2. **Testing**: Run individual modules for specific functionality
3. **Production**: Use `startup.py` or platform-specific scripts
4. **Deployment**: Follow `DEPLOYMENT_GUIDE.md` for cloud platforms

## File Dependencies

- **main.py** depends on: analysis.py, market.py, advanced_gpt_analyst.py
- **analysis.py** depends on: market.py, alpha_vantage_data.py
- **advanced_gpt_analyst.py** depends on: openai_market_analyst.py
- **startup.py** depends on: main.py and environment variables

All files are designed to work together as a cohesive quantitative finance analysis platform.