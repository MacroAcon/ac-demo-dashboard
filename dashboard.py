import streamlit as st
import pandas as pd
import requests

# Streamlit page title
st.title("AI-Powered Portfolio Dashboard")

# Section: System Insights
st.header("System Insights")
st.write("This dashboard showcases the performance of AI agents in the portfolio.")

# Sample data
sample_data = {
    "Agent": ["Analysis Agent", "Visualization Agent", "QA Agent"],
    "Avg Processing Time (s)": [1.2, 1.5, 0.9],
    "Refinements": [3, 5, 2]
}
df = pd.DataFrame(sample_data)

# Display as table
st.dataframe(df)

# Section: GitHub Logs
st.header("Latest GitHub Logs")
GITHUB_REPO = "MacroAcon/ac-demo-portfolio"  # Update with your GitHub repo
GITHUB_FILE_PATH = "logs/agent_logs.json"

github_url = f"https://raw.githubusercontent.com/{GITHUB_REPO}/main/{GITHUB_FILE_PATH}"

try:
    response = requests.get(github_url)
    if response.status_code == 200:
        logs = response.json()
        st.json(logs)
    else:
        st.write("No logs available yet.")
except Exception as e:
    st.write("Error fetching logs:", e)
