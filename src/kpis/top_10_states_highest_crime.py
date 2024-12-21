

import matplotlib.pyplot as plt

import seaborn as sns
import streamlit as st
from utils import crime_columns, fig_width, fig_height


def top_10_states_highest_crime(df, population_df, literacy_df):
    
    st.subheader("2. Top 10 States with Highest Crimes")
    st.text("Author: Sayanti Saha")

    st.write(
        """
        This chart provides a visual representation of the crime rates across different states in India.
        This represents overall crime rate in each state, as population density and the number of crimes reported.
        Analyzing the data over time can reveal whether crime rates are increasing or decreasing in specific states.
        The chart highlights the states with the highest number of reported crimes. 
        Uttar Pradesh leads with the highest crime rate.
        """
    )



    state_crime = df.groupby('STATE/UT')['Total crimes'].sum().sort_values(ascending = False).reset_index()
    state_crime


    # Visualize Top 10 States with Highest Crimes


    fig = plt.figure(figsize=(fig_width, fig_height))

    sns.barplot(x="STATE/UT", y="Total crimes", data=state_crime.head(10), palette="viridis")

    plt.title("Top 10 States with Highest Crimes")

    plt.xlabel("State")

    plt.ylabel("Total Crimes")

    plt.xticks(rotation=90)

    st.pyplot(fig)

