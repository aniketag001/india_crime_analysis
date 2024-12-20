
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def kpi7(df):
    """# Total crimes against SCs as per year"""

    yearly_crime_against_SC = df.groupby('Year')['Other Crimes Against SCs'].sum().reset_index()
    yearly_crime_against_SC

    # Visualise total crime over years
    fig = plt.figure(figsize=(10, 7))
    sns.lineplot(x='Year', y='Other Crimes Against SCs', data=yearly_crime_against_SC, color='purple' , marker='o')
    plt.title('Total crimes against SCs as per year')
    plt.xlabel('Year')
    plt.ylabel('Other Crimes Against SCs')
    st.pyplot(fig)
