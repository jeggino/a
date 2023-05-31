import streamlit as st
import pandas as pd
import pydeck as pdk
import numpy as np
import geopandas as gdf
import fiona

# -------------------------------------------------------
st.set_page_config(
    page_title="eBird",
    page_icon="🪶",
    layout="wide",
)


# -------------------------------------------------------
@st.cache_data() 
def get_data():
    df_raw =  gdf.read_file("dataframe.geojson")
    return df_raw


gdf = get_data()

st.write(gdf.info())

gdf_scatter = gdf.dissolve(by='subId' ,aggfunc=np.size)[["comName","geometry"]].reset_index()

# Define a layer to display on a map

GridLayer = pdk.Layer(
    "GridLayer", gdf, pickable=True, extruded=True, 
    cell_size=50000, elevation_scale=20, get_position="geometry.coordinates",
)

ScatterplotLayer = pdk.Layer(
    "ScatterplotLayer",
    gdf_scatter,
    pickable=True,
    opacity=0.8,
    stroked=True,
    filled=True,
    radius_scale=200,
    radius_min_pixels=gdf_scatter.comName.min(),
    radius_max_pixels=gdf_scatter.comName.max(),
    line_width_min_pixels=1,
    get_position="geometry.coordinates",
    get_radius="comName",
    get_fill_color=[255, 140, 0],
    get_line_color=[0, 0, 0],
)

tooltip_dictionary = {'ScatterplotLayer': {"text": "Name location: {subId} \nCount: {comName}"},
                      'IconLayer': {"text": "Name: {sciName} \nDatet: {date}"} }
    
# Render
r = pdk.Deck(layers=[ScatterplotLayer], map_style=pdk.map_styles.LIGHT, 
#              tooltip=tooltip_dictionary["ScatterplotLayer"]
            )
r
# st.pydeck_chart(pydeck_obj=r, use_container_width=True)
