from static_visualization import static_insights
from dynamic_visualization import dynamic_insights
import streamlit as st

st.set_page_config(
    page_title="India Crime Analysis",
    page_icon="🌟",
    layout="wide",  # Ensures the app takes up more horizontal space
)

kpis, dashboard = st.tabs(["KPIs", "Dashboard"])

with kpis:
    static_insights()
with dashboard:
    dynamic_insights()
