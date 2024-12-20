import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def kpi12(df):
    Calculating Total Crimes as per State (from highest to lowest)  
    state_crime = df.groupby('STATE/UT')['Total crimes'].sum().sort_values(ascending = False).reset_index()
    state_crime

    """# Analysis of Common Crime Type over Years"""

    # Analysis of common crime type over years
    crimes = ['Murder', 'Assault on women','Kidnapping and Abduction', 'Dacoity', 'Robbery', 'Arson', 'Hurt', 'Other Crimes Against SCs']