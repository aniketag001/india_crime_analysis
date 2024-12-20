import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns
import streamlit as st
from utils import load_crime_data, load_literacy_data, load_population_data
from kpis.total_crime_over_years import total_crime_over_years
from kpis.crime_rates_by_category import crime_rates_by_category
from kpis.top_10_states_highest_crime import top_10_states_highest_crime

def static_insights():
        print("Welcome")
        df = load_crime_data()
        literacy_df = load_literacy_data()
        population_df = load_population_data()
     
        crime_rates_by_category(df)
        total_crime_over_years(df)
        top_10_states_highest_crime(df)
        
