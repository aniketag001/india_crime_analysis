

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from utils import load_crime_data
import ipywidgets as widgets
from ctypes import alignment

def dynamic_insights():
        
    df = load_crime_data()

    #1.Crime Trends over Years w.r.t State

    crime_type_cols = ['Murder', 'Assault on women', 'Kidnapping and Abduction', 'Dacoity', 'Robbery', 
                    'Arson', 'Hurt', 'Prevention of atrocities (POA) Act', 'Protection of Civil Rights (PCR) Act', 
                    'Other Crimes Against SCs']

    # Get unique states from the DataFrame
    unique_states = df['STATE/UT'].unique()

    # Create a dropdown widget for state selection
    state_dropdown = widgets.Dropdown(
        options=unique_states,
        value=unique_states[0],  # Default to the first state
        description='Select State:'
    )

    # Function to update the chart based on state selection
    def update_chart(state):
        # Filter the DataFrame based on the selected state
        state_df = df[df['STATE/UT'] == state]
        
        # Calculate the sum of all crime types for each year for the selected state
        total_crimes_per_year = state_df.groupby('Year')[crime_type_cols].sum().sum(axis=1)
        fig = plt.figure(figsize=(10, 6))
        plt.plot(total_crimes_per_year.index, total_crimes_per_year.values)
        plt.xlabel('Year')
        plt.ylabel('Total Crimes')
        plt.title(f'Crime Trends Over Years in {state}')
        plt.xticks(rotation=45, ha='right')
        plt.grid(True)
        st.pyplot(fig)
    # Link the dropdown widget to the chart update function
    widgets.interactive(update_chart, state=state_dropdown)


    #2.crime types and counts in years w.r.t State
    crime_type_cols = ['Murder', 'Assault on women', 'Kidnapping and Abduction', 'Dacoity', 'Robbery',
                    'Arson', 'Hurt', 'Prevention of atrocities (POA) Act', 'Protection of Civil Rights (PCR) Act',
                    'Other Crimes Against SCs']

    # Get unique states from the DataFrame
    unique_states = df['STATE/UT'].unique()

    # Create dropdown widget for state selection
    state_dropdown = widgets.Dropdown(
        options=unique_states,
        value=unique_states[0],  # Default to the first state
        description='Select State:'
    )
    # Create a slider widget for year selection
    min_year = df['Year'].min()
    max_year = df['Year'].max()
    year_slider = widgets.IntSlider(
        min=min_year,
        max=max_year,
        step=1,
        value=min_year,  # Default to the minimum year
        description='Select Year:'
    )
    # Function to update the chart based on state and year selection
    def update_chart(state, year):
        # Filter the DataFrame based on selected state and year
        state_df = df[(df['STATE/UT'] == state) & (df['Year'] == year)]

        # Calculate the sum of all crime types for the selected state and year
        total_crimes_per_year = state_df[crime_type_cols].sum()

        if not total_crimes_per_year.empty:  # Check if data exists for the selection
            # Create a bar chart
            fig = plt.figure(figsize=(10, 6))
            plt.bar(total_crimes_per_year.index, total_crimes_per_year.values,color = 'Orange')
            plt.xlabel('Crime Type')
            plt.ylabel('Total Crimes')
            plt.title(f'Crime Types and Counts in {state} for Year {year}')
            plt.xticks(rotation=45, ha='right')
            plt.grid(True)
            st.pyplot()
        else:
            print(f"No data found for {state} in year {year}.")

    # Link the widgets to the chart update function
    widgets.interactive(update_chart, state=state_dropdown, year=year_slider)



    #3.States with Top 5 Crime Types
    crime_type_cols = ['Murder', 'Assault on women', 'Kidnapping and Abduction', 'Dacoity', 'Robbery',
                    'Arson', 'Hurt', 'Prevention of atrocities (POA) Act', 'Protection of Civil Rights (PCR) Act',
                    'Other Crimes Against SCs']

    unique_states = df['STATE/UT'].unique()

    # Create a dropdown widget for state selection
    state_dropdown = widgets.Dropdown(
        options=unique_states,
        value=unique_states[0],  # Default to the first state
        description='Select State:'
    )

    # Function to update the pie chart based on state selection
    def update_pie_chart(state):
        # Filter the DataFrame based on the selected state
        state_df = df[df['STATE/UT'] == state]

        # Calculate the sum of each crime type for the selected state
        crime_type_sums = state_df[crime_type_cols].sum()
        crime_type_sums = crime_type_sums[crime_type_sums > 0]
        if not crime_type_sums.empty:
        # Select the top 5 crime types with the highest occurrences
            top_5_crimes = crime_type_sums.nlargest(5)
            fig = plt.figure(figsize=(8, 8))
            plt.pie(top_5_crimes, labels=top_5_crimes.index, autopct='%1.1f%%', startangle=140)
            plt.title(f"Top 5 Crime Types in {state}")
            st.pyplot()
        else:
            print(f"No data found for {state} for crime types")
    # Link the dropdown widget to the chart update function
    widgets.interactive(update_pie_chart, state=state_dropdown)
