import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns
import streamlit as st
from utils import load_crime_data, load_literacy_data, load_population_data
from kpis.total_crime_over_years import total_crime_over_years
from kpis.crime_rates_by_category import crime_rates_by_category
from kpis.top_10_states_highest_crime import top_10_states_highest_crime
from kpis.each_crime_category_over_years import each_crime_category_over_years

def static_insights():
        
        df = load_crime_data()
        literacy_df = load_literacy_data()
        population_df = load_population_data()
     
        crime_rates_by_category(df)
        total_crime_over_years(df)
        top_10_states_highest_crime(df)
        each_crime_category_over_years(df)
        # kpi3(literacy_df)

        # kpi4(population_df)

        # kpi5(df)




        # cols = ['Murder', 'Assault on women', 'Kidnapping and Abduction', 'Dacoity',

        #         'Robbery', 'Arson', 'Hurt', 'Prevention of atrocities (POA) Act',

        #         'Protection of Civil Rights (PCR) Act', 'Other Crimes Against SCs']

        # fig = plt.figure(figsize=(40, 15))

        # dataset_pivot = df.groupby('STATE/UT')[cols].sum()

        # sns.heatmap(dataset_pivot, annot=True, fmt='.0f', cmap='GnBu')

        # plt.suptitle('Number of each cases in each states')

        # plt.xlabel('Types of Crimes')

        # plt.ylabel('States')
        # st.pyplot(fig)


        # """# Total Crimes per Type:"""


        # crime_type_cols = ['Murder', 'Assault on women', 'Kidnapping and Abduction', 'Dacoity', 'Robbery',

        #                 'Arson', 'Hurt', 'Prevention of atrocities (POA) Act', 'Protection of Civil Rights (PCR) Act',

        #                 'Other Crimes Against SCs']


        # # Sum of each crime type of all states

        # total_crimes_per_type = df[crime_type_cols].sum()

        # print("Total Crimes per Type:")
        # print(total_crimes_per_type)


        # """# States with Higher Overall Crime Rates:"""


        # crime_type_cols = ['Murder', 'Assault on women', 'Kidnapping and Abduction', 'Dacoity', 'Robbery',

        #                 'Arson', 'Hurt', 'Prevention of atrocities (POA) Act', 'Protection of Civil Rights (PCR) Act',

        #                 'Other Crimes Against SCs']

        # #sum of all crime of each state/UT

        # total_crimes = df.groupby('STATE/UT')[crime_type_cols].sum().sum(axis=1)


        # #states with higher crime rates

        # top_states = total_crimes.nlargest(5)

        # print("States with Higher Overall Crime Rates:")
        # print(top_states)


        # """# Total Crimes per State/UT"""


        # crime_type = ['Murder', 'Assault on women', 'Kidnapping and Abduction', 'Dacoity', 'Robbery',

        #                 'Arson', 'Hurt', 'Prevention of atrocities (POA) Act', 'Protection of Civil Rights (PCR) Act',

        #                 'Other Crimes Against SCs']


        # #sum of all crime types for each state

        # total_crimes = df.groupby('STATE/UT')[crime_type].sum().sum(axis=1)

        # fig = plt.figure(figsize=(10, 4))

        # sns.barplot(x=total_crimes.index, y=total_crimes)

        # plt.xlabel("State/UT")

        # plt.ylabel("Total Crimes")

        # plt.title("Total Crimes per State/UT")

        # plt.xticks(rotation=45, ha='right')

        # plt.tight_layout()
        # st.pyplot(fig)


        # # Total crime with its types in number of years

        # crime_type_cols = ['Murder', 'Assault on women', 'Kidnapping and Abduction', 'Dacoity', 'Robbery', 

        #           'Arson', 'Hurt', 'Prevention of atrocities (POA) Act', 'Protection of Civil Rights (PCR) Act', 

        #           'Other Crimes Against SCs']


        # # Calculate the sum of all crime types for each year

        # total_crimes_year = df.groupby('Year')[crime_type_cols].sum().sum(axis=1)


        # # Create a bar chart to visualize crime trends over years

        # fig = plt.figure(figsize=(10, 6))

        # plt.bar(total_crimes_year.index, total_crimes_year.values)

        # plt.xlabel('Year')

        # plt.ylabel('Total Crimes')

        # plt.title('Crime Trends Over Years')

        # plt.grid(True)

        # plt.tight_layout()
        # st.pyplot(fig)
        

        # #shows highest crime rate with their types

        # crime_type_cols = ['Murder', 'Assault on women', 'Kidnapping and Abduction', 'Dacoity', 'Robbery', 

        #           'Arson', 'Hurt', 'Prevention of atrocities (POA) Act', 'Protection of Civil Rights (PCR) Act', 

        #           'Other Crimes Against SCs']

        # crimes_type = df[crime_type_cols].sum()

        # top_crimes = crimes_type.nlargest(5)

        # fig = plt.figure(figsize=(10, 8))

        # plt.pie(top_crimes, labels=top_crimes.index, autopct='%1.1f%%', startangle=140)

        # plt.title("Top 5 Crime Types with Highest Occurrences")

        # plt.tight_layout()
        # st.pyplot(fig)

