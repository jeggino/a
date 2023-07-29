# streamlit_app.py
import streamlit as st
from sqlalchemy import create_engine
import pandas as pd
from ebird.api import get_observations




engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="Platinum79",
                               db="ebird"))
pd.read_sql()
COLUMNS = ['comName', 'date', 'lat', 'lng', 'locId', 'sciName', 'subId']
API_KEY = 'm37q4mkeq3fj'
BACK = 30
COUNTRIES = ['IT','NL','FR','ES','BE','DE']

df_old = pd.read_sql("SELECT * FROM df",con=engine)[COLUMNS]

records = get_observations(API_KEY, COUNTRIES,back=BACK)
df_ebird = pd.DataFrame(records)
df_ebird['date'] = df_ebird.obsDt.str.split(" ",expand=True)[0]
df_ebird = df_ebird[COLUMNS]

df_updated = pd.concat([df_ebird,df_old],axis=0)
df_updated[['lat', 'lng']] = df_updated[['lat', 'lng']].astype("float")
df_updated.drop_duplicates(inplace=True)
df_updated.reset_index(drop=True,inplace=True)

df_updated.to_sql(con=engine, name='df', if_exists='replace')
