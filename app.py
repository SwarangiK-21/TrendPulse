import streamlit as st
import pandas as pd
import sqlalchemy
import plotly.express as px

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="TrendPulse Dashboard", layout="wide", page_icon="⚡")

# Custom CSS for "Dark Mode" styling
st.markdown("""
    <style>
        .block-container {padding-top: 1rem; padding-bottom: 1rem;}
        div[data-testid="stMetricValue"] {font-size: 24px; color: #FAFAFA;}
        div[data-testid="stMetricLabel"] {font-size: 14px; color: #aaaaaa;}
    </style>
""", unsafe_allow_html=True)

# --- 2. DATA LOADER ---
@st.cache_data(ttl=5) 
def load_data():
    # Connect to database
    engine = sqlalchemy.create_engine('sqlite:///trendpulse.db')
    
    # Load Tables
    df_sales = pd.read_sql("SELECT * FROM sales", engine)
    df_social = pd.read_sql("SELECT * FROM social_buzz", engine)
    
    # Fix Dates
    df_sales['date'] = pd.to_datetime(df_sales['date'])
    df_social['date'] = pd.to_datetime(df_social['date'])
    
    return df_sales, df_social

try:
    df_sales, df_social = load_data()
except Exception as e:
    st.error(f"Database Error: {e}. Make sure trendpulse.db is in the folder!")
    st.stop()

# --- 3. SIDEBAR FILTERS ---
st.sidebar.title("⚡ TrendPulse")
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/1043/1043450.png", width=50)
st.sidebar.header("⚙️ Dashboard Filters")

# Filter by Platform
all_platforms = df_social['platform'].unique()
selected_platforms = st.sidebar.multiselect(
    "Select Social Platforms:", 
    options=all_platforms, 
    default=all_platforms 
)

# Apply Filter
if not selected_platforms:
    st.warning("Please select at least one platform.")
    st.stop()

filtered_social = df_social[df_social['platform'].isin(selected_platforms)]

# --- 4. HEADER & KPI CARDS ---
col_header, col_btn = st.columns([6, 1])
with col_header:
    st.title("🚀 TrendPulse: Market Command Center")
    st.markdown("Real-time correlation between **Brand Sentiment** and **Market Revenue**.")
with col_btn:
    if st.button("🔄 Refresh"):
        st.rerun()

st.markdown("---")

# KPI Row
col1, col2, col3, col4 = st.columns(4)

# KPI 1: Total Revenue
total_rev = df_sales['total_revenue'].sum()
col1.metric("💰 Total Revenue", f"${total_rev:,.0f}", delta="12% vs last month")

# KPI 2: Transactions (Safe Fix using row count)
transaction_count = len(df_sales) 
col2.metric("📦 Transactions", f"{transaction_count}", delta="Live")

# KPI 3: Social Buzz (Uses Filtered Data)
buzz_count = len(filtered_social)
col3.metric("🐦 Mentions (Filtered)", f"{buzz_count}", delta="Live")

# KPI 4: Sentiment (Uses Filtered Data)
avg_sent = filtered_social['sentiment_score'].mean()
sent_delta = "High" if avg_sent > 0.5 else "Neutral"
col4.metric("❤️ Brand Sentiment", f"{avg_sent:.2f}", delta=sent_delta)

# --- 5. TABS LAYOUT ---
tab1, tab2 = st.tabs(["📊 Executive Overview", "🔎 Data Deep Dive"])

# TAB 1: VISUALIZATIONS
with tab1:
    c1, c2 = st.columns([2, 1]) 

    with c1:
        st.subheader("📈 Revenue Trajectory")
        daily_sales = df_sales.groupby(df_sales['date'].dt.date)['total_revenue'].sum().reset_index()
        
        fig_sales = px.area(daily_sales, x='date', y='total_revenue', 
                            template="plotly_dark",
                            color_discrete_sequence=['#F63366'])
        
        fig_sales.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", yaxis_title="Revenue ($)")
        st.plotly_chart(fig_sales, use_container_width=True)

    with c2:
        st.subheader("🌍 Platform Split")
        
        # Donut Chart - CORRECTED CODE HERE
        platform_counts = filtered_social['platform'].value_counts().reset_index()
        platform_counts.columns = ['platform', 'count']
        
        # Use px.pie with hole=0.6 instead of px.donut
        fig_pie = px.pie(platform_counts, values='count', names='platform', hole=0.6,
                         template="plotly_dark",
                         color_discrete_sequence=px.colors.sequential.RdBu)
        
        fig_pie.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_pie, use_container_width=True)

# TAB 2: RAW DATA & PROGRESS BARS
with tab2:
    st.subheader("🧠 Sentiment Analysis")
    col_left, col_right = st.columns(2)
    
    with col_left:
        # Histogram
        fig_hist = px.histogram(filtered_social, x="sentiment_score", nbins=20,
                                title="Sentiment Distribution",
                                template="plotly_dark",
                                color_discrete_sequence=['#636EFA'])
        fig_hist.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_hist, use_container_width=True)
        
    with col_right:
        st.caption("Recent Mentions (With Sentiment Progress Bar)")
        
        st.dataframe(
            filtered_social[['date', 'platform', 'content', 'sentiment_score']].sort_values(by='date', ascending=False),
            column_config={
                "sentiment_score": st.column_config.ProgressColumn(
                    "Sentiment Score",
                    help="AI Confidence",
                    format="%.2f",
                    min_value=-1,
                    max_value=1,
                ),
            },
            use_container_width=True,
            hide_index=True
        )

# --- SIDEBAR FOOTER ---
st.sidebar.markdown("---")
st.sidebar.success("System Status: 🟢 Online")