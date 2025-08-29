# Source Code - Core Application

This directory contains the main source code for the QUANTFIN SOCIETY RESEARCH platform, organized into logical components.

## Directory Structure

### 🖥️ frontend/
Contains all user interface and frontend-related code:
- **main.py** - Primary Streamlit application with full functionality
- **app.py** - HTTP server compatibility layer for deployment
- **streamlit_app.py** - Alternative Streamlit entry point
- **main_dark.py** - Dark theme variant of the main application
- **pwa_integration.py** - Progressive Web App integration features
- **service-worker.js** - Service worker for offline functionality

### 🧠 backend/
Contains analysis engines and AI-powered components:
- **analysis.py** - Core quantitative analysis algorithms and CAPM implementation
- **advanced_gpt_analyst.py** - AI-powered market analysis with GPT-4o
- **openai_market_analyst.py** - OpenAI integration for market insights
- **gpt_news_detector.py** - Financial news detection and analysis system

### 📊 data/
Contains data ingestion and market data handling:
- **market.py** - Market data collection and reaction detection
- **alpha_vantage_data.py** - Alpha Vantage API integration
- **asset_search.py** - Asset search and discovery functionality

## Usage

### Running the Frontend
```bash
# From project root
streamlit run src/frontend/main.py

# Or use the platform launcher
python tools/run_platform.py
```

### Using Backend Components
```python
# Example: Using the analysis engine
from src.backend.analysis import EventStudyAnalyzer
from src.data.market import MarketAnalyzer

analyzer = EventStudyAnalyzer()
market = MarketAnalyzer()
# ... use the components
```

### Data Integration
```python
# Example: Market data collection
from src.data.market import MarketAnalyzer
from src.data.alpha_vantage_data import AlphaVantageData

market_analyzer = MarketAnalyzer()
data_provider = AlphaVantageData()
# ... collect and analyze data
```

## Development Guidelines

1. **Frontend components** should focus on UI/UX and user interaction
2. **Backend components** should contain business logic and analysis algorithms
3. **Data components** should handle external data sources and preprocessing
4. Keep imports clean and use relative imports within each section
5. Maintain separation of concerns between the three layers

## Dependencies

All components depend on the packages defined in `infrastructure/config/pyproject.toml`.
Core dependencies include:
- Streamlit (frontend)
- OpenAI (backend AI components)
- yfinance, pandas, numpy (data and analysis)
- plotly (visualization)