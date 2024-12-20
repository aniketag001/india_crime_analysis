import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns
import streamlit as st
from utils import load_crime_data, load_literacy_data, load_population_data
from kpis.total_crime_over_years import total_crime_over_years
from kpis.crime_rates_by_category import crime_rates_by_category
from kpis.top_10_states_highest_crime import top_10_states_highest_crime
from kpis.growth_rate_of_total_crimes import growth_rate_of_total_crimes
from kpis.yearly_crime_type_correlations import yearly_crime_type_correlations
from kpis.crime_rate_per_1_lakh_population import crime_rate_per_1_lakh_population
from kpis.crime_trends_over_years import crime_trends_over_years

def static_insights(): 


        df = load_crime_data()
        literacy_df = load_literacy_data()
        population_df = load_population_data()
     

        charts = [
                top_10_states_highest_crime, 
                growth_rate_of_total_crimes,
                yearly_crime_type_correlations, 
                crime_rates_by_category, 
                total_crime_over_years,
                crime_rate_per_1_lakh_population,
                crime_trends_over_years
                ]

        for chart in charts:
                col1, col2 = st.columns([2, 1])
                with col1:
                        chart(df, population_df, literacy_df)
                with col2:
                        print("") 