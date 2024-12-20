
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from utils import crime_columns


def kpi4(population_df):
    population_df.loc[:, "State or union territory"] = population_df["State or union territory"].replace(state_name_mapping)
    population_df = population_df[  
        population_df["State or union territory"] != "INDIA"
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
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_2001, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Correlation Between Population and Crimes in 2001')
    plt.show()

    # Plot the correlation matrix for 2011
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_2011, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Correlation Between Population and Crimes in 2011')
    plt.show()
