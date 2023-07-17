# streamlit_app.py

import streamlit as st

conn = st.experimental_connection("local", "sql")
df = conn.query("select * from df")

df
