

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from utils import load_crime_data, load_literacy_data, load_population_data
from static_visualization import kpi1, kpi2, kpi3, kpi4

def static_insights():
        
        df = load_crime_data()
        literacy_df = load_literacy_data()
        population_df = load_population_data()

        # df["Total crimes"] = df.iloc[:, 3:13].sum(axis=1)
        # all_crimes = ['Murder', 'Assault on women','Kidnapping and Abduction', 'Dacoity', 'Robbery', 'Arson', 'Hurt','Prevention of atrocities (POA) Act' , 'Protection of Civil Rights (PCR) Act', 'Other Crimes Against SCs']

        kpi1(df)
        kpi2(df)
        kpi3(literacy_df)
        kpi4(population_df)

        """# 2. Total crime over Years"""

        # category_filter = st.selectbox("Select Category", options=df['STATE/UT'].unique())
        crime_filter = st.selectbox("Select Crime", options= ['Total crimes' , 'Murder'])
        x_filter = st.selectbox("Select X Axis", options= ['STATE/UT' , 'Year'] )
        yearly_crime = df.groupby(x_filter)[crime_filter ].sum().reset_index()
        yearly_crime

        # Visualise total crime over years

        fig = plt.figure(figsize=(10, 4))
        sns.lineplot(x=x_filter, y=crime_filter, data=yearly_crime, color='teal' , marker='o')
        plt.title('Total Crime Over Years')
        plt.xlabel(x_filter)
        plt.ylabel(crime_filter )
        st.pyplot(fig)

        # """# 3. Total crimes against SCs as per year"""

        # yearly_crime_against_SC = df.groupby('Year')['Other Crimes Against SCs'].sum().reset_index()
        # yearly_crime_against_SC

        # """# 4. Rights under Prevention of atrocities (POA) Act and Protection of Civil Rights (PCR) Act over years"""

        # rights = df[['Year' ,'Prevention of atrocities (POA) Act' , 'Protection of Civil Rights (PCR) Act']].groupby('Year').sum().reset_index()
        # rights

        # """# 5. Crimes in top 5 states"""

        # top_5 = df.groupby('STATE/UT')['Total crimes'].sum().sort_values(ascending = False).reset_index().head(5)
        # top_5

        # """# 6. Top 5 Districts in Uttar Pradesh with crimes"""

        # UP = df[df['STATE/UT'] == 'Uttar Pradesh'][['DISTRICT' , 'Year','Total crimes'] + all_crimes].sort_values(by='Total crimes', ascending=False).head(5)
        # UP

        # """# 7. Top 5 Districts in Rajasthan with crimes"""

        # rajasthan = df[df['STATE/UT'] == 'Rajasthan'][['DISTRICT' , 'Year','Total crimes'] + all_crimes].sort_values(by='Total crimes', ascending=False).head(5)
        # rajasthan

        # """# 8. Top 5 Districts in Madhya Pradesh with crimes"""

        # MP = df[df['STATE/UT'] == 'Madhya Pradesh'][['DISTRICT' , 'Year','Total crimes'] + all_crimes].sort_values(by='Total crimes', ascending=False).head(5)
        # MP

        # """# 9. Top 5 Districts in Andhra Pradesh with crimes"""

        # AP = df[df['STATE/UT'] == 'Andhra Pradesh'][['DISTRICT' , 'Year','Total crimes'] + all_crimes].sort_values(by='Total crimes', ascending=False).head(5)
        # AP

        # """# 10. Top 5 Districts in Bihar with crimes"""

        # bihar = df[df['STATE/UT'] == 'Bihar'][['DISTRICT' , 'Year','Total crimes'] + all_crimes].sort_values(by='Total crimes', ascending=False).head(5)
        # bihar

        # df.isna().sum()

        # df.dropna(inplace=True)

        # print(f"Duplicates : {df.duplicated().sum()}")

        # df.drop_duplicates(inplace=True)

        # len(list(df["STATE/UT"].unique()))

        # print(f"Duplicates : {df.duplicated().sum()}")

        # df['STATE/UT'] = df['STATE/UT'].str.title()
        # df["STATE/UT"].unique()

        # df.describe()

        # """# Total number of each crime commited by state

        # """

        cols = ['Murder', 'Assault on women', 'Kidnapping and Abduction', 'Dacoity',
                'Robbery', 'Arson', 'Hurt', 'Prevention of atrocities (POA) Act',
                'Protection of Civil Rights (PCR) Act', 'Other Crimes Against SCs']
        fig = plt.figure(figsize=(40, 15))
        dataset_pivot = df.groupby('STATE/UT')[cols].sum()
        sns.heatmap(dataset_pivot, annot=True, fmt='.0f', cmap='GnBu')
        plt.suptitle('Number of each cases in each states')
        plt.xlabel('Types of Crimes')
        plt.ylabel('States')
        st.pyplot(fig)

        """# Total Crimes per Type:"""

        crime_type_cols = ['Murder', 'Assault on women', 'Kidnapping and Abduction', 'Dacoity', 'Robbery',
                        'Arson', 'Hurt', 'Prevention of atrocities (POA) Act', 'Protection of Civil Rights (PCR) Act',
                        'Other Crimes Against SCs']

        # Sum of each crime type of all states
        total_crimes_per_type = df[crime_type_cols].sum()
        print("Total Crimes per Type:")
        print(total_crimes_per_type)

        """# States with Higher Overall Crime Rates:"""

        crime_type_cols = ['Murder', 'Assault on women', 'Kidnapping and Abduction', 'Dacoity', 'Robbery',
                        'Arson', 'Hurt', 'Prevention of atrocities (POA) Act', 'Protection of Civil Rights (PCR) Act',
                        'Other Crimes Against SCs']
        #sum of all crime of each state/UT
        total_crimes = df.groupby('STATE/UT')[crime_type_cols].sum().sum(axis=1)

        #states with higher crime rates
        top_states = total_crimes.nlargest(5)
        print("States with Higher Overall Crime Rates:")
        print(top_states)

        """# Total Crimes per State/UT"""

        crime_type = ['Murder', 'Assault on women', 'Kidnapping and Abduction', 'Dacoity', 'Robbery',
                        'Arson', 'Hurt', 'Prevention of atrocities (POA) Act', 'Protection of Civil Rights (PCR) Act',
                        'Other Crimes Against SCs']

        #sum of all crime types for each state
        total_crimes = df.groupby('STATE/UT')[crime_type].sum().sum(axis=1)
        fig = plt.figure(figsize=(10, 4))
        sns.barplot(x=total_crimes.index, y=total_crimes)
        plt.xlabel("State/UT")
        plt.ylabel("Total Crimes")
        plt.title("Total Crimes per State/UT")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        st.pyplot(fig)
