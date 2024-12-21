import matplotlib.pyplot as plt 
import seaborn as sns
import streamlit as st
from utils import fig_width, fig_height


def top_5_crimes(df, population_df, literacy_df):
    st.subheader("Top_5_Crimes in India")
    st.text("Author: Aniket Agarkar")
    st.write(
        """
       This pie chart visualizes the distribution of the top 5 crime types based on their frequency of occurrence. 
       It provides a quick overview of the relative proportions of each crime type within the dataset.The Pie Chart
       shows Dominance of "Other Crimes Against SCs" category with the largest portion of the pie chart,
       with 44.7% of the top 5 crimes.
        """
    )
  crime_type_cols = ['Murder', 'Assault on women', 'Kidnapping and Abduction', 'Dacoity', 'Robbery',
                  'Arson', 'Hurt', 'Prevention of atrocities (POA) Act', 'Protection of Civil Rights (PCR) Act',
                  'Other Crimes Against SCs']
  crimes_type = df[crime_type_cols].sum()
  top_crimes = crimes_type.nlargest(5)
  fig = plt.figure(figsize=(10, 8))
  plt.pie(top_crimes, labels=top_crimes.index, autopct='%1.1f%%', startangle=140)
  plt.title("Top 5 Crime Types with Highest Occurrences")
  plt.tight_layout()
  st.pyplot(fig)
