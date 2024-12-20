
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

from utils import crime_columns

def crime_rates_by_category(df):

    st.subheader("Crime Rates By Category")
    st.text("Author: Sayanti Saha")

    fig = plt.figure(figsize=(12, 8))

    for crime in crime_columns:

        sns.lineplot(data=df.groupby('Year')[crime].sum().reset_index(), x='Year', y=crime, marker='o', label=crime)

    plt.xlabel('Year')

    plt.ylabel('Crime Counts')
    plt.legend()
    plt.grid() 
    st.pyplot(fig)

