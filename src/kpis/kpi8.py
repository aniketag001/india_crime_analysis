
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def kpi8(df):
    """# Analysis of Common Crime Type over Years"""

    # Analysis of common crime type over years
    crimes = ['Murder', 'Assault on women','Kidnapping and Abduction', 'Dacoity', 'Robbery', 'Arson', 'Hurt','Prevention of atrocities (POA) Act','Protection of Civil Rights (PCR) Act', 'Other Crimes Against SCs']

    plt.figure(figsize=(12, 8))
    for crime in crimes:
        sns.lineplot(data=df.groupby('Year')[crime].sum().reset_index(), x='Year', y=crime, marker='o', label=crime)

    fig = plt.figure(figsize=(10, 7))
    plt.title('Common Crime Types Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Crime Counts')
    plt.legend()
    plt.grid()
    st.pyplot(fig)
