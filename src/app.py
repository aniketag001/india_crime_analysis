from kpi_visualization import kpi_insights

from dashboard_visualization import dashboard_insights
import streamlit as st

st.set_page_config(
    page_title="India Crime Analysis",
    page_icon="🌟",
    layout="wide",  # Ensures the app takes up more horizontal space
)

st.title("Caste Based Crime Analysis")


kpis, dashboard = st.tabs(["KPIs", "Dashboard"])

import streamlit as st

import folium
import pandas as pd


from geopy.geocoders import Nominatim


from folium.plugins import HeatMap



with kpis:

    kpi_insights()


with dashboard:

    dashboard_insights()



