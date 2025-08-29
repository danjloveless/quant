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

# TradingView-inspired dark theme CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* Global TradingView-style dark theme */
html, body, [class^="css"] { 
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: #131722 !important;
    color: #d1d4dc !important;
}

/* Hide Streamlit elements */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { visibility: hidden; }

/* TradingView-style top navigation */
.tv-header {
    background: linear-gradient(180deg, #1e222d 0%, #131722 100%);
    border-bottom: 1px solid #2a2e39;
    padding: 0;
    margin: -1rem -1rem 0 -1rem;
    position: sticky;
    top: 0;
    z-index: 1000;
    backdrop-filter: blur(10px);
}

.tv-nav-container {
    max-width: 1400px;
    margin: 0 auto;
    padding: 0 1rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 60px;
}

.tv-logo {
    font-size: 1.5rem;
    font-weight: 800;
    background: linear-gradient(135deg, #00d4aa 0%, #0099cc 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: -0.5px;
}

.tv-nav-menu {
    display: flex;
    gap: 2rem;
    align-items: center;
}

.tv-nav-link {
    color: #d1d4dc;
    text-decoration: none;
    font-weight: 500;
    font-size: 0.9rem;
    padding: 0.5rem 0;
    border-bottom: 2px solid transparent;
    transition: all 0.2s ease;
}

.tv-nav-link:hover {
    color: #00d4aa;
    border-bottom-color: #00d4aa;
}

.tv-nav-link.active {
    color: #00d4aa;
    border-bottom-color: #00d4aa;
}

.tv-actions {
    display: flex;
    gap: 1rem;
    align-items: center;
}

.tv-search-box {
    background: #2a2e39;
    border: 1px solid #363c4e;
    border-radius: 6px;
    padding: 0.5rem 1rem;
    color: #d1d4dc;
    font-size: 0.9rem;
    min-width: 200px;
}

.tv-search-box:focus {
    outline: none;
    border-color: #00d4aa;
    box-shadow: 0 0 0 2px rgba(0, 212, 170, 0.2);
}

.tv-btn {
    background: #2a2e39;
    border: 1px solid #363c4e;
    color: #d1d4dc;
    padding: 0.5rem 1rem;
    border-radius: 6px;
    font-weight: 500;
    font-size: 0.9rem;
    cursor: pointer;
    transition: all 0.2s ease;
}

.tv-btn:hover {
    background: #363c4e;
    border-color: #4a4f5a;
}

.tv-btn.primary {
    background: linear-gradient(135deg, #00d4aa 0%, #0099cc 100%);
    border-color: #00d4aa;
    color: #131722;
    font-weight: 600;
}

.tv-btn.primary:hover {
    background: linear-gradient(135deg, #00b894 0%, #0088aa 100%);
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(0, 212, 170, 0.3);
}

/* Main content area */
.main .block-container {
    background: #131722;
    padding: 2rem;
    max-width: 1400px;
}

/* TradingView-style cards */
.tv-card {
    background: linear-gradient(145deg, #1e222d 0%, #2a2e39 100%);
    border: 1px solid #363c4e;
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1rem;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    transition: all 0.3s ease;
}

.tv-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.4);
    border-color: #4a4f5a;
}

.tv-card-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 1rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid #363c4e;
}

.tv-card-title {
    font-size: 1.2rem;
    font-weight: 700;
    color: #ffffff;
    margin: 0;
}

.tv-card-subtitle {
    font-size: 0.9rem;
    color: #787b86;
    margin: 0.25rem 0 0 0;
}

.tv-card-badge {
    background: linear-gradient(135deg, #00d4aa 0%, #0099cc 100%);
    color: #131722;
    padding: 0.25rem 0.75rem;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
}

/* Metric cards */
.tv-metric {
    background: linear-gradient(145deg, #1e222d 0%, #2a2e39 100%);
    border: 1px solid #363c4e;
    border-radius: 10px;
    padding: 1.25rem;
    text-align: center;
    transition: all 0.3s ease;
}

.tv-metric:hover {
    transform: translateY(-1px);
    border-color: #00d4aa;
}

.tv-metric-value {
    font-size: 2rem;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 0.5rem;
}

.tv-metric-label {
    font-size: 0.9rem;
    color: #787b86;
    font-weight: 500;
}

.tv-metric-change {
    font-size: 0.8rem;
    font-weight: 600;
    margin-top: 0.5rem;
}

.tv-metric-change.positive {
    color: #00d4aa;
}

.tv-metric-change.negative {
    color: #ff6b6b;
}

/* Form styling */
.stTextInput > div > div > input {
    background: #2a2e39 !important;
    border: 1px solid #363c4e !important;
    color: #d1d4dc !important;
    border-radius: 6px !important;
}

.stTextInput > div > div > input:focus {
    border-color: #00d4aa !important;
    box-shadow: 0 0 0 2px rgba(0, 212, 170, 0.2) !important;
}

.stSelectbox > div > div > div {
    background: #2a2e39 !important;
    border: 1px solid #363c4e !important;
    color: #d1d4dc !important;
    border-radius: 6px !important;
}

.stDateInput > div > div > input {
    background: #2a2e39 !important;
    border: 1px solid #363c4e !important;
    color: #d1d4dc !important;
    border-radius: 6px !important;
}

/* Button styling */
.stButton > button {
    background: linear-gradient(135deg, #00d4aa 0%, #0099cc 100%) !important;
    border: none !important;
    color: #131722 !important;
    font-weight: 600 !important;
    border-radius: 6px !important;
    padding: 0.75rem 1.5rem !important;
    transition: all 0.2s ease !important;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #00b894 0%, #0088aa 100%) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 12px rgba(0, 212, 170, 0.3) !important;
}

/* Chart styling */
.plotly-graph-div {
    background: #1e222d !important;
    border: 1px solid #363c4e !important;
    border-radius: 10px !important;
    padding: 1rem !important;
    margin: 1rem 0 !important;
}

/* Success/Error messages */
.stAlert {
    background: linear-gradient(145deg, #1e222d 0%, #2a2e39 100%) !important;
    border: 1px solid #363c4e !important;
    border-radius: 8px !important;
    color: #d1d4dc !important;
}

/* Responsive design */
@media (max-width: 768px) {
    .tv-nav-container {
        padding: 0 0.5rem;
        flex-direction: column;
        height: auto;
        gap: 1rem;
    }
    
    .tv-nav-menu {
        gap: 1rem;
        flex-wrap: wrap;
    }
    
    .tv-actions {
        width: 100%;
        justify-content: center;
    }
    
    .main .block-container {
        padding: 1rem;
    }
    
    .tv-card {
        padding: 1rem;
    }
}

/* Loading animation */
@keyframes pulse {
    0% { opacity: 1; }
    50% { opacity: 0.5; }
    100% { opacity: 1; }
}

.tv-loading {
    animation: pulse 2s infinite;
}

/* Custom scrollbar */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: #1e222d;
}

::-webkit-scrollbar-thumb {
    background: #363c4e;
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background: #4a4f5a;
}
</style>
""", unsafe_allow_html=True)

# Add favicon
st.markdown("""
<link rel="shortcut icon" href="static/favicon.png" type="image/png">
<link rel="icon" href="static/favicon.ico" type="image/x-icon">
""", unsafe_allow_html=True)

# TradingView-style header
st.markdown("""
<div class="tv-header">
    <div class="tv-nav-container">
        <div class="tv-logo">QUANTFIN</div>
        <div class="tv-nav-menu">
            <a class="tv-nav-link active" href="#">Markets</a>
            <a class="tv-nav-link" href="#">Analysis</a>
            <a class="tv-nav-link" href="#">AI Insights</a>
            <a class="tv-nav-link" href="#">Research</a>
            <a class="tv-nav-link" href="#">Documentation</a>
        </div>
        <div class="tv-actions">
            <input class="tv-search-box" placeholder="Search assets, tickers..." />
            <button class="tv-btn">Sign In</button>
            <button class="tv-btn primary">Launch Platform</button>
        </div>
    </div>
</div>
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
    
    # TradingView-style hero section
    st.markdown("""
    <div class="tv-card" style="background: linear-gradient(135deg, #1e222d 0%, #2a2e39 100%); border: 1px solid #363c4e; margin-bottom: 2rem;">
        <div class="tv-card-header">
            <div>
                <h1 style="font-size: 2.5rem; font-weight: 800; color: #ffffff; margin: 0; background: linear-gradient(135deg, #00d4aa 0%, #0099cc 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">QUANTFIN SOCIETY RESEARCH</h1>
                <p style="font-size: 1.1rem; color: #787b86; margin: 0.5rem 0 0 0; font-weight: 500;">Professional Event Study Analysis Platform</p>
            </div>
            <div class="tv-card-badge">v2.2.1</div>
        </div>
        <p style="color: #d1d4dc; font-size: 1rem; line-height: 1.6; margin: 1rem 0 0 0;">
            Advanced quantitative analysis platform for event studies, market impact assessment, and AI-powered financial research.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # TradingView-style quick action cards
    st.markdown("""
    <div style="margin-bottom: 2rem;">
        <h2 style="color: #ffffff; font-size: 1.5rem; font-weight: 700; margin-bottom: 1rem;">Quick Actions</h2>
    </div>
    """, unsafe_allow_html=True)
    
    qc1, qc2, qc3 = st.columns(3)
    with qc1:
        st.markdown("""
        <div class="tv-card">
            <div class="tv-card-header">
                <div>
                    <h4 class="tv-card-title">📊 Event Study Analysis</h4>
                    <p class="tv-card-subtitle">CAPM-based quantitative analysis</p>
                </div>
                <div class="tv-card-badge">Manual</div>
            </div>
            <p style="color: #d1d4dc; font-size: 0.9rem; margin: 1rem 0;">Run comprehensive event studies with statistical significance testing and visualization.</p>
        </div>
        """, unsafe_allow_html=True)
    with qc2:
        st.markdown("""
        <div class="tv-card">
            <div class="tv-card-header">
                <div>
                    <h4 class="tv-card-title">🤖 AI News Detection</h4>
                    <p class="tv-card-subtitle">GPT-powered market analysis</p>
                </div>
                <div class="tv-card-badge">AI</div>
            </div>
            <p style="color: #d1d4dc; font-size: 0.9rem; margin: 1rem 0;">Identify market-moving events using advanced AI and natural language processing.</p>
        </div>
        """, unsafe_allow_html=True)
    with qc3:
        st.markdown("""
        <div class="tv-card">
            <div class="tv-card-header">
                <div>
                    <h4 class="tv-card-title">📈 Market Data</h4>
                    <p class="tv-card-subtitle">Real-time financial data</p>
                </div>
                <div class="tv-card-badge">Live</div>
            </div>
            <p style="color: #d1d4dc; font-size: 0.9rem; margin: 1rem 0;">Access clean historical data from multiple sources with advanced filtering.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # TradingView-style sidebar configuration
    with st.sidebar:
        st.markdown("""
        <div style="background: linear-gradient(145deg, #1e222d 0%, #2a2e39 100%); border: 1px solid #363c4e; border-radius: 12px; padding: 1.5rem; margin-bottom: 1rem;">
            <h3 style="color: #ffffff; font-size: 1.2rem; font-weight: 700; margin-bottom: 1rem;">⚙️ Analysis Configuration</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Analysis mode selection
        analysis_mode = st.selectbox(
            "📋 Analysis Mode",
            ["Manual Event Study", "AI News Detection"],
            help="Choose analysis approach"
        )
        
        # Event date selection
        event_date = st.date_input(
            "📅 Event Date",
            value=datetime.now().date(),
            help="Select the event date for analysis"
        )
        
        # Event description
        event_description = st.text_area(
            "📝 Event Description",
            placeholder="Describe the market event...",
            help="Provide details about the event"
        )
        
        # Asset selection
        assets_input = st.text_area(
            "💼 Assets (one per line)",
            placeholder="AAPL\nMSFT\nGOOGL",
            help="Enter asset symbols, one per line"
        )
        
        # Analysis parameters
        estimation_window = st.slider(
            "📊 Estimation Window (days)",
            min_value=60,
            max_value=500,
            value=252,
            help="Period for CAPM estimation"
        )
        
        event_window = st.slider(
            "🎯 Event Window (days)",
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
    """Display analysis results with TradingView-style design"""
    
    # TradingView-style summary metrics
    st.markdown("""
    <div style="margin-bottom: 2rem;">
        <h2 style="color: #ffffff; font-size: 1.5rem; font-weight: 700; margin-bottom: 1rem;">📊 Analysis Summary</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="tv-metric">
            <div class="tv-metric-value">{len(assets)}</div>
            <div class="tv-metric-label">Assets Analyzed</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="tv-metric">
            <div class="tv-metric-value">{results.get('event_date', 'N/A')}</div>
            <div class="tv-metric-label">Event Date</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="tv-metric">
            <div class="tv-metric-value">{results.get('estimation_window', 0)}</div>
            <div class="tv-metric-label">Estimation Window (days)</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="tv-metric">
            <div class="tv-metric-value">{results.get('event_window', 0)}</div>
            <div class="tv-metric-label">Event Window (days)</div>
        </div>
        """, unsafe_allow_html=True)
    
    # TradingView-style results tabs
    tab1, tab2, tab3 = st.tabs(["📊 Analysis Results", "📈 Charts", "🤖 AI Insights"])
    
    with tab1:
        display_analysis_results(results)
    
    with tab2:
        display_charts(results)
    
    with tab3:
        if ai_insights:
            display_ai_insights(ai_insights)
        else:
            st.markdown("""
            <div class="tv-card">
                <div class="tv-card-header">
                    <div>
                        <h4 class="tv-card-title">🤖 AI Insights</h4>
                        <p class="tv-card-subtitle">GPT-powered market analysis</p>
                    </div>
                    <div class="tv-card-badge">Premium</div>
                </div>
                <p style="color: #d1d4dc; font-size: 0.9rem; margin: 1rem 0;">
                    AI insights are available with AI News Detection mode. Switch to AI mode in the sidebar to get advanced market analysis.
                </p>
            </div>
            """, unsafe_allow_html=True)

def display_analysis_results(results):
    """Display detailed analysis results with TradingView-style design"""
    
    if 'abnormal_returns' in results:
        st.markdown("""
        <div style="margin-bottom: 1rem;">
            <h3 style="color: #ffffff; font-size: 1.3rem; font-weight: 700;">📊 Abnormal Returns Analysis</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Convert to DataFrame for display
        ar_df = pd.DataFrame(results['abnormal_returns'])
        st.markdown("""
        <div class="tv-card">
            <div class="tv-card-header">
                <div>
                    <h4 class="tv-card-title">📈 Returns Data</h4>
                    <p class="tv-card-subtitle">Abnormal returns analysis results</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.dataframe(ar_df, use_container_width=True)
        
        # Statistical summary
        if 'statistics' in results:
            st.markdown("""
            <div style="margin: 2rem 0 1rem 0;">
                <h3 style="color: #ffffff; font-size: 1.3rem; font-weight: 700;">📋 Statistical Summary</h3>
            </div>
            """, unsafe_allow_html=True)
            stats_df = pd.DataFrame(results['statistics'])
            st.markdown("""
            <div class="tv-card">
                <div class="tv-card-header">
                    <div>
                        <h4 class="tv-card-title">📊 Statistics</h4>
                        <p class="tv-card-subtitle">Statistical significance testing</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.dataframe(stats_df, use_container_width=True)

def display_charts(results):
    """Display interactive charts with TradingView-style design"""
    
    if 'charts' in results:
        st.markdown("""
        <div style="margin-bottom: 1rem;">
            <h3 style="color: #ffffff; font-size: 1.3rem; font-weight: 700;">📈 Interactive Charts</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Display each chart
        for chart_name, chart_data in results['charts'].items():
            st.markdown(f"""
            <div class="tv-card">
                <div class="tv-card-header">
                    <div>
                        <h4 class="tv-card-title">📊 {chart_name}</h4>
                        <p class="tv-card-subtitle">Interactive visualization</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.plotly_chart(chart_data, use_container_width=True)

def display_ai_insights(ai_insights):
    """Display AI-generated insights with TradingView-style design"""
    
    st.markdown("""
    <div style="margin-bottom: 1rem;">
        <h3 style="color: #ffffff; font-size: 1.3rem; font-weight: 700;">🤖 AI Market Analysis</h3>
    </div>
    """, unsafe_allow_html=True)
    
    if isinstance(ai_insights, dict):
        for key, value in ai_insights.items():
            st.markdown(f"""
            <div class="tv-card">
                <div class="tv-card-header">
                    <div>
                        <h4 class="tv-card-title">🔍 {key}</h4>
                        <p class="tv-card-subtitle">AI-generated insight</p>
                    </div>
                </div>
                <p style="color: #d1d4dc; font-size: 0.9rem; margin: 1rem 0;">{value}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="tv-card">
            <div class="tv-card-header">
                <div>
                    <h4 class="tv-card-title">🤖 AI Analysis</h4>
                    <p class="tv-card-subtitle">GPT-powered insights</p>
                </div>
            </div>
            <p style="color: #d1d4dc; font-size: 0.9rem; margin: 1rem 0;">{ai_insights}</p>
        </div>
        """, unsafe_allow_html=True)

# Run the application
if __name__ == "__main__":
    main()