
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from utils import crime_columns, fig_width, fig_height

def crime_rates_by_category(df, population_df, literacy_df):
    st.subheader("6. Crime Rates By Category")
    st.text("Author: Sayanti Saha")

    st.write(
        """
        The graph shows a mixed trend in crime rates across different categories in India. 
        Some crimes have shown an increasing trend, while others have remained stable or decreased over the years. 
        This indicates varying dynamics in crime patterns, which may be influenced by socio-economic factors, law enforcement effectiveness, and public awareness campaigns. 
        Rising Concerns: Murder and kidnapping cases show an upward trend, highlighting concerns for public safety and crime prevention efforts.
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
