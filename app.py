# streamlit_app.py

import streamlit as st
import pandas as pd

# # Create the SQL connection to pets_db as specified in your secrets file.
# conn = st.experimental_connection('pets_db', type='sql')

# # Insert some data with conn.session.
# with conn.session as s:
#     s.execute('CREATE TABLE IF NOT EXISTS Tommaso (person TEXT, pet TEXT);')
#     s.execute('DELETE FROM Tommaso;')
#     # pet_owners = {'filippo': 'insalata', 'barbara': 'cat', 'alex': 'puppy'}
#     # for k in pet_owners:
#     #     s.execute(
#     #         'INSERT INTO Tommaso (person, pet) VALUES (:owner, :pet);',
#     #         params=dict(owner=k, pet=pet_owners[k]),
#     #     )
#     s.commit()

# # Query and display the data you inserted
# pet_owners = conn.query('select * from Tommaso')
# st.dataframe(pet_owners)

conn = st.experimental_connection(
    # "local_db",
    type="sql",
    url="mysql://root:Platinum79@localhost:3306/ebird"
)
df_ebird = conn.query("select * from df")
st.dataframe(df_ebird)
# df_ebird = pd.read_csv("df_raw (2).csv")
# st.dataframe(df_ebird)
st.map(df_ebird.iloc[:30], size=20,latitude="lat", longitude="lng")

