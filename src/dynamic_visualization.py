

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from utils import clean_data, load_data

def dynamic_insights():
        
        df = load_data()
        df = clean_data(df)

        df["Total crimes"] = df.iloc[:, 3:13].sum(axis=1)

        df.head()

        all_crimes = ['Murder', 'Assault on women','Kidnapping and Abduction', 'Dacoity', 'Robbery', 'Arson', 'Hurt','Prevention of atrocities (POA) Act' , 'Protection of Civil Rights (PCR) Act', 'Other Crimes Against SCs']

        print(all_crimes)

        print(type(all_crimes))

       
