
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from utils import crime_columns, fig_width, fig_height

def crime_rates_by_category(df, population_df, literacy_df):
    st.subheader("Crime Rates By Category")
    st.text("Author: Sayanti Saha")
   
    fig = plt.figure(figsize=(fig_width, fig_height))

    for crime in crime_columns:

        sns.lineplot(data=df.groupby('Year')[crime].sum().reset_index(), x='Year', y=crime, marker='o', label=crime)

    plt.xlabel('Year')

    plt.ylabel('Crime Counts')
    plt.legend()
    plt.grid() 
    st.pyplot(fig)