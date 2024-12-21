
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from utils import crime_columns, fig_width, fig_height


def yearly_crime_type_correlations(df, population_df, literacy_df):
    st.subheader("3. Yearly Crime Type Correlations")
    st.text("Author: Sakshi Jaiswal")
    st.write(
        """
        Using Seaborn's clustermap, we analyzed the correlations between different types of crimes against Scheduled Castes (SCs) in India.
        The resulting heatmap demonstrated a higher degree of correlation among murder, kidnapping, and assault on women relative to other offenses.
        This analysis provides insights into the complex relationships between various crimes against SCs, which can inform targeted prevention and intervention strategies.
        """

    )

    yearly_crime = df.groupby('Year')[crime_columns].sum()
    correlation_matrix = yearly_crime.corr()
    fig = plt.figure(figsize=(fig_width, fig_height))
    sns.heatmap(correlation_matrix, annot=True, cmap='viridis')
    st.pyplot(fig)

