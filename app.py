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
df1 = pd.read_sql(q1, engine)

st.dataframe(df1)
