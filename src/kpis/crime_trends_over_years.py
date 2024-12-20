import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from utils import crime_columns, fig_width, fig_height

def crime_trends_over_years(df, population_df, literacy_df):
    st.subheader("Crime Trends Over Years")
    st.text("Author: Aniket Agarkar")
    
    total_crimes_year = df.groupby('Year')[crime_columns].sum().sum(axis=1)

    # Create a bar chart to visualize crime trends over years
    fig = plt.figure(figsize=(fig_width, fig_height))
    plt.bar(total_crimes_year.index, total_crimes_year.values)
    plt.xlabel('Year')
    plt.ylabel('Total Crimes')
    plt.grid(True)
    plt.tight_layout()
    st.pyplot(fig)