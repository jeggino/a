# streamlit_app.py

import streamlit as st
import pandas as pd
import pymysql
from sqlalchemy import create_engine
# # Database connection
# conn = pymysql.connect(host="localhost", user="root", password="Platinum79", db="ebird")

# df = pd.read_sql("SELECT * FROM df",con=conn)

# # df = conn.query("select * from pet_owners")
# st.dataframe(df)

engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="Platinum79",
                               db="ebird"))

COLUMNS = ['comName', 'date', 'lat', 'lng', 'locId', 'sciName', 'subId']
API_KEY = 'm37q4mkeq3fj'
BACK = 30
COUNTRIES = ['IT','NL','FR','ES','BE','DE']

df_old = pd.read_sql_query("SELECT * FROM df",con=engine)[COLUMNS]

# conn = st.experimental_connection(
#     "local_db",
#     type="sql",
#     url="mysql://root:Platinum79@localhost:3306/ebird"
# )
# df_ebird = conn.query("select * from df")
# st.dataframe(df_ebird)
# # df_ebird = pd.read_csv("df_raw (2).csv")
# # st.dataframe(df_ebird)
# st.map(df_ebird.iloc[:30], size=20,latitude="lat", longitude="lng")

