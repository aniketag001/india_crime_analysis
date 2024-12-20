
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from utils import crime_columns, fig_width, fig_height

def crime_rates_by_category(df):
    st.subheader("Crime Rates By Category")
    st.text("Author: Sayanti Saha")
    st.write(
        """
        This chart represents the values of different categories. 
        Each bar corresponds to a specific category and its respective value. 
        The data shows that Category D has the highest value, while Category A has the lowest. 
        Such visualizations are helpful for comparing categorical data.
        """
    )
    fig = plt.figure(figsize=(fig_width, fig_height))

    for crime in crime_columns:

        sns.lineplot(data=df.groupby('Year')[crime].sum().reset_index(), x='Year', y=crime, marker='o', label=crime)

    plt.xlabel('Year')

    plt.ylabel('Crime Counts')
    plt.legend()
    plt.grid() 
    st.pyplot(fig)