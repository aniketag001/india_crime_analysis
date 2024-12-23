from utils import load_crime_data, load_literacy_data, load_population_data 
from dashboard.crime_trends_over_years import crime_trends_over_years
from dashboard.each_crime_category_over_years import each_crime_category_over_years
from dashboard.crime_types_and_count_over_years import crime_types_and_count_over_years
from dashboard.state_with_top_5_crimes import state_with_top_5_crimes
from dashboard.crime_literacy_rate import crime_literacy_rate
from dashboard.rural_urban_crime_comparison import rural_urban_crime_comparison
import streamlit as st


def dashboard_insights():
        

    df = load_crime_data()

    literacy_df = load_literacy_data()

    population_df = load_population_data()
 


    charts = [

            crime_types_and_count_over_years,

            crime_literacy_rate, 

            each_crime_category_over_years,

            state_with_top_5_crimes,

            rural_urban_crime_comparison,

            crime_trends_over_years, 

            ]


    for chart in charts:

            col1, col2 = st.columns([2.5, 0.5])

            with col1:

                    chart(df, population_df, literacy_df)

            with col2:

                    print("") 
    

