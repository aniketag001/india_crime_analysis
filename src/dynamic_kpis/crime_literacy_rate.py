
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from utils import crime_columns, state_name_mapping, plotly_fig_width, plotly_fig_height
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

def crime_literacy_rate(df, population_df, literacy_df):
    
    st.subheader("2. Correlation Between Crime Rates and Literacy Rate")
    st.text("Author: Sakshi Jaiswal")
    col1, col2 = st.columns(2)
    with col1:    
        print(literacy_df.columns)

    
        print(literacy_df["Country/ States/ Union Territories Name"].unique())
        # Step 1: Calculate total crimes for 2001 and 2011
        crimes_2001 = df[df["Year"] == 2001].groupby("STATE/UT")["Total crimes"].sum().reset_index()
        crimes_2011 = df[df["Year"] == 2011].groupby("STATE/UT")["Total crimes"].sum().reset_index()

        # Rename columns for clarity
        crimes_2001.rename(columns={"Total crimes": "Total crimes 2001"}, inplace=True)
        crimes_2011.rename(columns={"Total crimes": "Total crimes 2011"}, inplace=True)

        # Step 2: Prepare literacy df
        literacy_df = {
            "STATE/UT": literacy_df["Country/ States/ Union Territories Name"],
            "LR-2011": literacy_df["Literacy Rate (Persons) - Total - 2011"],
            "LR-2001": literacy_df["Literacy Rate (Persons) - Total - 2001"],
        }

        literacy_df = pd.DataFrame(literacy_df)

        # Step 3: Merge literacy df with crime df
        merged_df = pd.merge(literacy_df, crimes_2001, on="STATE/UT", how="left")
        merged_df = pd.merge(merged_df, crimes_2011, on="STATE/UT", how="left")

        # Step 4: Display the final dfFrame
        merged_df
        # Calculate correlations for 2001 and 2011
        correlation_2001 = merged_df["LR-2001"].corr(merged_df["Total crimes 2001"])
        correlation_2011 = merged_df["LR-2011"].corr(merged_df["Total crimes 2011"])

        # Display the results
        print("Correlation between Literacy Rate (2001) and Total crimes (2001):", correlation_2001)
        print("Correlation between Literacy Rate (2011) and Total crimes (2011):", correlation_2011)
    

        # Create scatter plots with regression lines for 2001 and 2011
        # 2001
        # fig_2001 = plt.figure(figsize=(20, 10))
        fig_2001 = px.scatter(merged_df, x="LR-2001", y="Total crimes 2001",
                            width = plotly_fig_width, height = plotly_fig_height,
                            title="Literacy Rate vs Total Crimes (2001)",
                            labels={"LR-2001": "Literacy Rate (2001)", "Total crimes 2001": "Total Crimes (2001)"})
                

        # Fit a linear regression model for 2001
        model_2001 = LinearRegression()
        model_2001.fit(merged_df[["LR-2001"]], merged_df["Total crimes 2001"])
        line_x_2001 = np.linspace(merged_df["LR-2001"].min(), merged_df["LR-2001"].max(), 100).reshape(-1, 1)
        line_y_2001 = model_2001.predict(line_x_2001)

        # Add the regression line to the figure
        fig_2001.add_trace(go.Scatter(x=line_x_2001.flatten(), y=line_y_2001, mode='lines', name='Regression Line', line=dict(color='red')))
        st.plotly_chart(fig_2001)

    with col2:
        # 2011
        fig_2011 = px.scatter(merged_df, x="LR-2011", y="Total crimes 2011", 
                            width = plotly_fig_width, height = plotly_fig_height,
                            title="Literacy Rate vs Total Crimes (2011)",
                            labels={"LR-2011": "Literacy Rate (2011)", "Total crimes 2011": "Total Crimes (2011)"})

        # Fit a linear regression model for 2011
        model_2011 = LinearRegression()
        model_2011.fit(merged_df[["LR-2011"]], merged_df["Total crimes 2011"])
        line_x_2011 = np.linspace(merged_df["LR-2011"].min(), merged_df["LR-2011"].max(), 100).reshape(-1, 1)
        line_y_2011 = model_2011.predict(line_x_2011)

        # Add the regression line to the figure
        fig_2011.add_trace(go.Scatter(x=line_x_2011.flatten(), y=line_y_2011, mode='lines', name='Regression Line', line=dict(color='red')))

        st.plotly_chart(fig_2011)


 
