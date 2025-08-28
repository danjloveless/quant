#!/usr/bin/env python3
"""
Fast documentation generator for QUANTFIN SOCIETY RESEARCH platform.
Quick generation of comprehensive documentation.
"""

import os
import sys
from pathlib import Path
from datetime import datetime

def create_quick_start():
    """Create quick start guide"""
    
    content = """# QUANTFIN SOCIETY RESEARCH - Quick Start Guide

## 🚀 Fast Setup (5 minutes)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure API Keys
Create `.env` file:
```env
OPENAI_API_KEY=your_openai_api_key_here
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_key_here
```

### 3. Launch Platform
```bash
python startup.py
```

### 4. Access Platform
Open browser: http://localhost:5000

## 🎯 Quick Analysis

1. **Select Mode**: Choose "Manual Event Study" or "AI News Detection"
2. **Set Date**: Pick event date for analysis
3. **Add Assets**: Enter stock symbols (one per line)
4. **Run Analysis**: Click "Run Analysis" button
5. **Review Results**: Check charts and statistics

## 📊 Key Features

- **AI News Detection**: Automatic market event identification
- **CAPM Analysis**: Professional abnormal returns calculation
- **Interactive Charts**: Real-time visualization
- **Multi-Asset Support**: Analyze stocks, ETFs, indices
- **Statistical Validation**: T-tests and significance testing

## 🔧 Troubleshooting

**Installation Issues:**
```bash
python install_requirements.py
```

**API Issues:**
- Verify API keys in `.env` file
- Check internet connection
- Ensure sufficient API quotas

**Performance Issues:**
```bash
python update.py optimize
```

## 📞 Support

For issues and questions:
- Check troubleshooting section
- Review error messages
- Verify system requirements

---
*Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""
    
    with open('QUICK_START.md', 'w') as f:
        f.write(content)
    
    print("✅ Quick Start Guide created!")

def create_api_docs():
    """Create API documentation"""
    
    content = """# QUANTFIN SOCIETY RESEARCH - API Documentation

## 🔑 Required API Keys

### OpenAI API Key
- **Purpose**: AI-powered news analysis and market insights
- **Setup**: Get from https://platform.openai.com/api-keys
- **Usage**: GPT-4o analysis for market events

### Alpha Vantage API Key
- **Purpose**: Financial market data and real-time quotes
- **Setup**: Get from https://www.alphavantage.co/support/#api-key
- **Usage**: Stock prices, technical indicators, fundamental data

## 🌐 Environment Variables

```env
# Required
OPENAI_API_KEY=sk-...
ALPHA_VANTAGE_API_KEY=...

# Optional
STREAMLIT_SERVER_PORT=5000
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_SERVER_ENABLE_CORS=false
STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION=false
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
```

## 📊 Data Sources

### Primary Sources
- **Yahoo Finance**: Real-time stock data via yfinance
- **Alpha Vantage**: Alternative data source
- **OpenAI GPT-4o**: AI analysis and insights

### Supported Assets
- **Stocks**: AAPL, MSFT, GOOGL, etc.
- **ETFs**: SPY, QQQ, IWM, etc.
- **Indices**: ^GSPC, ^DJI, ^IXIC, etc.
- **Cryptocurrencies**: BTC-USD, ETH-USD, etc.
- **Forex**: EURUSD=X, GBPUSD=X, etc.

## 🔧 API Limits

### OpenAI
- **Rate Limit**: Varies by plan
- **Usage**: Per API call
- **Cost**: ~$0.01-0.10 per analysis

### Alpha Vantage
- **Free Tier**: 5 API calls per minute, 500 per day
- **Premium**: Higher limits available
- **Usage**: Per data request

## 📈 Analysis Methods

### Event Study Analysis
- **CAPM Model**: Capital Asset Pricing Model
- **Abnormal Returns**: AR = R_actual - R_expected
- **Cumulative AR**: CAR = Σ(AR) over event window
- **Statistical Testing**: T-tests for significance

### AI Analysis
- **News Detection**: Automatic event identification
- **Impact Assessment**: Market reaction analysis
- **Sentiment Analysis**: News sentiment scoring
- **Forecasting**: Market direction predictions

