# streamlit_app.py

import streamlit as st

# Create the SQL connection to pets_db as specified in your secrets file.
conn = st.experimental_connection('ebird', type='sql')

# Query and display the data you inserted
pet_owners = conn.query('select * from df')
st.dataframe(pet_owners)
