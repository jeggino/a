import streamlit as st

# Create the SQL connection to pets_db as specified in your secrets file.
conn = st.experimental_connection('pets_db', type='sql')
