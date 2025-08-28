# QUANTFIN SOCIETY RESEARCH - Essential Files

## Core Platform Files (Required)

### Main Application
- `main.py` - Main Streamlit web application interface
- `advanced_gpt_analyst.py` - AI-powered market analysis engine
- `analysis.py` - CAPM event study calculations and statistical testing
- `market.py` - Market data collection and processing
- `asset_search.py` - Universal asset search across all financial instruments
- `alpha_vantage_data.py` - Alternative financial data source
- `openai_market_analyst.py` - AI market interpretation module

### Setup & Configuration
- `install_requirements.py` - Cross-platform dependency installer
- `run_platform.py` - Universal launcher for Mac/Windows
- `pyproject.toml` - Package configuration
- `.env` - API keys and environment variables
- `replit.md` - Project documentation and architecture

### Supporting Files
- `README.md` - Platform documentation and usage guide
- `generated-icon.png` - Platform icon
- `.replit` - Replit configuration

## File Dependencies Map

```
main.py
├── advanced_gpt_analyst.py (AI analysis)
├── analysis.py (CAPM calculations)
├── market.py (data collection)
├── asset_search.py (asset lookup)
├── alpha_vantage_data.py (backup data)
└── openai_market_analyst.py (AI interpretation)
```

## Cross-Platform Compatibility

### Windows Launch
```cmd
python install_requirements.py
python run_platform.py
```

### Mac/Linux Launch
```bash
python3 install_requirements.py
python3 run_platform.py
```

### Manual Launch
```bash
streamlit run main.py --server.port 5000
```

## Required API Keys
- OPENAI_API_KEY (Essential)
- ALPHA_VANTAGE_API_KEY (Backup data)
- POLYGON_API_KEY (Optional)

## Minimum System Requirements
- Python 3.11+
- 4GB RAM
- Internet connection
- 500MB storage

Total Essential Files: 11 core files for full functionality