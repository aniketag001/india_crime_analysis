
import streamlit as st
import ipywidgets as widgets
from utils import crime_columns
import matplotlib.pyplot as plt


def state_with_top_5_crimes(df):
 
    st.subheader("State With Top 5 Crimes")
    st.text("Author: Aniket Agarkar") 
    unique_states = df['STATE/UT'].unique()
    selected_state = st.selectbox("Select State", options=unique_states)
    state_df = df[df['STATE/UT'] == selected_state]  
    crime_type_sums = state_df[crime_columns].sum()
    crime_type_sums = crime_type_sums[crime_type_sums > 0]
    if not crime_type_sums.empty:
        top_5_crimes = crime_type_sums.nlargest(5)
        fig = plt.figure(figsize=(8, 8))
        plt.pie(top_5_crimes, labels=top_5_crimes.index, autopct='%1.1f%%', startangle=140)
        plt.title(f"Top 5 Crime Types in {selected_state}")
        st.pyplot(fig)
    else:
        print(f"No data found for {selected_state} for crime types")