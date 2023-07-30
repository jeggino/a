import streamlit as st
import pandas as pd
import pymysql

# Create the SQL connection to pets_db as specified in your secrets file.
conn = st.experimental_connection('pets_db', type='sql')
st.write("ok")

df = pd.read_sql("SELECT * FROM df",con=conn)
st.dataframe(df)
