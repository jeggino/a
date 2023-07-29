# streamlit_app.py
import streamlit as st
from streamlit_elements import elements, mui, html


with elements("new_element"):

    mui.Typography("Hello world")
