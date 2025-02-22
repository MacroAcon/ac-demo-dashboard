import streamlit as st
import pandas as pd

# Set up page configuration
st.set_page_config(
    page_title="AI-Powered Portfolio Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar Theme Toggle
st.sidebar.title("⚙️ Settings")
dark_mode_enabled = st.sidebar.checkbox("🌙 Dark Mode", value=True)

# Define Dark & Light Mode Themes
DARK_MODE_CSS = """
    <style>
        body, .stApp {
            background-color: #0e1117 !important;
            color: #c9d1d9 !important;
        }
        .stDataFrame, .stTable {
            background-color: #161b22 !important;
            color: #c9d1d9 !important;
        }
        .css-1d391kg {
            background-color: #0e1117 !important;
        }
        .stMarkdown, .stTextInput, .stButton {
            color: #c9d1d9 !important;
        }
    </style>
"""

LIGHT_MODE_CSS = """
    <style>
        body, .stApp {
            background-color: white !important;
            color: black !important;
        }
    </style>
"""

# Apply the selected theme
if dark_mode_enabled:
    st.markdown(DARK_MODE_CSS, unsafe_allow_html=True)
else:
    st.markdown(LIGHT_MODE_CSS, unsafe_allow_html=True)

# Dashboard Header
st.markdown(
    f"<h1 style='text-align: center;'>🚀 AI-Powered Portfolio Dashboard</h1>",
    unsafe_allow_html=True,
)
st.write("---")  # Horizontal line for structure

# Sales Data Integration
st.markdown("### 📈 **Sales Data Overview**")
sales_data_path = "C:/Users/thnxt/Documents/ACPortfolio/ac-demo-dashboard/sales_data.csv"

try:
    df = pd.read_csv(sales_data_path)
    st.dataframe(df.style.set_properties(**{"background-color": "#161b22", "color": "#c9d1d9"}))
except FileNotFoundError:
    st.error(f"❌ Sales data file not found at: `{sales_data_path}`")

# AI Agent Performance Insights Placeholder
st.markdown("### 🤖 **AI Agent Performance Insights**")
st.write("This section will display AI agent performance logs and insights.")

# Simulated AI Agent Logs (Placeholder)
agent_performance = {
    "Analysis Agent": {"avg_processing_time": 1.2, "refinements": 3},
    "Visualization Agent": {"avg_processing_time": 1.5, "refinements": 5},
    "QA Agent": {"avg_processing_time": 0.9, "refinements": 2},
}

st.table(pd.DataFrame(agent_performance).T)

# Placeholder for Future Optimizations
st.markdown("### ⚙️ **System Optimizations & Logs**")
st.write("In future versions, AI agents will track logs and suggest performance optimizations.")

st.success("✅ Dashboard loaded successfully!")
