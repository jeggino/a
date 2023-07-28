# streamlit_app.py

import streamlit as st
import pandas as pd
import pymysql
from sqlalchemy import create_engine


engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="Platinum79",
                               db="ebird"))

# Query and display the data you inserted
pet_owners = engine.query('select * from df')
st.dataframe(pet_owners)

# df_old = pd.read_sql_query("SELECT * FROM df",con=engine)[COLUMNS]

