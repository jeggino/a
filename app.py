# streamlit_app.py

import streamlit as st
import pandas as pd
import pymysql
from sqlalchemy import create_engine


engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="Platinum79",
                               db="ebird"))

q1 = 'SELECT * FROM df'

def read_df1():
  df1 = pd.read_sql_query(q1, engine)
  return df1

st.dataframe(read_df1())
