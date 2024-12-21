import streamlit as st
import folium
import plotly.graph_objects as go
from utils import load_crime_data

def total_crimes_accross_india(df, population_df, literacy_df):

    df2 = df.copy(deep=True)
    st.subheader("Total Crimes Accross India")
    st.text("Author: Sakshi Jaiswal")

    df2['STATE/UT'] = df2['STATE/UT'].str.title()
    df2 = df2.groupby('STATE/UT').agg(
        Total_Crime=('Total crimes', 'sum')
    ).reset_index() 
    
    # plt.figure(figsize=(fig_width, fig_height))
    fig = go.Figure(data=go.Choropleth(   
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locationmode='geojson-id',
        locations=df2['STATE/UT'],
        z=df2['Total_Crime'],

        autocolorscale=False,
        colorscale='Reds',
        marker_line_color='peachpuff',

        colorbar=dict(
            title={'text': "Total Crimes"},

            thickness=15,
            len=0.35,
            bgcolor='rgba(255,255,255,0.6)',

            tick0=0,
            dtick=20000,

            xanchor='left',
            x=0.01,
            yanchor='bottom',
            y=0.05
        )
    ))

    fig.update_geos(
        visible=False,
        projection=dict(
            type='conic conformal',
            parallels=[12.472944444, 35.172805555556],
            rotation={'lat': 24, 'lon': 80}
        ),
        lonaxis={'range': [68, 98]},
        lataxis={'range': [6, 38]}
    )

    fig.update_layout(
        title=dict(
            text="Total crimes in India by State as of 2012",
            xanchor='center',
            x=0.5,
            yref='paper',
            yanchor='bottom',
            y=1,
            pad={'b': 10}
        ),
        margin={'r': 0, 't': 30, 'l': 0, 'b': 0},
        height=550,
        width=550
    )

    st.plotly_chart(fig)
