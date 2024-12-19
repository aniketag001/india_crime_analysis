
import pandas as pd

def load_data():
    url = "https://raw.githubusercontent.com/sakshitechworld/india_crime_analysis/main/data/crime_by_district_rt.csv"
    df = pd.read_csv(url)
    print(df.head())
    df=pd.DataFrame(df)
    return df


def clean_data(df):
    df.drop_duplicates(inplace=True)

    # """# Checking if duplicates are dropped or not"""

    df.duplicated().sum()

    # """# Display Descriptive Stats for numerical columns of crimes only"""

    df.drop(columns=['Year']).describe()      #here we are dropping year column

    df.replace(to_replace=' ', value='', regex=True)

    # """# Adding a new column as "Total Crimes" in the Dataset"""

    df = df.reset_index(drop = True)

    return df