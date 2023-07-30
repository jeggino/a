import streamlit as st
import pandas as pd
import pymysql
from sqlalchemy import create_engine

# Create the SQL connection to pets_db as specified in your secrets file.
conn = create_engine("mysql+pymysql://{user}:{pw}@127.0.0.1/{db}".format(user="root",pw="Platinum79",db="ebird"))
st.write("ok")

df = pd.read_sql_query("SELECT * FROM df",con=conn)
st.dataframe(df)
