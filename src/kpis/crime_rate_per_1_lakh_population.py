
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd
from utils import crime_columns, fig_width, fig_height, state_name_mapping

def crime_rate_per_1_lakh_population(df, population_df, literacy_df):
    print(df)
    st.subheader("Crime Rate Per 100,000 Population")
    st.text("Author: Sakshi Jaiswal")
    st.write(
        """
       The charts highlight the changing trends in crime rates per 100,000 population in India from 2001 to 2011, reflecting both progress and persistent challenges. 
       Crimes such as "Assault on Women" and overall "Other Crimes Against SCs" shows upward trends, pointing to growing concerns around ongoing caste-based discrimination and gender-based violence. It can also be seen that there is not much improvement in crimes like " Kidnapping and Abduction" and "Murder". However, some crimes, like "Robbery", "Protection of Civil Rights (PCR) Act", and "Hurt" have decreased, suggesting improvements in law enforcement or social conditions in these areas.

This mixed pattern emphasizes the complexity of crime dynamics. While reductions in specific crimes highlight the success of targeted interventions, the rise in others—especially caste- and gender-related violence—demands urgent policy reforms, stricter enforcement of laws, and increased public awareness.
        """
    )
    population_df.loc[:, "State or union territory"] = population_df["State or union territory"].replace(state_name_mapping)
    population_df = population_df[  
        population_df["State or union territory"] != "India"
    ]
    print(population_df["State or union territory"].unique())
    # Extract the unique state names from the crime dfset (in the same order)
    state_order = df['STATE/UT'].unique()

    # Now, sort the population dfset based on this state order
    df_population_sorted = population_df.set_index('State or union territory')
    df_population_sorted = df_population_sorted.reindex(state_order).reset_index()

    # Display the sorted population dfframe
    df_population_sorted

    # Extract relevant columns from both dfsets
    df_population_2001_2011 = population_df[['State or union territory', 'Population 2001', 'Population 2011']]
    df_crimes_2001_2011 = df[df['Year'].isin([2001, 2011])]

    # Pivot the crime df to get the crime count for each state for 2001 and 2011
    df_crimes_pivot = df_crimes_2001_2011.pivot_table(index='STATE/UT', columns='Year', 
                                                    values=['Murder', 'Assault on women', 'Kidnapping and Abduction', 
                                                            'Dacoity', 'Robbery', 'Arson', 'Hurt', 
                                                            'Prevention of atrocities (POA) Act', 
                                                            'Protection of Civil Rights (PCR) Act', 
                                                            'Other Crimes Against SCs'], 
                                                    aggfunc='sum')

    df_crimes_pivot.columns = [f'{col[0]} {col[1]}' for col in df_crimes_pivot.columns]
    # Reset index of the pivoted dfframe
    df_crimes_pivot.reset_index(inplace=True)

    # Merge the population df with the crime df on 'State or union territory'
    merged_df = pd.merge(df_population_2001_2011, df_crimes_pivot, 
                        left_on='State or union territory', right_on='STATE/UT')

    print(merged_df)
    # Now, we will calculate the correlation between population in 2001 and 2011 with crime statistics
    correlation_2001 = merged_df[['Population 2001', 'Murder 2001', 'Assault on women 2001', 'Kidnapping and Abduction 2001', 
                                    'Dacoity 2001', 'Robbery 2001', 'Arson 2001', 'Hurt 2001', 
                                    'Prevention of atrocities (POA) Act 2001', 'Protection of Civil Rights (PCR) Act 2001', 
                                    'Other Crimes Against SCs 2001']].corr()

    correlation_2011 = merged_df[['Population 2011', 'Murder 2011', 'Assault on women 2011', 'Kidnapping and Abduction 2011', 
                                    'Dacoity 2011', 'Robbery 2011', 'Arson 2011', 'Hurt 2011', 
                                    'Prevention of atrocities (POA) Act 2011', 'Protection of Civil Rights (PCR) Act 2011', 
                                    'Other Crimes Against SCs 2011']].corr()

    # Display correlation for 2001 and 2011
    print("Correlation for 2001 between Population and Crimes:")
    print(correlation_2001['Population 2001'])

    print("\nCorrelation for 2011 between Population and Crimes:")
    print(correlation_2011['Population 2011'])

    # Merge the df to get the population and crimes together
    merged_df = pd.merge(df_population_2001_2011, df_crimes_pivot, 
                           left_on='State or union territory', right_on='STATE/UT')

    # Calculate crime rate per 100,000 population for 2001
    merged_df['Murder Rate 2001'] = (merged_df['Murder 2001'] / merged_df['Population 2001']) * 100000
    merged_df['Assault on women Rate 2001'] = (merged_df['Assault on women 2001'] / merged_df['Population 2001']) * 100000
    merged_df['Kidnapping and Abduction Rate 2001'] = (merged_df['Kidnapping and Abduction 2001'] / merged_df['Population 2001']) * 100000
    merged_df['Dacoity Rate 2001'] = (merged_df['Dacoity 2001'] / merged_df['Population 2001']) * 100000
    merged_df['Robbery Rate 2001'] = (merged_df['Robbery 2001'] / merged_df['Population 2001']) * 100000
    merged_df['Arson Rate 2001'] = (merged_df['Arson 2001'] / merged_df['Population 2001']) * 100000
    merged_df['Hurt Rate 2001'] = (merged_df['Hurt 2001'] / merged_df['Population 2001']) * 100000
    merged_df['Prevention of atrocities (POA) Act Rate 2001'] = (merged_df['Prevention of atrocities (POA) Act 2001'] / merged_df['Population 2001']) * 100000
    merged_df['Protection of Civil Rights (PCR) Act Rate 2001'] = (merged_df['Protection of Civil Rights (PCR) Act 2001'] / merged_df['Population 2001']) * 100000
    merged_df['Other Crimes Against SCs Rate 2001'] = (merged_df['Other Crimes Against SCs 2001'] / merged_df['Population 2001']) * 100000

    # Calculate crime rate per 100,000 population for 2011
    merged_df['Murder Rate 2011'] = (merged_df['Murder 2011'] / merged_df['Population 2011']) * 100000
    merged_df['Assault on women Rate 2011'] = (merged_df['Assault on women 2011'] / merged_df['Population 2011']) * 100000
    merged_df['Kidnapping and Abduction Rate 2011'] = (merged_df['Kidnapping and Abduction 2011'] / merged_df['Population 2011']) * 100000
    merged_df['Dacoity Rate 2011'] = (merged_df['Dacoity 2011'] / merged_df['Population 2011']) * 100000
    merged_df['Robbery Rate 2011'] = (merged_df['Robbery 2011'] / merged_df['Population 2011']) * 100000
    merged_df['Arson Rate 2011'] = (merged_df['Arson 2011'] / merged_df['Population 2011']) * 100000
    merged_df['Hurt Rate 2011'] = (merged_df['Hurt 2011'] / merged_df['Population 2011']) * 100000
    merged_df['Prevention of atrocities (POA) Act Rate 2011'] = (merged_df['Prevention of atrocities (POA) Act 2011'] / merged_df['Population 2011']) * 100000
    merged_df['Protection of Civil Rights (PCR) Act Rate 2011'] = (merged_df['Protection of Civil Rights (PCR) Act 2011'] / merged_df['Population 2011']) * 100000
    merged_df['Other Crimes Against SCs Rate 2011'] = (merged_df['Other Crimes Against SCs 2011'] / merged_df['Population 2011']) * 100000

    # Display the first few rows of the resulting dfframe
    merged_df[['State or union territory', 'Murder Rate 2001', 'Assault on women Rate 2001', 
                    'Kidnapping and Abduction Rate 2001', 'Dacoity Rate 2001', 'Robbery Rate 2001', 
                    'Arson Rate 2001', 'Hurt Rate 2001', 'Prevention of atrocities (POA) Act Rate 2001', 
                    'Protection of Civil Rights (PCR) Act Rate 2001', 'Other Crimes Against SCs Rate 2001',
                    'Murder Rate 2011', 'Assault on women Rate 2011', 'Kidnapping and Abduction Rate 2011', 
                    'Dacoity Rate 2011', 'Robbery Rate 2011', 'Arson Rate 2011', 'Hurt Rate 2011', 
                    'Prevention of atrocities (POA) Act Rate 2011', 'Protection of Civil Rights (PCR) Act Rate 2011', 
                    'Other Crimes Against SCs Rate 2011']]

    sns.set(style="whitegrid")

    # Define a list of the crime categories to plot
    crime_columns_2001 = ['Murder Rate 2001', 'Assault on women Rate 2001', 'Kidnapping and Abduction Rate 2001', 
                        'Dacoity Rate 2001', 'Robbery Rate 2001', 'Arson Rate 2001', 'Hurt Rate 2001', 
                        'Prevention of atrocities (POA) Act Rate 2001', 'Protection of Civil Rights (PCR) Act Rate 2001', 
                        'Other Crimes Against SCs Rate 2001']

    crime_columns_2011 = ['Murder Rate 2011', 'Assault on women Rate 2011', 'Kidnapping and Abduction Rate 2011', 
                        'Dacoity Rate 2011', 'Robbery Rate 2011', 'Arson Rate 2011', 'Hurt Rate 2011', 
                        'Prevention of atrocities (POA) Act Rate 2011', 'Protection of Civil Rights (PCR) Act Rate 2011', 
                        'Other Crimes Against SCs Rate 2011']

    # Set the figure size
    fig = plt.figure(figsize=(fig_width, fig_height))

    # Plot for 2001 and 2011 side by side
    plt.subplot(1, 2, 1)  # First plot for 2001
    merged_df[crime_columns_2001].mean().sort_values().plot(kind='barh', color='skyblue')
    print(merged_df)
    plt.title('Crime Rate per 100,000 Population - 2001')
    plt.xlabel('Crime Rate per 100,000')
    plt.ylabel('Crime Type')

    plt.subplot(1, 2, 2)  # Second plot for 2011
    merged_df[crime_columns_2011].mean().sort_values().plot(kind='barh', color='salmon')
    plt.title('Crime Rate per 100,000 Population - 2011')
    plt.xlabel('Crime Rate per 100,000')
    plt.ylabel('Crime Type')

    # Display the plot
    plt.tight_layout()
    st.pyplot(fig)
