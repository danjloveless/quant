# 🚀 QUANTFIN SOCIETY RESEARCH - Ultra-Fast Professional Event Study Analysis Platform

[![Version](https://img.shields.io/badge/version-v2.2.0-blue.svg)](https://github.com/QuantFin-Exeter/quant/releases/tag/v2.2.0)
[![Status](https://img.shields.io/badge/status-active-success.svg)](https://quantfin.it.com/)
[![Platform](https://img.shields.io/badge/platform-independent-brightgreen.svg)](https://github.com/QuantFin-Exeter/quant)

**Latest Update: TradingView-like UI with modern design and ultra-fast performance**

## ⚡ Ultra-Fast Professional Event Study Analysis Platform

This is a professional quantitative finance platform for event study analysis, reorganized into distinct sections for better maintainability and development workflow.

## 📁 Repository Structure

### 🖥️ **src/** - Core Application Source Code
- **frontend/** - User interface and frontend logic
  - `main.py` - Primary Streamlit application
  - `app.py` - HTTP server compatibility layer
  - `streamlit_app.py` - Alternative Streamlit entry point
  - `main_dark.py` - Dark theme variant
  - `pwa_integration.py` - Progressive Web App integration
  - `service-worker.js` - Service worker for PWA

- **backend/** - Analysis engines and AI-powered insights
  - `analysis.py` - Core quantitative analysis algorithms
  - `advanced_gpt_analyst.py` - AI-powered market analysis
  - `openai_market_analyst.py` - OpenAI integration for market insights
  - `gpt_news_detector.py` - Financial news detection system

- **data/** - Data ingestion and market data handling
  - `market.py` - Market data collection and operations
  - `alpha_vantage_data.py` - Alpha Vantage API integration
  - `asset_search.py` - Asset search and discovery

### 🏗️ **infrastructure/** - Deployment and Configuration
- **deployment/** - Cloud platform deployment scripts
  - `startup.py` - Production startup script
  - `deploy_main.py` - Main deployment entry point
  - `startup_render.sh` - Render-specific startup
  - `deploy.sh` - Shell deployment script
  - `deploy_all.py` - Multi-platform deployment
  - `Procfile` - Heroku process configuration

- **config/** - Configuration files and dependencies
  - `pyproject.toml` - Python project metadata and dependencies
  - `requirements.txt` - Python package requirements
  - `manifest.json` - PWA manifest configuration
  - `.streamlit/` - Streamlit server configuration
  - `uv.lock` - UV package manager lock file

### 🛠️ **tools/** - Utility Scripts and Management
- `backup.py` - Data backup and restore utilities
- `monitor.py` - Platform monitoring and health checks
- `update.py` - Update and optimization scripts
- `clear_cache.py` - Cache management
- `install_requirements.py` - Dependency installation
- `run_platform.py` - Platform launcher
- `test_platform.py` - Testing utilities
- `quick_start.py` - Quick setup script
- `docs.py` - Documentation generation

### 📱 **mobile/** - Mobile Applications
- iOS and Android applications for the platform
- See `mobile/README.md` for mobile-specific documentation

### 📚 **docs/** - Documentation
- `README.md` - Main project documentation (original)
- `DEPLOYMENT_GUIDE.md` - Cloud platform deployment guide
- `ESSENTIAL_FILES.md` - File structure documentation
- `FINAL_CHECKPOINT.md` - Project status summary

### 🎨 **assets/** - Static Assets and Resources
- Icons, images, logos, and screenshots
- Favicon files and PWA icons
- Project assets and visual resources

## 🚀 Quick Start

1. **Setup Environment**:
   ```bash
   python tools/quick_start.py setup
   ```

2. **Run Locally**:
   ```bash
   python tools/run_platform.py
   # OR
   streamlit run src/frontend/main.py
   ```

3. **Deploy to Cloud**:
   ```bash
   python infrastructure/deployment/deploy_all.py render
   ```

## 🔑 Environment Variables

Create `.env` file in the root directory:
```env
OPENAI_API_KEY=your_openai_api_key_here
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_key_here
```

## 📖 Documentation

- **Quick Start**: See `tools/quick_start.py`
- **Deployment**: See `docs/DEPLOYMENT_GUIDE.md`
- **API Documentation**: Run `python tools/docs.py api`
- **User Guide**: Run `python tools/docs.py user`

## 🔧 Development

- **Test Platform**: `python tools/test_platform.py`
- **Monitor Health**: `python tools/monitor.py`
- **Update Dependencies**: `python tools/update.py dependencies`
- **Generate Documentation**: `python tools/docs.py all`

## 📊 Analysis Methods

- **CAPM Model**: Capital Asset Pricing Model
- **Abnormal Returns**: AR = R_actual - R_expected
- **Cumulative AR**: CAR = Σ(AR) over event window
- **Statistical Testing**: T-tests for significance
- **AI Analysis**: GPT-4o powered insights

## 👨‍💻 Developer

**Maksim Kitikov** - QUANTFIN SOCIETY RESEARCH

---

*Professional quantitative finance platform with organized, maintainable codebase*