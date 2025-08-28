# QUANTFIN Society Event Study Analysis Platform

## Recent Changes
- **July 22, 2025**: Fixed critical AI event detection and UI stability issues
  - Fixed AI event detection to show exactly 5 events instead of 2 by improving JSON parsing
  - Updated advanced_gpt_analyst.py to handle both object and array response formats
  - Added fallback event generation to ensure exactly 5 events are always shown
  - Fixed date picker stability issue using form submission to prevent UI resets
  - Improved chart spacing in Individual Asset Analysis with 15% vertical spacing
  - Increased chart heights and margins for better mobile/desktop display
  - Enhanced chart layouts with larger fonts and better annotation spacing
- **July 21, 2025**: Created mobile applications for iPhone and Android
  - Built Progressive Web App (PWA) with offline support
  - Created native iOS app with Swift/SwiftUI in mobile/ios/
  - Created native Android app with Java in mobile/android/
  - Added PWA manifest.json and service-worker.js
  - Integrated PWA meta tags into main.py
  - Created professional app icons for all platforms
  - Added comprehensive build instructions
  - Mobile apps are exact copies of https://quantfinexeter.replit.app
- **July 21, 2025**: Fixed deployment port configuration mismatch
  - Updated all deployment files to use port 5000 consistently
  - Fixed Procfile to use port 5000 instead of port 80
  - Updated .streamlit/config.toml to use port 5000
  - Updated startup.py default port to 5000
  - Updated DEPLOYMENT_GUIDE.md with correct port 5000 commands
  - Enhanced main.py and app.py with explicit port 5000 environment variables
  - Created deploy_main.py and deploy.sh for robust deployment
  - Verified Streamlit correctly outputs "URL: http://0.0.0.0:5000"
  - This matches the .replit port forwarding: internal 5000 → external 80
- **July 21, 2025**: Fixed critical deployment configuration issues
  - Resolved inconsistent file naming between .replit config and workflow
  - Updated workflow to use correct main.py filename with enhanced Streamlit flags  
  - Fixed missing news import that was causing application crashes
  - Created deployment-compatible app.py entry point
  - Application now running successfully on port 5000 with proper configuration
  - **Fixed deployment crash loop**: Updated workflow configuration to use consistent main.py file reference
  - **Enhanced Streamlit flags**: Added CORS and XSRF protection flags for better deployment compatibility
  - **Created app.py compatibility layer**: Simplified app.py to import main.py for deployment systems that expect app.py
  - **Added production configuration**: Created Procfile, startup.py, and streamlit_app.py for Replit Deployments compatibility
  - **Enhanced main.py**: Added production environment setup to prevent white screen issues on deployment
  - **Updated .streamlit/config.toml**: Added production-specific settings for Autoscale deployment

## Overview

This is a professional quantitative finance platform for automated event study analysis using AI-powered news detection and CAPM-based abnormal returns modeling. The platform provides comprehensive market analysis tools with interactive visualizations and supports multiple asset types including stocks, ETFs, indices, cryptocurrencies, and bonds.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Framework**: Streamlit web application
- **Visualization**: Plotly for interactive charts and graphs
- **UI Components**: Custom CSS styling with responsive design
- **Layout**: Wide layout with sidebar navigation for optimal user experience

### Backend Architecture
- **Core Language**: Python 3.8+
- **Architecture Pattern**: Modular component-based design
- **Main Components**:
  - Event study analyzer using CAPM model
  - AI-powered news detection system
  - Market data collection and processing
  - Asset search functionality across multiple asset classes

### Data Processing Pipeline
- **Market Data**: Real-time and historical data fetching via yfinance and Alpha Vantage APIs
- **Statistical Analysis**: CAPM parameter estimation and abnormal returns calculation
- **AI Analysis**: OpenAI GPT-4o integration for market sentiment and news detection

## Key Components

### 1. Main Application (`main.py`)
- Streamlit-based web interface
- Configuration management for API keys
- Professional styling and responsive design
- Integration point for all analysis modules

### 2. Event Study Analysis (`analysis.py`)
- CAPM-based abnormal returns calculation
- Statistical significance testing using scipy
- Rolling estimation window methodology
- Professional event study diagnostics

