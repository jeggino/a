import streamlit as st
import pandas as pd
from ebird.api import get_observations


API_KEY = 'm37q4mkeq3fj'
BACK = 30
COUNTRIES = ['IT','NL','FR','ES','BE','DE']
COLUMNS = ['comName', 'date', 'lat', 'lng', 'locId', 'sciName', 'subId']



records = get_observations(API_KEY, COUNTRIES,back=BACK)
df_ebird = pd.DataFrame(records)
df_ebird['date'] = df_ebird.obsDt.str.split(" ",expand=True)[0]
df_ebird = df_ebird[COLUMNS]

st.dataframe(df_ebird)
