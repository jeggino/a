# streamlit_app.py
import streamlit as st
import pandas as pd
import pymysql
from sqlalchemy import create_engine


conn = pymysql.connect(
    host="localhost",
    user="root",
    password="Platinum79",
    db="ebird"
)

cursor = conn.cursor() 
query = "SELECT * FROM df"
cursor.execute(query)
record = cursor.fetchone()

if record:
    st.write("GOOOODDDDD")
else:
    st.warning(“Incorrect username or password”)


# df1 = view_todo()
# st.dataframe(df1)



