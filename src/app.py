from static_visualization import static_insights
from dynamic_visualization import dynamic_insights
import streamlit as st

st.set_page_config(
    page_title="India Crime Analysis",
    page_icon="🌟",
    layout="wide",  # Ensures the app takes up more horizontal space
)

kpis, dashboard = st.tabs(["KPIs", "Dashboard"])

import streamlit as st
import folium
import pandas as pd
from geopy.geocoders import Nominatim
from folium.plugins import HeatMap

# with kpis:
#     static_insights()
# with dashboard:
#     dynamic_insights()

import streamlit as st
import folium
import pandas as pd
from geopy.geocoders import Nominatim
# from folium.plugins import Choropleth
import json

# Crime Data for Indian States (replace with your actual data)
crime_data = {
    "Delhi": 150, 
    "Maharashtra": 200, 
    "Tamil Nadu": 120,
    "Karnataka": 100,
    "Uttar Pradesh": 300,
    "Gujarat": 180,
    "West Bengal": 130,
    "Rajasthan": 90,
    "Bihar": 75,
    "Punjab": 110,
    "Madhya Pradesh": 160
}

# List of states in India
states = list(crime_data.keys())

# Function to get latitude and longitude for each state
def get_lat_lon(state_name):
    geolocator = Nominatim(user_agent="crime_heatmap")
    location = geolocator.geocode(f"{state_name}, India")
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

# Fetching latitude and longitude for each state
state_coordinates = {}
for state in states:
    lat, lon = get_lat_lon(state)
    if lat and lon:
        state_coordinates[state] = {'latitude': lat, 'longitude': lon}
    else:
        state_coordinates[state] = {'latitude': None, 'longitude': None}

# Prepare data for folium Choropleth
data = []
for state, coords in state_coordinates.items():
    crime_count = crime_data.get(state, 0)
    if coords['latitude'] and coords['longitude']:
        data.append([state, coords['latitude'], coords['longitude'], crime_count])

# Create the base map
# m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# # Add markers for each state to visualize the crime data
# for state, lat_lon_crime in zip(states, data):
#     state_name, latitude, longitude, crime_count = lat_lon_crime
#     folium.CircleMarker(
#         location=(latitude, longitude),
#         radius=10,
#         color='red' if crime_count > 100 else 'green',
#         fill=True,
#         fill_color='red' if crime_count > 100 else 'green',
#         fill_opacity=0.6,
#         popup=f"State: {state_name}<br>Crime Count: {crime_count}"
#     ).add_to(m)

# # Display map in Streamlit
# st.title("Crime Heatmap by State in India (Geocoded)")
# st.markdown("This map visualizes crime data by state in India, with geolocation fetched automatically.")
# st.components.v1.html(m._repr_html_(), height=600)
import plotly.graph_objects as go
from utils import load_crime_data
# import requests
# url = 'https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/india-states.geojson'
# geojson_data = requests.get(url).json()

df = load_crime_data()
df['STATE/UT'] = df['STATE/UT'].str.title()
df = df.groupby('STATE/UT').agg(
    Total_Crime=('Total crimes', 'sum')
).reset_index()
print(df)
fig = go.Figure(data=go.Choropleth(   
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locationmode='geojson-id',
    locations=df['STATE/UT'],
    z=df['Total_Crime'],

    autocolorscale=False,
    colorscale='Reds',
    marker_line_color='peachpuff',

    colorbar=dict(
        title={'text': "Active Cases"},

        thickness=15,
        len=0.35,
        bgcolor='rgba(255,255,255,0.6)',

        tick0=0,
        dtick=20000,

        xanchor='left',
        x=0.01,
        yanchor='bottom',
        y=0.05
    )
))

fig.update_geos(
    visible=False,
    projection=dict(
        type='conic conformal',
        parallels=[12.472944444, 35.172805555556],
        rotation={'lat': 24, 'lon': 80}
    ),
    lonaxis={'range': [68, 98]},
    lataxis={'range': [6, 38]}
)

fig.update_layout(
    title=dict(
        text="Active COVID-19 Cases in India by State as of July 17, 2020",
        xanchor='center',
        x=0.5,
        yref='paper',
        yanchor='bottom',
        y=1,
        pad={'b': 10}
    ),
    margin={'r': 0, 't': 30, 'l': 0, 'b': 0},
    height=550,
    width=550
)

fig.show()
