
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from utils import fig_width, fig_height


def growth_rate_of_total_crimes(df, population_df, literacy_df):

    st.subheader("Growth Rate of Total Crimes by State/UT Across Years")
    st.text("Author: Sakshi Jaiswal")
    st.write("""
          The findings of this analysis, visualized in the heatmap, demonstrate considerable variation in the growth rate of total crimes across Indian states and union territories from 2001 to 2012.
          The color gradient, ranging from blue indicating negative growth to red signifying positive growth, reveals substantial heterogeneity in crime trends across regions and over time. While some states consistently demonstrated a decline in crime rates, others experienced pronounced increases, particularly in the latter years. 
          Notably, several states exhibit fluctuating patterns, characterized by periods of rapid growth interspersed with periods of decline, suggesting complex and dynamic crime dynamics.
            """ 
    )
    yearly_crime = df.groupby(['Year', 'STATE/UT'])['Total crimes'].sum().reset_index()
    yearly_crime['Growth Rate (%)'] = yearly_crime.groupby('STATE/UT')['Total crimes'].pct_change() * 100
    growth_rate_pivot = yearly_crime.pivot(index='STATE/UT', columns='Year', values='Growth Rate (%)')

    #Heatmap for quickly spotting growth patterns across states and years.
    fig = plt.figure(figsize=(fig_width, fig_height))
    sns.heatmap(growth_rate_pivot, annot=True, cmap='coolwarm', fmt=".1f", linewidths=0.5)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('State/UT', fontsize=12)
    st.pyplot(fig)

