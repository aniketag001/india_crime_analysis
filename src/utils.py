
import pandas as pd

fig_width = 15
fig_height = 7

crime_columns = [
    'Murder', 'Assault on women', 'Kidnapping and Abduction', 'Dacoity', 'Robbery',
    'Arson', 'Hurt', 'Prevention of atrocities (POA) Act', 'Protection of Civil Rights (PCR) Act',
    'Other Crimes Against SCs'
] 


def load_population_data():
    url = "https://raw.githubusercontent.com/sakshitechworld/india_crime_analysis/main/data/population_of_india.csv"
    df = pd.read_csv(url)
    df = pd.DataFrame(df)
    return df

def load_literacy_data():
    url = "https://raw.githubusercontent.com/sakshitechworld/india_crime_analysis/main/data/india_literacy_rate.csv"
    df = pd.read_csv(url)
    df = pd.DataFrame(df)
    return df

def load_crime_data():
    url = "https://raw.githubusercontent.com/sakshitechworld/india_crime_analysis/main/data/crime_by_state_rt.csv"
    df = pd.read_csv(url)
    df = pd.DataFrame(df)
    df = clean_crime_data(df)
    df.loc[:, crime_columns] = df[crime_columns].apply(pd.to_numeric, errors='coerce')
    df.loc[:, 'Total crimes'] = df.loc[:, crime_columns].sum(axis=1)
    return df


def clean_crime_data(df):
    df.drop_duplicates(inplace=True)

    # """# Checking if duplicates are dropped or not"""

    df.duplicated().sum()

    # """# Display Descriptive Stats for numerical columns of crimes only"""

    df.drop(columns=['Year']).describe()      #here we are dropping year column

    df.replace(to_replace=' ', value='', regex=True)

    # """# Adding a new column as "Total Crimes" in the Dataset"""

    df = df.reset_index(drop = True)

    return df