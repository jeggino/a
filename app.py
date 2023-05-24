import streamlit as st
from deta import Deta


# Connect to Deta Base with your Data Key
deta = Deta(st.secrets["data_key"])

db = deta.Base("vdfvd")


db_content = db.fetch().items
df = pd.DataFrame(db_content)
st.write(db_content)