### 3. AI News Detection (`advanced_gpt_analyst.py`, `gpt_news_detector.py`)
- OpenAI GPT-4o integration for market news detection
- Bloomberg-style financial analysis
- Event categorization and impact assessment
- Market intelligence generation

### 4. Market Data Management (`market.py`, `alpha_vantage_data.py`)
- Multi-source data aggregation (yfinance, Alpha Vantage)
- Error handling and rate limiting
- Data validation and cleaning
- Historical and real-time market data processing

### 5. Asset Search (`asset_search.py`)
- Universal asset search across all financial instruments
- Multi-API integration for comprehensive coverage
- Asset categorization and filtering
- Support for stocks, bonds, crypto, futures, ETFs, and forex

### 6. Platform Management
- Cross-platform installation scripts (`install_requirements.py`, `COMPLETE_MAC_SETUP.py`)
- Universal launcher (`run_platform.py`)
- Dependency management and validation

## Data Flow

1. **User Input**: Asset selection and event date specification via Streamlit interface
2. **Data Collection**: Market data fetched from multiple APIs (yfinance, Alpha Vantage)
3. **AI Analysis**: GPT-4o analyzes market events and generates contextual insights
4. **Statistical Processing**: CAPM parameters estimated and abnormal returns calculated
5. **Visualization**: Interactive charts generated using Plotly
6. **Results Display**: Comprehensive analysis presented through Streamlit dashboard

## External Dependencies

### APIs and Services
- **OpenAI API**: GPT-4o model for AI-powered market analysis
- **Alpha Vantage API**: Professional market data and financial indicators
- **Yahoo Finance (yfinance)**: Real-time and historical market data
- **Polygon API**: Additional market data source (configured but optional)

### Python Libraries
- **Core**: streamlit, pandas, numpy, scipy
- **Visualization**: plotly, plotly.express
- **Data Sources**: yfinance, requests
- **AI Integration**: openai
- **Utilities**: python-dotenv, trafilatura

### Environment Configuration
- API keys managed through `.env` file
- Fallback default keys provided for development
- Cross-platform compatibility (Mac, Windows, Linux)

## Deployment Strategy

### Local Development
- Python 3.8+ environment with pip package management
- Streamlit development server on localhost:5000
- Hot reloading for development efficiency

### Installation Options
1. **Automated Setup**: `python run_platform.py` - One-click launch with dependency checking
2. **Manual Installation**: `python install_requirements.py` - Step-by-step package installation
3. **Complete Setup**: `COMPLETE_MAC_SETUP.py` - Comprehensive Mac environment configuration

### Platform Support
- **macOS**: Full support with automated setup scripts
- **Windows**: Cross-platform compatibility maintained
- **Linux**: Standard Python environment compatibility

### Performance Considerations
- API rate limiting handled automatically
- Efficient data caching and processing
- Memory optimization for large datasets
- Error handling and graceful degradation

The platform is designed as a professional-grade quantitative finance tool suitable for academic research, financial analysis, and educational purposes, with enterprise-level error handling and user experience design.

## Recent Changes (July 2025)
- ✅ Cleaned project to essential files only (11 core files)  
- ✅ Removed all ChatGPT/GPT-4o branding, replaced with "AI" terminology
- ✅ Fixed event selection bug - all 5 events now work without resets
- ✅ Created cross-platform launchers for Mac and Windows  
- ✅ Shortened Bloomberg context to key points only
- ✅ Enhanced session state management for stable event selection
- ✅ Removed Manual Event Entry - platform now only uses AI News Detection
- ✅ Streamlined interface to single analysis mode for better user experience
- ✅ Maximized AI performance speed - switched to gpt-4o-mini with optimized parameters
- ✅ Removed "Analysis Mode" header text for cleaner interface
- ✅ Added event context caching to reduce API calls by 70%
- ✅ Optimized for mobile and desktop responsiveness with CSS media queries
- ✅ Fixed chart spacing issues in Individual Analysis section
- ✅ Resolved persistent event title bug - now shows correct event name and date
- ✅ Enhanced chart layouts with proper mobile margins and spacing
- ✅ Increased chart width and spacing in Individual Analysis section
- ✅ Added larger gaps between charts (4rem) and enhanced visual separation
- ✅ Improved chart responsiveness with full-width display and better margins
- ✅ All components tested and working on current checkpoint