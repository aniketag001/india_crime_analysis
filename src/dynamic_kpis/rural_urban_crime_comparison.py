import matplotlib.pyplot as plt
import streamlit as st
from utils import crime_columns, state_name_mapping, fig_width, fig_height
import plotly.express as px
import pandas as pd
import ipywidgets as widgets
from ipywidgets import interactive

def rural_urban_crime_comparison(df, population_df, literacy_df):
    st.subheader("5. Crimes of Rural Urban Comparison")
    st.text("Author: Sakshi Jaiswal")

    crimes_2001 = df[df["Year"] == 2001].groupby("STATE/UT")["Total crimes"].sum().reset_index()
    crimes_2011 = df[df["Year"] == 2011].groupby("STATE/UT")["Total crimes"].sum().reset_index()
    
    # Rename columns for clarity
    crimes_2001.rename(columns={"Total crimes": "Total crimes 2001"}, inplace=True)
    crimes_2011.rename(columns={"Total crimes": "Total crimes 2011"}, inplace=True)

    # Step 2: Prepare literacy df
    rural_urban_df = {
        "STATE/UT": literacy_df["Country/ States/ Union Territories Name"],
        "LR-Rural-2001": literacy_df["Literacy Rate (Persons) - Rural - 2001"],
        "LR-Urban-2001": literacy_df["Literacy Rate (Persons) - Urban - 2001"],
        "LR-Rural-2011": literacy_df["Literacy Rate (Persons) - Rural - 2011"],
        "LR-Urban-2011": literacy_df["Literacy Rate (Persons) - Urban - 2011"]
    }

    rural_urban_df = pd.DataFrame(rural_urban_df)

    # Step 3: Merge literacy df with crime df
    merged_rural_urban_df = pd.merge(rural_urban_df, crimes_2001, on="STATE/UT", how="left")
    merged_rural_urban_df = pd.merge(merged_rural_urban_df, crimes_2011, on="STATE/UT", how="left")

    # print(crimes_2001)
    # print(merged_rural_urban_df)

    # Step 4: Display the final dfFrame
    # print(merged_rural_urban_df)


    # Set up Streamlit widgets for selecting the year and area
    year = st.selectbox("Select Year", [2001, 2011], index=0)
    area = st.selectbox("Select Area", ['Rural', 'Urban'], index=0)

    fig, ax1 = plt.subplots(figsize=(fig_width, fig_height))


    # Function to update the plot based on slider or dropdown selection
    def update_plot(year, area):
        # Clear previous plot
        ax1.clear()
        
        # Plot the selected data based on year and area
        if area == 'Rural':
            if year == 2001:
                ax1.plot(merged_rural_urban_df['STATE/UT'], merged_rural_urban_df['LR-Rural-2001'], label=f'LR Rural {year}')
            else:
                ax1.plot(merged_rural_urban_df['STATE/UT'], merged_rural_urban_df['LR-Rural-2011'], label=f'LR Rural {year}')
        elif area == 'Urban':
            if year == 2001:
                ax1.plot(merged_rural_urban_df['STATE/UT'], merged_rural_urban_df['LR-Urban-2001'], label=f'LR Urban {year}')
            else:
                ax1.plot(merged_rural_urban_df['STATE/UT'], merged_rural_urban_df['LR-Urban-2011'], label=f'LR Urban {year}')
        

        ax2 = ax1.twinx()

        # Plot the selected data based on year for total crimes
        if year == 2001:
            ax2.plot(merged_rural_urban_df['STATE/UT'], merged_rural_urban_df['Total crimes 2001'], label=f'Total Crimes {year}', color='r')
        else:
            ax2.plot(merged_rural_urban_df['STATE/UT'], merged_rural_urban_df['Total crimes 2011'], label=f'Total Crimes {year}', color='r')

        # Set plot labels and title
        ax1.set_xlabel('State/UT')
        ax1.set_ylabel('Literacy Rate (%)', color='b')
        ax2.set_ylabel('Total Crimes', color='r')
        ax1.set_title(f'Literacy Rate and Total Crimes in {area} Area ({year})')

        # Add legends for both axes
        ax1.legend(loc='upper left')
        ax2.legend(loc='upper right')

        # Rotate the x-axis labels for better visibility
        for label in ax1.get_xticklabels():
            label.set_rotation(45)

        plt.tight_layout()

        # Display the updated plot in Streamlit
        st.pyplot(fig)

    # Call the function to update the plot when the user selects a year and area
    update_plot(year, area)