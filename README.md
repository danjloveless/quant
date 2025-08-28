# QUANTFIN SOCIETY RESEARCH
## Professional Event Study Analysis Platform

### 🎯 Overview
Advanced quantitative finance platform for automated event study analysis using AI-powered news detection and CAPM-based abnormal returns modeling.

### ✨ Key Features
- **AI News Detection**: Automatic identification of market-moving events
- **CAPM Analysis**: Professional abnormal returns calculation
- **Interactive Charts**: Real-time visualization with Plotly
- **Multi-Asset Support**: Stocks, ETFs, indices, and more
- **Cross-Platform**: Works on Mac, Windows, and Linux

### 🚀 Quick Start

#### 1. Installation
```bash
# Install Python dependencies
python install_requirements.py

# Or install manually
pip install streamlit pandas numpy plotly scipy yfinance openai requests trafilatura python-dotenv polygon polygon-api-client
```

#### 2. Configuration
Create `.env` file with your API keys:
```bash
OPENAI_API_KEY=your_openai_api_key_here
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_key_here
```

#### 3. Launch Platform
```bash
# Easy launch
python run_platform.py

# Or direct launch
streamlit run main.py --server.port 5000
```

### 📋 System Requirements
- **Python**: 3.11 or higher
- **OS**: Windows 10+, macOS 10.15+, Linux
- **RAM**: 4GB minimum (8GB recommended)
- **Internet**: Required for API calls

### 🔧 Core Files
- `main.py` - Main Streamlit application
- `advanced_gpt_analyst.py` - AI analysis engine
- `analysis.py` - CAPM event study calculations
- `market.py` - Market data collection
- `asset_search.py` - Universal asset search
- `alpha_vantage_data.py` - Alternative data source

### 🌐 Usage
1. Select analysis mode (Manual or AI Detection)
2. Choose event date and description
3. Select assets for analysis
4. Run comprehensive event study
5. Review statistical results and AI insights

### 🛠️ Troubleshooting

**Installation Issues:**
```bash
# Force reinstall dependencies
python install_requirements.py

# Check Python version
python --version  # Should be 3.11+
```

**API Issues:**
- Verify API keys in `.env` file
- Check internet connection
- Ensure sufficient API quotas

### 👨‍💻 Developer
**Maksim Kitikov** - QUANTFIN SOCIETY RESEARCH

---
*Professional quantitative finance analysis platform*