 
from utils import load_crime_data  
from dynamic_kpis.crime_trends_over_years import crime_trends_over_years
from dynamic_kpis.each_crime_category_over_years import each_crime_category_over_years
from dynamic_kpis.crime_types_and_count_over_years import crime_types_and_count_over_years
from dynamic_kpis.state_with_top_5_crimes import state_with_top_5_crimes

def dynamic_insights():
        
    df = load_crime_data()
    state_with_top_5_crimes(df)
    crime_trends_over_years(df)
    crime_types_and_count_over_years(df)
