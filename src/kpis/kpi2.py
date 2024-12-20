
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from utils import crime_columns


def kpi2(df):
    yearly_crime = df.groupby('Year')[crime_columns].sum()
    correlation_matrix = yearly_crime.corr()
    fig = sns.heatmap(correlation_matrix, annot=True, cmap='viridis')
    plt.title("Yearly Crime Type Correlations")
    st.pyplot(fig)

