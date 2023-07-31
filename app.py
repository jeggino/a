import streamlit as st
import pandas as pd
from ebird.api import get_observations
import requests
from streamlit_option_menu import option_menu



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

selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")




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
    st.sidebar.warning('Select a country', icon="⚠️")
    st.stop()

try:
    df_ebird = pd.DataFrame(records)
    df_ebird['date'] = df_ebird.obsDt.str.split(" ",expand=True)[0]
    df_ebird = df_ebird[COLUMNS]

    try:
        SPECIES = st.sidebar.multiselect("Select one o more species", df_ebird["comName"], max_selections=None, placeholder="Choose an option")

        df_filter = df_ebird[df_ebird["comName"].isin(SPECIES)]
        
        if selected2 == "Home":
            tab1, tab2, tab3, tab4  = st.tabs(["Chart 1", "Chart 2", "Chart 3", "Chart 4"])
            import altair as alt
            NUMBER = tab1.number_input("Number of species", min_value=1, max_value=50, value=10, step=1,  label_visibility="visible")
        
            source = df_filter.groupby(["comName"],as_index=False).size().sort_values('size',ascending=False).reset_index().loc[:NUMBER]
            
            bar_chart = alt.Chart(source).mark_bar().encode(
                x=alt.X(field='size', title="Number of observations"),
                y=alt.Y('comName',title="", sort="ascending", ),
            )
            
            tab1.altair_chart(bar_chart, theme=None, use_container_width=True)
    
            #---
            source = df_filter.groupby("date",as_index=False).size()
    
            heatmap = alt.Chart(source, title="Daily Max Temperatures (C) in Seattle, WA").mark_rect().encode(
                x=alt.X("date(date):O", title="Day", axis=alt.Axis(format="%e", labelAngle=0)),
                y=alt.Y("month(date):O", title="Month"),
                color=alt.Color("sum(size)", legend=alt.Legend(title=None)),
                tooltip=[
                    alt.Tooltip("monthdate(date)", title="Date"),
                    alt.Tooltip("max(size)", title="Summ of number of observations"),
                ],
            ).configure_view(step=13, strokeWidth=0).configure_axis(domain=False)
    
            tab2.altair_chart(heatmap, theme=None, use_container_width=True)
    
            #---
            source = df_filter.groupby("date",as_index=False).size()
    
            # Size of the hexbins
            size = 15
            # Count of distinct x features
            xFeaturesCount = 12
            # Count of distinct y features
            yFeaturesCount = 7
            # Name of the x field
            xField = 'date'
            # Name of the y field
            yField = 'date'
            
            # the shape of a hexagon
            hexagon = "M0,-2.3094010768L2,-1.1547005384 2,1.1547005384 0,2.3094010768 -2,1.1547005384 -2,-1.1547005384Z"
            
            hexbin = alt.Chart(source).mark_point(size=size**2, shape=hexagon).encode(
                x=alt.X('xFeaturePos:Q', axis=alt.Axis(title='Month',
                                                       grid=False, tickOpacity=0, domainOpacity=0)),
                y=alt.Y('day(' + yField + '):O', axis=alt.Axis(title='Weekday',
                                                               labelPadding=20, tickOpacity=0, domainOpacity=0)),
                stroke=alt.value('black'),
                strokeWidth=alt.value(0.2),
                fill=alt.Color('sum(size):Q', scale=alt.Scale(scheme='darkblue')),
                tooltip=['month(' + xField + '):O', 'day(' + yField + '):O', 'sum(size):Q']
            ).transform_calculate(
                # This field is required for the hexagonal X-Offset
                xFeaturePos='(day(datum.' + yField + ') % 2) / 2 + month(datum.' + xField + ')'
            ).properties(
                # Exact scaling factors to make the hexbins fit
                width=size * xFeaturesCount * 2,
                height=size * yFeaturesCount * 1.7320508076,  # 1.7320508076 is approx. sin(60°)*2
            ).configure_view(
                strokeWidth=0
            )
    
            tab3.altair_chart(hexbin, theme=None, use_container_width=True)
    
            #---
            source = df_filter.groupby("date",as_index=False).size()
    
            bar = alt.Chart(source).mark_bar().encode(
                x='date:T',
                y='size:Q'
            )
            
            rule = alt.Chart(source).mark_rule(color='red').encode(
                y='mean(size):Q'
            )
            
            tab4.altair_chart((bar + rule), theme=None, use_container_width=True)
        
        elif selected2 == "Upload":
            st.map(data=df_filter, latitude="lat", longitude="lng", color=None, size=None, zoom=None, use_container_width=True)

    except:
        st.sidebar.warning('Select a species', icon="⚠️")
        st.stop()
        
except:
    st.error('Sorry, no data', icon="🚨")
