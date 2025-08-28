import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import yfinance as yf
from scipy import stats
from datetime import datetime, timedelta
import os
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings("ignore")

# Production configuration
def setup_production():
    """Configure production environment settings"""
    os.environ.setdefault('STREAMLIT_SERVER_PORT', '5000')
    os.environ.setdefault('STREAMLIT_SERVER_ADDRESS', '0.0.0.0')
    os.environ.setdefault('STREAMLIT_SERVER_HEADLESS', 'true')
    os.environ.setdefault('STREAMLIT_SERVER_ENABLE_CORS', 'false')
    os.environ.setdefault('STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION', 'false')
    os.environ.setdefault('STREAMLIT_BROWSER_GATHER_USAGE_STATS', 'false')

# Initialize production settings
setup_production()

# Page configuration
st.set_page_config(
    page_title="QUANTFIN SOCIETY RESEARCH",
    page_icon="static/favicon.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Optimized CSS for fast loading
st.markdown("""
<style>
/* Core responsive design */
@media (max-width: 768px) {
    .main .block-container { padding: 1rem; max-width: 100%; }
    .stColumns > div { gap: 0.5rem !important; }
    .quantfin-header { padding: 1.5rem !important; font-size: 0.9rem; }
}

@media (min-width: 769px) {
    .main .block-container { max-width: 1200px; padding: 2rem; }
    .stColumns > div { gap: 2rem !important; }
}

/* Optimized chart styling */
.plotly-graph-div {
    margin-bottom: 1rem !important;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 0.5rem;
}

/* Header styling */
.quantfin-header {
    background: linear-gradient(135deg, #0f4c75 0%, #3282b8 100%);
    color: white;
    padding: 2rem;
    border-radius: 10px;
    text-align: center;
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 16px rgba(0,0,0,0.1);
}

/* Metric styling */
.metric-box {
    background: white;
    padding: 1rem;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    margin: 0.5rem 0;
}

/* Success alert */
.success-alert {
    background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
    border-radius: 8px;
    padding: 1rem;
    margin: 0.5rem 0;
    color: #155724;
}

/* Date picker optimization */
.stDateInput > div > div { position: relative; z-index: 1000; }
.stDateInput [data-baseweb="calendar"] {
    position: absolute;
    z-index: 1001 !important;
    background: white;
    border: 1px solid #3282b8;
    border-radius: 8px;
    box-shadow: 0 4px 16px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

# Add favicon
st.markdown("""
<link rel="shortcut icon" href="static/favicon.png" type="image/png">
<link rel="icon" href="static/favicon.ico" type="image/x-icon">
""", unsafe_allow_html=True)

# Lazy-initialized components to speed up first paint
class NewsAnalyzer:
    """Financial news detection and analysis system"""
    
    def __init__(self):
        from gpt_news_detector import GPTNewsDetector
        self.news_collector = GPTNewsDetector()
    
    def fetch_financial_news(self, date_str, keywords=None):
        """Fetch financial news for specific date"""
        try:
            return self.news_collector.detect_market_events(date_str, keywords)
        except Exception as e:
            st.error(f"News fetch error: {e}")
            return []

class EventStudyAnalyzer:
    """CAPM-based event study analysis system"""
    
    def __init__(self):
        from analysis import EventStudyAnalysis
        self.analyzer = EventStudyAnalysis()
    
    def run_analysis(self, event_date, event_description, assets, estimation_window=252, event_window=11):
        """Run comprehensive event study analysis"""
        try:
            return self.analyzer.perform_event_study(
                event_date, event_description, assets, 
                estimation_window, event_window
            )
        except Exception as e:
            st.error(f"Analysis error: {e}")
            return None

class MarketDataManager:
    """Market data collection and management"""
    
    def __init__(self):
        from market import MarketDataCollector
        self.collector = MarketDataCollector()
    
    def get_asset_data(self, symbol, start_date, end_date):
        """Get market data for asset"""
        try:
            return self.collector.get_stock_data(symbol, start_date, end_date)
        except Exception as e:
            st.error(f"Data fetch error for {symbol}: {e}")
            return None

class AssetSearcher:
    """Universal asset search functionality"""
    
    def __init__(self):
        from asset_search import AssetSearch
        self.searcher = AssetSearch()
    
    def search_assets(self, query):
        """Search for financial assets"""
        try:
            return self.searcher.search(query)
        except Exception as e:
            st.error(f"Search error: {e}")
            return []

class AIAnalyst:
    """AI-powered market analysis"""
    
    def __init__(self):
        from advanced_gpt_analyst import AdvancedGPTAnalyst
        self.analyst = AdvancedGPTAnalyst()
    
    def analyze_market_impact(self, event_data, market_data):
        """Analyze market impact using AI"""
        try:
            return self.analyst.analyze_event_impact(event_data, market_data)
        except Exception as e:
            st.error(f"AI analysis error: {e}")
            return None

# Cached getters (lazy creation on first use)
@st.cache_resource
def get_news_analyzer() -> NewsAnalyzer:
    return NewsAnalyzer()

@st.cache_resource
def get_event_study_analyzer() -> EventStudyAnalyzer:
    return EventStudyAnalyzer()

@st.cache_resource
def get_market_data_manager() -> MarketDataManager:
    return MarketDataManager()

@st.cache_resource
def get_asset_searcher() -> AssetSearcher:
    return AssetSearcher()

@st.cache_resource
def get_ai_analyst() -> AIAnalyst:
    return AIAnalyst()

# Main application
def main():
    """Main application function"""
    
    # Header
    st.markdown("""
    <div class="quantfin-header">
        <h1>QUANTFIN SOCIETY RESEARCH</h1>
        <p>Professional Event Study Analysis Platform</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar configuration
    with st.sidebar:
        st.header("Analysis Configuration")
        
        # Analysis mode selection
        analysis_mode = st.selectbox(
            "Analysis Mode",
            ["Manual Event Study", "AI News Detection"],
            help="Choose analysis approach"
        )
        
        # Event date selection
        event_date = st.date_input(
            "Event Date",
            value=datetime.now().date(),
            help="Select the event date for analysis"
        )
        
        # Event description
        event_description = st.text_area(
            "Event Description",
            placeholder="Describe the market event...",
            help="Provide details about the event"
        )
        
        # Asset selection
        assets_input = st.text_area(
            "Assets (one per line)",
            placeholder="AAPL\nMSFT\nGOOGL",
            help="Enter asset symbols, one per line"
        )
        
        # Analysis parameters
        estimation_window = st.slider(
            "Estimation Window (days)",
            min_value=60,
            max_value=500,
            value=252,
            help="Period for CAPM estimation"
        )
        
        event_window = st.slider(
            "Event Window (days)",
            min_value=1,
            max_value=21,
            value=11,
            help="Period around event date"
        )
    
    # Main content area
    if st.button("Run Analysis", type="primary"):
        if not assets_input.strip():
            st.error("Please enter at least one asset symbol")
            return
        
        # Parse assets
        assets = [asset.strip().upper() for asset in assets_input.split('\n') if asset.strip()]
        
        # Run analysis based on mode
        if analysis_mode == "Manual Event Study":
            run_manual_analysis(event_date, event_description, assets, estimation_window, event_window)
        else:
            run_ai_analysis(event_date, event_description, assets, estimation_window, event_window)

def run_manual_analysis(event_date, event_description, assets, estimation_window, event_window):
    """Run manual event study analysis"""
    
    with st.spinner("Running event study analysis..."):
        analyzer = get_event_study_analyzer()
        results = analyzer.run_analysis(
            event_date, event_description, assets, estimation_window, event_window
        )
        
        if results:
            display_results(results, assets)

def run_ai_analysis(event_date, event_description, assets, estimation_window, event_window):
    """Run AI-powered analysis"""
    
    with st.spinner("Running AI-powered analysis..."):
        # Fetch news data (cached analyzer, I/O happens only on first call per session)
        news = get_news_analyzer()
        news_data = news.fetch_financial_news(str(event_date))
        
        analyzer = get_event_study_analyzer()
        results = analyzer.run_analysis(
            event_date, event_description, assets, estimation_window, event_window
        )
        
        if results:
            ai = get_ai_analyst()
            ai_insights = ai.analyze_market_impact(
                {'date': event_date, 'description': event_description, 'news': news_data},
                results
            )
            
            display_results(results, assets, ai_insights)

def display_results(results, assets, ai_insights=None):
    """Display analysis results"""
    
    # Summary metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Assets Analyzed", len(assets))
    
    with col2:
        st.metric("Event Date", results.get('event_date', 'N/A'))
    
    with col3:
        st.metric("Estimation Window", f"{results.get('estimation_window', 0)} days")
    
    with col4:
        st.metric("Event Window", f"{results.get('event_window', 0)} days")
    
    # Results tabs
    tab1, tab2, tab3 = st.tabs(["📊 Analysis Results", "📈 Charts", "🤖 AI Insights"])
    
    with tab1:
        display_analysis_results(results)
    
    with tab2:
        display_charts(results)
    
    with tab3:
        if ai_insights:
            display_ai_insights(ai_insights)
        else:
            st.info("AI insights available with AI News Detection mode")

def display_analysis_results(results):
    """Display detailed analysis results"""
    
    if 'abnormal_returns' in results:
        st.subheader("Abnormal Returns Analysis")
        
        # Convert to DataFrame for display
        ar_df = pd.DataFrame(results['abnormal_returns'])
        st.dataframe(ar_df, use_container_width=True)
        
        # Statistical summary
        if 'statistics' in results:
            st.subheader("Statistical Summary")
            stats_df = pd.DataFrame(results['statistics'])
            st.dataframe(stats_df, use_container_width=True)

def display_charts(results):
    """Display interactive charts"""
    
    if 'charts' in results:
        st.subheader("Interactive Charts")
        
        # Display each chart
        for chart_name, chart_data in results['charts'].items():
            st.plotly_chart(chart_data, use_container_width=True)

def display_ai_insights(ai_insights):
    """Display AI-generated insights"""
    
    st.subheader("AI Market Analysis")
    
    if isinstance(ai_insights, dict):
        for key, value in ai_insights.items():
            st.markdown(f"**{key}:** {value}")
    else:
        st.write(ai_insights)

# Run the application
if __name__ == "__main__":
    main()