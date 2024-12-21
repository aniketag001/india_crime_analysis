
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from utils import fig_width, fig_height


def total_crime_over_years(df, population_df, literacy_df):
    
    st.subheader("Total Crime Over Year")
    st.text("Author: Sayanti Saha, Aniket Agarkar")
    st.write(
        """
        The graph indicates notable fluctuations in crime rates over the years, with peaks in 2002 and 2012. 
        The number of crimes was highest in 2002 and 2012, with around 33,500 crimes.
        A sharp decline in crime rates is observed from 2002 to 2003, suggesting effective crime prevention measures or reporting changes.
        Following the initial drop, there is a steady rise in crime rates from 2003 to 2008, indicating potential challenges in law enforcement or emerging crime trends.
        """
    )
    yearly_crime = df.groupby('Year')['Total crimes'].sum().reset_index()
    yearly_crime

    # Visualise total crime over years
    fig = plt.figure(figsize=(fig_width, fig_height))
    sns.lineplot(x='Year', y='Total crimes', data=yearly_crime, color='teal' , marker='o')
    plt.xlabel('Year')
    plt.ylabel('Total Crimes')
    st.pyplot(fig)
