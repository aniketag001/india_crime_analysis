
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from utils import fig_width, fig_height


def total_crime_over_years(df):
    
    st.subheader("Total Crime Over Year")
    st.text("Author: Sayanti Saha")

    yearly_crime = df.groupby('Year')['Total crimes'].sum().reset_index()
    yearly_crime

    # Visualise total crime over years
    fig = plt.figure(figsize=(fig_width, fig_height))
    sns.lineplot(x='Year', y='Total crimes', data=yearly_crime, color='teal' , marker='o')
    plt.xlabel('Year')
    plt.ylabel('Total Crimes')
    st.pyplot(fig)
