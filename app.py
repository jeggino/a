import streamlit as st
import pandas as pd
from ebird.api import get_observations
import requests

URL = "http://fasteri.com/list/2/short-names-of-countries-and-iso-3166-codes"
API_KEY = 'm37q4mkeq3fj'
BACK = st.number_input("Number of days back", min_value=0, max_value=30, value=0, step=1,  label_visibility="visible")
COLUMNS = ['comName', 'date', 'lat', 'lng', 'locId', 'sciName', 'subId']


r = requests.get(URL)
df_code = pd.read_html(r.content)[0]
list_ = {}
for index, column in df_code.iterrows():
    list_[column['ISO 3166 code']] = column["Country name"]

COUNTRIES = st.multiselect("Select one o more countries", df_code["Country name"].tolist(), placeholder="Choose an option")
  
records = get_observations(API_KEY, COUNTRIES,back=BACK)
df_ebird = pd.DataFrame(records)
df_ebird['date'] = df_ebird.obsDt.str.split(" ",expand=True)[0]
df_ebird = df_ebird[COLUMNS]

st.dataframe(df_ebird)
