# streamlit_app.py
import streamlit as st
from streamlit_elements import elements, mui, html, dashboard


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


with elements("callbacks_retrieve_data"):

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
    mui.TextField(
            label="My text input",
            onChange=handle_change,
            defaultValue="Small",
            variant="standard",
            size="small",
            color="warning"
        )

with elements("dashboard"):

    # You can create a draggable and resizable dashboard using
    # any element available in Streamlit Elements.

    # First, build a default layout for every element you want to include in your dashboard

    layout = [
        # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
        dashboard.Item("first_item", 0, 0, 2, 2, isDraggable=True, isResizable=True),
        dashboard.Item("second_item", 2, 0, 2, 2, isDraggable=False, moved=False),
        dashboard.Item("third_item", 0, 2, 1, 1, isResizable=False),
    ]

    # Next, create a dashboard layout using the 'with' syntax. It takes the layout
    # as first parameter, plus additional properties you can find in the GitHub links below.

    with dashboard.Grid(layout):
        
        # mui.TextField(
        #     label="My text input dashborad",
        #     defaultValue="Small",
        #     variant="standard",
        #     size="small",
        #     color="warning",
        #     key="first_item"
        # )

        from streamlit_elements import nivo

        DATA = [
            { "taste": "fruity", "chardonay": 93, "carmenere": 61, "syrah": 114 },
            { "taste": "bitter", "chardonay": 91, "carmenere": 37, "syrah": 72 },
            { "taste": "heavy", "chardonay": 56, "carmenere": 95, "syrah": 99 },
            { "taste": "strong", "chardonay": 64, "carmenere": 90, "syrah": 30 },
            { "taste": "sunny", "chardonay": 119, "carmenere": 94, "syrah": 103 },
        ]
    
        # with mui.Box(sx={"height": 500}):
        nivo.Radar(
            key="first_item",
            data=DATA,
            keys=[ "chardonay", "carmenere", "syrah" ],
            indexBy="taste",
            valueFormat=">-.2f",
            margin={ "top": 70, "right": 80, "bottom": 40, "left": 80 },
            borderColor={ "from": "color" },
            gridLabelOffset=36,
            dotSize=10,
            dotColor={ "theme": "background" },
            dotBorderWidth=2,
            motionConfig="wobbly",
            legends=[
                {
                    "anchor": "top-left",
                    "direction": "column",
                    "translateX": -50,
                    "translateY": -40,
                    "itemWidth": 80,
                    "itemHeight": 20,
                    "itemTextColor": "#999",
                    "symbolSize": 12,
                    "symbolShape": "circle",
                    "effects": [
                        {
                            "on": "hover",
                            "style": {
                                "itemTextColor": "#000"
                            }
                        }
                    ]
                }
            ],
            theme={
                "background": "#FFFFFF",
                "textColor": "#31333F",
                "tooltip": {
                    "container": {
                        "background": "#FFFFFF",
                        "color": "#31333F",
                    }
                }
            }
        )


        # mui.Paper("First item", key="first_item")
        mui.Paper("Second item (cannot drag)", key="second_item")
        mui.Paper("Third item (cannot resize)", key="third_item")



    
    
