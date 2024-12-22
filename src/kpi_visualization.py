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
from kpis.total_crimes_across_india import total_crimes_across_india
from kpis.top_5_crimes import top_5_crimes

def kpi_insights(): 

        df = load_crime_data()

        literacy_df = load_literacy_data()

        population_df = load_population_data()
     


        charts = [

                total_crimes_across_india,

                top_10_states_highest_crime, 

                yearly_crime_type_correlations,

                total_crime_over_years,

                growth_rate_of_total_crimes,

                crime_rates_by_category,

                crime_rate_per_1_lakh_population,

                top_5_crimes

                ]


        for chart in charts:

                col1, col2 = st.columns([2, 1])

                with col1:

                        chart(df, population_df, literacy_df)

                with col2:

                        print("") 

