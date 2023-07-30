import streamlit as st
import pandas as pd
from ebird.api import get_observations
import requests

URL = "http://fasteri.com/list/2/short-names-of-countries-and-iso-3166-codes"
API_KEY = 'm37q4mkeq3fj'
BACK = st.sidebar.number_input("Number of days back", min_value=1, max_value=30, value=1, step=1,  label_visibility="visible")
COLUMNS = ['comName', 'date', 'lat', 'lng', 'locId', 'sciName', 'subId']


r = requests.get(URL)
df_code = pd.read_html(r.content)[0]
list_ = {}
for index, column in df_code.iterrows():
    list_[column["Country name"]] = column["ISO 3166 code"]

COUNTRIES = st.sidebar.selectbox("Select one o more countries", df_code["Country name"], placeholder="Choose an option")
records = get_observations(API_KEY, list_[COUNTRIES],back=BACK)

try:
    df_ebird = pd.DataFrame(records)
    df_ebird['date'] = df_ebird.obsDt.str.split(" ",expand=True)[0]
    df_ebird = df_ebird[COLUMNS]

    col1, col2 = st.columns([2,3])

    with col1:
        st.dataframe(df_ebird)

    with col2:
        st.map(data=df_ebird, latitude="lat", longitude="lng", color=None, size=None, zoom=None, use_container_width=True)

except:
    st.error('Sorry, no data', icon="🚨")
