
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def kpi7(df):
    """# Total Crime over Years"""

    yearly_crime = df.groupby('Year')['Total crimes'].sum().reset_index()
    yearly_crime

    # Visualise total crime over years
    fig = plt.figure(figsize=(10, 7))
    sns.lineplot(x='Year', y='Total crimes', data=yearly_crime, color='teal' , marker='o')
    plt.title('Total Crime Over Years')
    plt.xlabel('Year')
    plt.ylabel('Total Crimes')
    st.pyplot(fig)
