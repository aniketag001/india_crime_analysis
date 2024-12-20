

import matplotlib.pyplot as plt

import seaborn as sns
import streamlit as st
from utils import crime_columns, fig_width, fig_height


def top_10_states_highest_crime(df, population_df, literacy_df):
    
    st.subheader("Top 10 States with Highest Crimes")

    st.text("Author: Sayanti Saha")


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