---
*Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""
    
    with open('API_DOCS.md', 'w') as f:
        f.write(content)
    
    print("✅ API Documentation created!")

def create_deployment_docs():
    """Create deployment documentation"""
    
    content = """# QUANTFIN SOCIETY RESEARCH - Deployment Guide

## 🚀 Quick Deployment

### Render (Recommended)
1. **Connect Repository**: Link GitHub repo to Render
2. **Configure Service**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `./startup_render.sh`
3. **Set Environment Variables**:
   - `OPENAI_API_KEY`
   - `ALPHA_VANTAGE_API_KEY`
4. **Deploy**: Automatic deployment on push

### Railway
1. **Connect Repository**: Link GitHub repo to Railway
2. **Auto-Deploy**: Automatic deployment enabled
3. **Environment Variables**: Set in Railway dashboard
4. **Custom Domain**: Configure in settings

### Heroku
1. **Create App**: New Heroku app
2. **Connect Git**: Link repository
3. **Set Config Vars**: Add API keys
4. **Deploy**: `git push heroku main`

### Vercel
1. **Import Project**: Connect GitHub repository
2. **Framework Preset**: Python
3. **Build Settings**: Auto-detected
4. **Environment Variables**: Add in dashboard

### Fly.io
1. **Install CLI**: `curl -L https://fly.io/install.sh | sh`
2. **Login**: `fly auth login`
3. **Launch**: `fly launch`
4. **Deploy**: `fly deploy`

## 🔧 Environment Setup

### Required Variables
```bash
OPENAI_API_KEY=sk-...
ALPHA_VANTAGE_API_KEY=...
PORT=5000  # Auto-detected by most platforms
```

### Optional Variables
```bash
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_SERVER_ENABLE_CORS=false
STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION=false
```

## 📊 Performance Optimization

### Render
- **Instance Type**: Free tier (sleep after 15 min)
- **Upgrade**: $7/month for always-on
- **Custom Domain**: Supported

### Railway
- **Free Tier**: $5 credit monthly
- **Paid Plans**: Pay-per-use
- **Custom Domain**: Supported

### Heroku
- **Free Tier**: Discontinued
- **Paid Plans**: $7/month basic dyno
- **Custom Domain**: Supported

### Vercel
- **Free Tier**: 100GB bandwidth
- **Pro Plan**: $20/month
- **Custom Domain**: Supported

### Fly.io
- **Free Tier**: 3 shared-cpu VMs
- **Paid Plans**: Pay-per-use
- **Custom Domain**: Supported

## 🔍 Troubleshooting

### Common Issues
1. **Build Failures**: Check requirements.txt
2. **Runtime Errors**: Verify environment variables
3. **Port Issues**: Ensure PORT variable is set
4. **API Errors**: Check API key configuration

### Debug Commands
```bash
# Test locally
python test_platform.py

# Check dependencies
python -c "import streamlit, pandas, numpy, plotly, yfinance, openai"

# Monitor platform
python monitor.py
```

---
*Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""
    
    with open('DEPLOYMENT_DOCS.md', 'w') as f:
        f.write(content)
    
    print("✅ Deployment Documentation created!")

def create_user_guide():
    """Create comprehensive user guide"""
    
    content = """# QUANTFIN SOCIETY RESEARCH - User Guide

## 🎯 Platform Overview

QUANTFIN SOCIETY RESEARCH is a professional quantitative finance platform for automated event study analysis using AI-powered news detection and CAPM-based abnormal returns modeling.

## 📊 Analysis Modes

### 1. Manual Event Study
- **Use Case**: Known market events
- **Input**: Event date and description
- **Output**: Statistical analysis and charts

### 2. AI News Detection
- **Use Case**: Unknown market events
- **Input**: Date range for analysis
- **Output**: AI-detected events + analysis

## 🔧 Step-by-Step Guide

### Step 1: Platform Setup
1. **Install Dependencies**: `pip install -r requirements.txt`
2. **Configure API Keys**: Create `.env` file
3. **Launch Platform**: `python startup.py`
4. **Access Interface**: http://localhost:5000

### Step 2: Analysis Configuration
1. **Select Mode**: Choose analysis approach
2. **Set Date**: Pick event date
3. **Describe Event**: Provide event details
4. **Add Assets**: Enter stock symbols

