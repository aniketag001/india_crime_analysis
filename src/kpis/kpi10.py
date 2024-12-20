  
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def kpi10(df):
    """# Rights under Prevention of Atrocities (POA) Act and Protection of Civil Rights (PCR) Act over years"""

    rights = df[['Year' ,'Prevention of atrocities (POA) Act' , 'Protection of Civil Rights (PCR) Act']].groupby('Year').sum().reset_index()
    rights

    # Visualise  Prevention of atrocities (POA) Act and Protection of Civil Rights (PCR) Act over years

    fig=plt.figure(figsize=(10, 7))

    sns.lineplot(data=rights, x="Year", y="Protection of Civil Rights (PCR) Act", marker='o', label="PCR Act", color='orange', linewidth=2.5, markersize=10)
    sns.lineplot(data=rights, x="Year", y="Prevention of atrocities (POA) Act", marker='*', label="POA Act", color='green', linewidth=2.5, markersize=13)

    plt.title('Crimes under POA Act and PCR Act Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Crime Counts')
    plt.legend(title='Crime Acts', frameon=True)
    plt.grid()
    plt.tight_layout()
    st.pyplot(fig)
