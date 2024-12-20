import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from utils import clean_data, load_data


def static_insights():
        
        df = load_data()
        df = clean_data(df)

        df["Total crimes"] = df.iloc[:, 3:13].sum(axis=1)

        df.head()

        all_crimes = ['Murder', 'Assault on women','Kidnapping and Abduction', 'Dacoity', 'Robbery', 'Arson', 'Hurt','Prevention of atrocities (POA) Act' , 'Protection of Civil Rights (PCR) Act', 'Other Crimes Against SCs']

        print(all_crimes)

        print(type(all_crimes))

        """# 1. Calculating Total Crimes as per State (from highest to lowest)"""

        state_crime = df.groupby('STATE/UT')['Total crimes'].sum().sort_values(ascending = False).reset_index()
        state_crime

        # Visualize Top 10 States with Highest Crimes

        sns.barplot(x="STATE/UT", y="Total crimes", data=state_crime.head(10), palette="viridis")
        plt.title("Top 10 States with Highest Crimes")
        plt.xlabel("State")
        plt.ylabel("Total Crimes")
        plt.xticks(rotation=90)
        plt.show()
        st.pyplot(fig)

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

        """# 3. Total crimes against SCs as per year"""

        yearly_crime_against_SC = df.groupby('Year')['Other Crimes Against SCs'].sum().reset_index()
        yearly_crime_against_SC

        # Visualise total crime over years

        sns.lineplot(x='Year', y='Other Crimes Against SCs', data=yearly_crime_against_SC, color='purple' , marker='o')
        plt.title('Total crimes against SCs as per year')
        plt.xlabel('Year')
        plt.ylabel('Other Crimes Against SCs')
        plt.show()
        st.pyplot(fig)

        """# 4. Rights under Prevention of atrocities (POA) Act and Protection of Civil Rights (PCR) Act over years"""

        rights = df[['Year' ,'Prevention of atrocities (POA) Act' , 'Protection of Civil Rights (PCR) Act']].groupby('Year').sum().reset_index()
        rights

        # Visualise  Prevention of Atrocities (POA) Act and Protection of Civil Rights (PCR) Act over years

        plt.figure(figsize=(10, 7))

        sns.lineplot(data=rights, x="Year", y="Protection of Civil Rights (PCR) Act", marker='o', label="PCR Act", color='orange', linewidth=2.5, markersize=10)
        sns.lineplot(data=rights, x="Year", y="Prevention of atrocities (POA) Act", marker='*', label="POA Act", color='green', linewidth=2.5, markersize=13)

        plt.title('Crimes under POA Act and PCR Act Over the Years')
        plt.xlabel('Year')
        plt.ylabel('Crime Counts')
        plt.legend(title='Crime Acts', frameon=True)
        plt.grid()
        plt.tight_layout()
        plt.show()
        st.pyplot(fig)

        """# 5. Analysis for each Crime Type"""

        plt.figure(figsize=(12, 10))
        sns.boxplot(data=df[all_crimes])
        plt.title('Distribution of Different Crime Types')
        plt.xticks(rotation=90)
        plt.xlabel('Crime Type')
        plt.ylabel('Crime Counts')
        plt.grid()
        plt.show()
        st.pyplot(fig)

        """# 6. Analysis of Common Crime Type over Years"""

        # List of crimes
        crimes = ['Murder', 'Assault on women', 'Kidnapping and Abduction', 
                  'Dacoity', 'Robbery', 'Arson', 'Hurt', 'Other Crimes Against SCs']

        # Categorize crimes into violent and non-violent
        violent_crimes = ['Murder', 'Assault on women', 'Kidnapping and Abduction', 
                          'Dacoity', 'Robbery', 'Arson', 'Hurt']

        non_violent_crimes = ['Other Crimes Against SCs']


        plt.figure(figsize=(14, 8))

        # Plot violent crimes
        for crime in violent_crimes:
            sns.lineplot(data=df.groupby('Year')[crime].sum().reset_index(), 
                         x='Year', y=crime, marker='o', label=crime, color='red')

        # Plot non-violent crimes
        for crime in non_violent_crimes:
            sns.lineplot(data=df.groupby('Year')[crime].sum().reset_index(), 
                         x='Year', y=crime, marker='o', label=crime, color='blue')

        # Title and labels
        plt.title('Common Crime Types Over the Years')
        plt.xlabel('Year')
        plt.ylabel('Crime Counts')
        plt.legend(title='Crime Types')
        plt.grid()
        plt.show()
        st.pyplot(fig)

        df['STATE/UT'] = df['STATE/UT'].str.strip().str.title()
        df['DISTRICT'] = df['DISTRICT'].str.strip().str.title()
        
        name_mapping = {
            'A&N Islands': 'A & N Islands',
            'D&N Haveli': 'D & N Haveli',
            'Delhi Ut': 'Delhi'
            }
        cols = ['Murder', 'Assault on women', 'Kidnapping and Abduction', 'Dacoity',
                'Robbery', 'Arson', 'Hurt', 'Prevention of atrocities (POA) Act',
                'Protection of Civil Rights (PCR) Act', 'Other Crimes Against SCs']
        df['STATE/UT'] = df['STATE/UT'].replace(name_mapping)
        merged_state = df.groupby('STATE/UT')[cols].sum().reset_index()
        print(df['STATE/UT'].unique())


        df.isna().sum()

        df.dropna(inplace=True)

        print(f"Duplicates : {df.duplicated().sum()}")

        df.drop_duplicates(inplace=True)

        len(list(df["STATE/UT"].unique()))

        print(f"Duplicates : {df.duplicated().sum()}")

        df['STATE/UT'] = df['STATE/UT'].str.title()
        df["STATE/UT"].unique()

        df.describe()

        """# Total number of each crime commited by state

        """

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

        """# write code to find top 5 district with higher crime rates and show in bar chart"""

        crime_type_cols = ['Murder', 'Assault on women', 'Kidnapping and Abduction', 'Dacoity', 'Robbery',
                        'Arson', 'Hurt', 'Prevention of atrocities (POA) Act', 'Protection of Civil Rights (PCR) Act',
                        'Other Crimes Against SCs']
        #sum of all crime types for each district
        total_crimes_per_district = df.groupby('DISTRICT')[crime_type_cols].sum().sum(axis=1)
        #top 5 districts with higher crime rates
        top_districts = total_crimes_per_district.nlargest(5)
        fig = plt.figure(figsize=(10, 6))
        plt.bar(top_districts.index, top_districts.values)
        plt.xlabel('District')
        plt.ylabel('Total Crimes')
        plt.title('Top 5 Districts with Higher Crime Rates')
        plt.xticks(rotation=45, ha='right')
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

        # Total crime with its types in number of years
        crime_type_cols = ['Murder', 'Assault on women', 'Kidnapping and Abduction', 'Dacoity', 'Robbery', 
                  'Arson', 'Hurt', 'Prevention of atrocities (POA) Act', 'Protection of Civil Rights (PCR) Act', 
                  'Other Crimes Against SCs']

        # Calculate the sum of all crime types for each year
        total_crimes_year = df.groupby('Year')[crime_type_cols].sum().sum(axis=1)

        # Create a bar chart to visualize crime trends over years
        fig = plt.figure(figsize=(10, 6))
        plt.bar(total_crimes_year.index, total_crimes_year.values)
        plt.xlabel('Year')
        plt.ylabel('Total Crimes')
        plt.title('Crime Trends Over Years')
        plt.grid(True)
        plt.tight_layout()
        st.pyplot(fig)
        
        #shows highest crime rate with their types
        crime_type_cols = ['Murder', 'Assault on women', 'Kidnapping and Abduction', 'Dacoity', 'Robbery', 
                  'Arson', 'Hurt', 'Prevention of atrocities (POA) Act', 'Protection of Civil Rights (PCR) Act', 
                  'Other Crimes Against SCs']
        crimes_type = df[crime_type_cols].sum()
        top_crimes = crimes_type.nlargest(5)
        fig = plt.figure(figsize=(10, 8))
        plt.pie(top_crimes, labels=top_crimes.index, autopct='%1.1f%%', startangle=140)
        plt.title("Top 5 Crime Types with Highest Occurrences")
        plt.tight_layout()
        st.pyplot(fig)