### Step 3: Run Analysis
1. **Click "Run Analysis"**: Start processing
2. **Wait for Results**: Processing time varies
3. **Review Output**: Check all tabs

### Step 4: Interpret Results
1. **Summary Tab**: Key metrics and statistics
2. **Charts Tab**: Interactive visualizations
3. **AI Insights Tab**: AI-generated analysis

## 📈 Understanding Results

### Key Metrics
- **CAR (Cumulative Abnormal Return)**: Total abnormal return over event window
- **T-Statistic**: Statistical significance measure
- **P-Value**: Probability of random occurrence
- **Beta**: Market sensitivity measure

### Statistical Significance
- **P < 0.01**: Highly significant (99% confidence)
- **P < 0.05**: Significant (95% confidence)
- **P < 0.10**: Marginally significant (90% confidence)
- **P > 0.10**: Not significant

### Chart Interpretation
- **Abnormal Returns**: Daily deviations from expected returns
- **Cumulative AR**: Running sum of abnormal returns
- **Event Window**: Period around event date
- **Confidence Intervals**: Statistical significance bands

## 🎯 Best Practices

### Event Selection
- **Choose Significant Events**: Major announcements, earnings, policy changes
- **Avoid Market Holidays**: Ensure trading activity
- **Consider Market Hours**: Use trading day dates

### Asset Selection
- **Diversify**: Include different sectors and sizes
- **Relevance**: Choose assets directly affected by event
- **Liquidity**: Prefer highly traded securities

### Analysis Parameters
- **Estimation Window**: 60-252 days (standard practice)
- **Event Window**: 3-11 days (typical range)
- **Market Benchmark**: S&P 500 or relevant index

## 🔍 Advanced Features

### AI Analysis
- **News Detection**: Automatic event identification
- **Impact Assessment**: Market reaction analysis
- **Sentiment Analysis**: News sentiment scoring
- **Forecasting**: Market direction predictions

### Custom Analysis
- **Multiple Events**: Compare different events
- **Sector Analysis**: Industry-specific studies
- **Cross-Asset**: Multi-asset comparisons
- **Time Series**: Historical event analysis

## 🛠️ Troubleshooting

### Common Issues
1. **No Data**: Check asset symbols and date range
2. **API Errors**: Verify API keys and quotas
3. **Slow Performance**: Check internet connection
4. **Calculation Errors**: Verify input parameters

### Performance Tips
1. **Limit Assets**: Analyze 5-10 assets at once
2. **Optimize Windows**: Use standard estimation periods
3. **Cache Results**: Platform caches for speed
4. **Update Dependencies**: Keep packages current

## 📞 Support

### Getting Help
1. **Check Documentation**: Review this guide
2. **Test Platform**: Run `python test_platform.py`
3. **Monitor Performance**: Use `python monitor.py`
4. **Update Platform**: Run `python update.py all`

### System Requirements
- **Python**: 3.11 or higher
- **RAM**: 4GB minimum (8GB recommended)
- **Internet**: Required for API calls
- **Browser**: Modern web browser

---
*Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""
    
    with open('USER_GUIDE.md', 'w') as f:
        f.write(content)
    
    print("✅ User Guide created!")

def main():
    """Main documentation generator"""
    
    if len(sys.argv) < 2:
        print("📚 QUANTFIN SOCIETY RESEARCH - Documentation Generator")
        print("Usage:")
        print("  python docs.py quick     - Create Quick Start Guide")
        print("  python docs.py api       - Create API Documentation")
        print("  python docs.py deploy    - Create Deployment Guide")
        print("  python docs.py user      - Create User Guide")
        print("  python docs.py all       - Create all documentation")
        return
    
    command = sys.argv[1]
    
    if command == "quick":
        create_quick_start()
    elif command == "api":
        create_api_docs()
    elif command == "deploy":
        create_deployment_docs()
    elif command == "user":
        create_user_guide()
    elif command == "all":
        print("📚 Creating all documentation...")
        create_quick_start()
        create_api_docs()
        create_deployment_docs()
        create_user_guide()
        print("✅ All documentation created!")
    else:
        print(f"❌ Unknown command: {command}")

if __name__ == "__main__":
    main()
