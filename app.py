import streamlit as st
from deta import Deta
import pandas as pd


# Connect to Deta Base with your Data Key
deta = Deta(st.secrets["data_key"])

db = deta.Base("vdfvd")


db_content = db.fetch(limit=None).items
df = pd.DataFrame(db_content)
st.write(len(df))
st.write(df)
