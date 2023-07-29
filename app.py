# streamlit_app.py
import streamlit as st
from streamlit_elements import elements, mui, html


with elements("new_element"):

    mui.Typography("Hello world")


with elements("multiple_children"):

    mui.Button(
        mui.icon.EmojiPeople,
        mui.icon.DoubleArrow,
        "Button with multiple children"
    )


    with mui.Button:
        mui.icon.EmojiPeople()
        mui.icon.DoubleArrow()
        mui.Typography("Button with multiple children")
