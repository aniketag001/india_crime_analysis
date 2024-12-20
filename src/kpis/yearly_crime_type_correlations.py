
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from utils import crime_columns, fig_width, fig_height


def yearly_crime_type_correlations(df, population_df, literacy_df):
    st.subheader("Yearly Crime Type Correlations")
    st.text("Author: Sakshi Jaiswal")
    yearly_crime = df.groupby('Year')[crime_columns].sum()
    correlation_matrix = yearly_crime.corr()
    fig = plt.figure(figsize=(fig_width, fig_height))
    sns.heatmap(correlation_matrix, annot=True, cmap='viridis')
    st.pyplot(fig)

