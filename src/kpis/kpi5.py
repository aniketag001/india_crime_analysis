import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from utils import crime_columns

def kpi5(df):
        crimes_type = df[crime_columns].sum()
        top_crimes = crimes_type.nlargest(5)
        fig = plt.figure(figsize=(10, 8))
        plt.pie(top_crimes, labels=top_crimes.index, autopct='%1.1f%%', startangle=140)
        plt.title("Top 5 Crime Types with Highest Occurrences")
        plt.tight_layout()
        st.pyplot(fig)