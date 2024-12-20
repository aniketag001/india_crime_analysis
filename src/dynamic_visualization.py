

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import ipywidgets as widgets
from utils import clean_data, load_data

def dynamic_insights():
        
        df = load_data()
        df = clean_data(df)

        df["Total crimes"] = df.iloc[:, 3:13].sum(axis=1)

        df.head()

        all_crimes = ['Murder', 'Assault on women','Kidnapping and Abduction', 'Dacoity', 'Robbery', 'Arson', 'Hurt','Prevention of atrocities (POA) Act' , 'Protection of Civil Rights (PCR) Act', 'Other Crimes Against SCs']

        print(all_crimes)

        print(type(all_crimes))


#Crime Trends over Years w.r.t State

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
    plt.figure(figsize=(10, 6))
    plt.plot(total_crimes_per_year.index, total_crimes_per_year.values)
    plt.xlabel('Year')
    plt.ylabel('Total Crimes')
    plt.title(f'Crime Trends Over Years in {state}')
    plt.xticks(rotation=45, ha='right')
    plt.grid(True)
    plt.show()

# Link the dropdown widget to the chart update function
widgets.interactive(update_chart, state=state_dropdown)
