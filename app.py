import streamlit as st
import pandas as pd
import pydeck as pdk
import numpy as np
import geopandas


# gdf = geopandas.read_file("https://github.com/jeggino/eBird/blob/d9efbc6fc684675e3f5eb56fb84e017f0319d705/dataframe.geojson")
gdf = geopandas.GeoDataFrame.from_features("https://github.com/jeggino/eBird/blob/d9efbc6fc684675e3f5eb56fb84e017f0319d705/dataframe.geojson").set_geometry('geometry')


# gdf = geopandas.GeoDataFrame(
#     df, geometry=geopandas.points_from_xy(df.lng, df.lat), crs="EPSG:4326"
# )

gdf_scatter = gdf.dissolve(by='subId' ,aggfunc=np.size)[["comName","geometry"]].reset_index()

# Define a layer to display on a map

layer = pdk.Layer(
    "GridLayer", gdf, pickable=True, extruded=True, 
    cell_size=5000, elevation_scale=20, get_position="geometry.coordinates",
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
r = pdk.Deck(layers=[ScatterplotLayer], map_style=pdk.map_styles.LIGHT, tooltip=tooltip_dictionary["ScatterplotLayer"],)

st.pydeck_chart(pydeck_obj=r, use_container_width=True)
