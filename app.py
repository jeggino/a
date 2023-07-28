# streamlit_app.py

import streamlit as st
import pandas as pd
import pymysql
from sqlalchemy import create_engine
import streamlit as st
import mysql.connector



def view_todo():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Platinum79",
        database="ebird"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM df")
    todo = cursor.fetchall()
    conn.close()
    return todo

df1 = view_todo()
st.dataframe(df1)



