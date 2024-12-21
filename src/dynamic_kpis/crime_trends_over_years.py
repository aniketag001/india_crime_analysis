


import streamlit as st
import ipywidgets as widgets
from utils import crime_columns, fig_width, fig_height
import matplotlib.pyplot as plt

def crime_trends_over_years(df, population_df, literacy_df):
 
    st.subheader("6. Each Crime Category over Years")
    st.text("Author: Aniket Agarkar")
    unique_states = df['STATE/UT'].unique()

    # Create a dropdown widget for state selection
    selected_state = st.selectbox("Select State For Each Crime", options=unique_states)  
   
    state_df = df[df['STATE/UT'] == selected_state]
    total_crimes_per_year = state_df.groupby('Year')[crime_columns].sum().sum(axis=1)
    fig = plt.figure(figsize=(fig_width, fig_height))
    plt.plot(total_crimes_per_year.index, total_crimes_per_year.values)
    plt.xlabel('Year')
    plt.ylabel('Total Crimes')
    plt.title(f'Crime Trends Over Years in {selected_state}')
    plt.xticks(rotation=45, ha='right')
    plt.grid(True)
    st.pyplot(fig)