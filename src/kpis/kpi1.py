
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def kpi1(df):
    yearly_crime = df.groupby(['Year', 'STATE/UT'])['Total crimes'].sum().reset_index()
    yearly_crime['Growth Rate (%)'] = yearly_crime.groupby('STATE/UT')['Total crimes'].pct_change() * 100
    growth_rate_pivot = yearly_crime.pivot(index='STATE/UT', columns='Year', values='Growth Rate (%)')

    #Heatmap for quickly spotting growth patterns across states and years.
    plt.figure(figsize=(12, 10))
    sns.heatmap(growth_rate_pivot, annot=True, cmap='coolwarm', fmt=".1f", linewidths=0.5)
    plt.title('Growth Rate of Total Crimes by State/UT Across Years', fontsize=16)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('State/UT', fontsize=12)
    plt.show()

