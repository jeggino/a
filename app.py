# streamlit_app.py
import streamlit as st
from streamlit_elements import elements, mui, html


with elements("new_element"):

    mui.Typography("Hello world")


with elements("multiple_children"):

    mui.Button(
        mui.icon.EmojiPeople,
        mui.icon.AddLocation,
        "Button with multiple children"
    )


with elements("nested_children"):

   
    with mui.Paper:
        with mui.Typography:
            html.p("Hello world")
            html.p("Goodbye world")


    with mui.Button:
        mui.icon.EmojiPeople()
        mui.icon.DoubleArrow()
        mui.Typography("Button with multiple children_2")

with elements("properties"):

    with mui.Paper(elevation=3, variant="outlined", square=True):
        mui.TextField(
            label="My text input",
            # defaultValue="Type here",
            # variant="standard",
            defaultValue="Small",
            variant="standard",
            size="small",
            color="warning"
        )


    mui.Collapse(in_=True)

with elements("style_mui_sx"):

    # For Material UI elements, use the 'sx' property.
    #
    # <Box
    #   sx={{
    #     bgcolor: 'background.paper',
    #     boxShadow: 1,
    #     borderRadius: 2,
    #     p: 2,
    #     minWidth: 300,
    #   }}
    # >
    #   Some text in a styled box
    # </Box>

    mui.Box(
        "Some text in a styled box",
        sx={
            "bgcolor": "background.paper",
            "boxShadow": 1,
            "borderRadius": 2,
            "p": 2,
            "minWidth": 300,
        }
    )

with elements("style_elements_css"):

    html.div(
        "This has a hotpink background",
        css={
            "backgroundColor": "hotpink",
            "&:hover": {
                "color": "lightgreen"
            }
        }
    )

import streamlit as st

with elements("callbacks_retrieve_data"):

    # Some element allows executing a callback on specific event.
    #
    # const [name, setName] = React.useState("")
    # const handleChange = (event) => {
    #   // You can see here that a text field value
    #   // is stored in event.target.value
    #   setName(event.target.value)
    # }
    #
    # <TextField
    #   label="Input some text here"
    #   onChange={handleChange}
    # />

    # Initialize a new item in session state called "my_text"
    if "my_text" not in st.session_state:
        st.session_state.my_text = ""

    # When text field changes, this function will be called.
    # To know which parameters are passed to the callback,
    # you can refer to the element's documentation.
    def handle_change(event):
        st.session_state.my_text = event.target.value

    # Here we display what we have typed in our text field
    mui.Typography(st.session_state.my_text)

    # And here we give our 'handle_change' callback to the 'onChange'
    # property of the text field.
    mui.TextField(label="Input some text here", onChange=handle_change)
        
