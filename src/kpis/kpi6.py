import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from utils import crime_columns

def kpi6(df):
     total_crimes_year = df.groupby('Year')[crime_columns].sum().sum(axis=1)

    # Create a bar chart to visualize crime trends over years
    fig = plt.figure(figsize=(10, 6))
    plt.bar(total_crimes_year.index, total_crimes_year.values)
    plt.xlabel('Year')
    plt.ylabel('Total Crimes')
    plt.title('Crime Trends Over Years')
    plt.grid(True)
    plt.tight_layout()
    st.pyplot(fig)