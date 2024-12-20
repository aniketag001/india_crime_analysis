

#1.Crime Trends over Years w.r.t State

  
  
def crime_trends_over_years(df):
 
    st.subheader("Each Crime Category over Years")
    st.text("Author: Aniket Agarkar")
    unique_states = df['STATE/UT'].unique()

    # Create a dropdown widget for state selection
    state_dropdown = widgets.Dropdown(
        options=unique_states,
        value=unique_states[0],  # Default to the first state
        description='Select State:'
    )

    # Function to update the chart based on state selection
    # def update_chart(state):
        # Filter the DataFrame based on the selected state
    state_df = df[df['STATE/UT'] == state]
    
    # Calculate the sum of all crime types for each year for the selected state
    total_crimes_per_year = state_df.groupby('Year')[crime_type_cols].sum().sum(axis=1)
    fig = plt.figure(figsize=(10, 6))
    plt.plot(total_crimes_per_year.index, total_crimes_per_year.values)
    plt.xlabel('Year')
    plt.ylabel('Total Crimes')
    plt.title(f'Crime Trends Over Years in {state}')
    plt.xticks(rotation=45, ha='right')
    plt.grid(True)
    st.pyplot(fig)
    # Link the dropdown widget to the chart update function

    # widgets.interactive(update_chart, state=state_dropdown)