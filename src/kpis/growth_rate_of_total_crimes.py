
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from utils import fig_width, fig_height


def growth_rate_of_total_crimes(df):

    st.subheader("Growth Rate of Total Crimes by State/UT Across Years")
    st.text("Author: Sakshi Jaiswal")
    yearly_crime = df.groupby(['Year', 'STATE/UT'])['Total crimes'].sum().reset_index()
    yearly_crime['Growth Rate (%)'] = yearly_crime.groupby('STATE/UT')['Total crimes'].pct_change() * 100
    growth_rate_pivot = yearly_crime.pivot(index='STATE/UT', columns='Year', values='Growth Rate (%)')

    #Heatmap for quickly spotting growth patterns across states and years.
    fig = plt.figure(figsize=(fig_width, fig_height))
    sns.heatmap(growth_rate_pivot, annot=True, cmap='coolwarm', fmt=".1f", linewidths=0.5)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('State/UT', fontsize=12)
    st.pyplot(fig)

