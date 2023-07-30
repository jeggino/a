import streamlit as st
import pandas as pd
from ebird.api import get_observations
import requests


st.set_page_config(
    page_title="Ebird Cool App",
    page_icon="🪶",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


URL = "http://fasteri.com/list/2/short-names-of-countries-and-iso-3166-codes"
API_KEY = 'm37q4mkeq3fj'
BACK = st.sidebar.number_input("Number of days back", min_value=1, max_value=30, value=1, step=1,  label_visibility="visible")
COLUMNS = ['comName', 'date', 'lat', 'lng', 'locId', 'sciName', 'subId']


r = requests.get(URL)
df_code = pd.read_html(r.content)[0]
list_ = {}
for index, column in df_code.iterrows():
    list_[column["Country name"]] = column["ISO 3166 code"]

COUNTRIES = st.sidebar.multiselect("Select one o more countries", df_code["Country name"], max_selections=10, placeholder="Choose an option")


try:
    b = []
    for country in COUNTRIES:
        b.append(list_[country])
        
    records = get_observations(API_KEY, b,back=BACK)

except:
    st.stop()

try:
    df_ebird = pd.DataFrame(records)
    df_ebird['date'] = df_ebird.obsDt.str.split(" ",expand=True)[0]
    df_ebird = df_ebird[COLUMNS]
    
    col1, col2 = st.columns([2,3])
    
    with col1:
        import altair as alt
        NUMBER = st.number_input("Number of species", min_value=1, max_value=50, value=10, step=1,  label_visibility="visible")
    
        source = df_ebird.groupby(["comName"],as_index=False).size().sort_values('size',ascending=False).reset_index().loc[:NUMBER]
        
        bar_chart = alt.Chart(source).mark_bar().encode(
            x='size',
            y='comName',
            order=alt.Order(
              # Sort the segments of the bars by this field
              'comName',
              sort='descending'
            )
        )
        
        st.altair_chart(bar_chart, theme=None, use_container_width=True)
        
    
    with col2:
        st.map(data=df_ebird, latitude="lat", longitude="lng", color=None, size=None, zoom=None, use_container_width=True)

except:
    st.error('Sorry, no data', icon="🚨")
