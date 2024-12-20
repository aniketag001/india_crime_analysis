
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import altair as alt
from utils import fig_width, fig_height

def each_crime_category_over_years(df):
 
 
    st.subheader("Each Crime Category over Years")
    st.text("Author: Sayanti Saha")

 
    # Drop the first and last columns
    df = df.drop(df.columns[[0, -1]], axis=1)

    # Define a color mapping for each crime type
    color_mapping = {
        'Murder': 'red',
        'Assault on women': 'brown',
        'Kidnapping and Abduction': 'teal',
        'Dacoity': 'orange',
        'Robbery': 'purple',
        'Arson': 'salmon',
        'Hurt': 'deeppink',
        'Prevention of atrocities (POA) Act': 'maroon',
        'Protection of Civil Rights (PCR) Act': 'magenta',
        'Other Crimes Against SCs': 'black',
    }
    # Streamlit app layout
    st.title("Crime Trends Over Years")

    # Create a dropdown for selecting the crime type
    crime_type = st.selectbox("Select Crime Type:", df.columns[1:])  # Exclude 'Year' from options


    # Function to update the plot based on selected year and crime type
    def update_plot(crime_type):
        fig = plt.figure(figsize=(10, 6))
        sns.lineplot(x=df['Year'], y=df[crime_type],  data=df, marker='o', color=color_mapping[crime_type])
        plt.title(f'Trend of {crime_type} Over Years')
        plt.xlabel('Year')
        plt.ylabel(crime_type)
        plt.xticks(df['Year'], rotation=45)
        plt.grid()
        plt.tight_layout()
        st.pyplot(fig)  # Display the plot in Streamlit

    # Call the function to update the Matplotlib plot
    update_plot(crime_type)


    # Create a long format DataFrame for Altair
    df_long = df.melt(id_vars=['Year'], var_name='Crime Type', value_name='Count')

    # Filter the DataFrame based on the selected crime type
    filtered_data = df_long[df_long['Crime Type'] == crime_type]

    # Create an Altair chart with tooltips for the selected crime type
    alt_chart = alt.Chart(filtered_data).mark_line(point=True).encode(
        x='Year:O',
        y='Count:Q',
        tooltip=['Year', 'Crime Type', 'Count']  # Tooltip showing year, crime type, and count
    ).interactive()

    # Display the Altair chart in Streamlit
    st.altair_chart(alt_chart, use_container_width=True)
