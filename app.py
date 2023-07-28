# streamlit_app.py

import streamlit as st
import pandas as pd
import pymysql
from sqlalchemy import create_engine


engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="Platinum79",
                               db="ebird"))

COLUMNS = ['comName', 'date', 'lat', 'lng', 'locId', 'sciName', 'subId']
API_KEY = 'm37q4mkeq3fj'
BACK = 30
COUNTRIES = ['IT','NL','FR','ES','BE','DE']

# df_old = pd.read_sql_query("SELECT * FROM df",con=engine)[COLUMNS]

