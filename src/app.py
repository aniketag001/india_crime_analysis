from static_visualization import static_insights
from dynamic_visualization import dynamic_insights

import streamlit as st

kpis, dashboard = st.tabs(["KPIs", "Dashboard"])

with kpis:
    static_insights()
with dashboard:
    dynamic_insights()
