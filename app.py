# streamlit_app.py

import streamlit as st

conn = st.experimental_connection("env:DB_CONN", "sql")
df = conn.query("select * from df")

df
