import streamlit as st


from streamlit_option_menu import option_menu


slected = option_menu(
    menu_title=None,
    options=["Home", "About", "Contact"],
    icons=["house", "book", "envelope"],
    menu_icon="cast",
    orientation="horizontal"
)
styles = {
    "container": {"padding": "0!important", "background-color": "#fafafa"},
    "icon": {"color": "orange", "font-size": "25px"},
    "nav-link": {"font-size": "25px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
    "nav-link-selected": {"background-color": "green"},
}


if slected == "Home":
    st.title("Home")
    st.write("This is the home page")
elif slected == "About":
    st.title("About")
    st.write("This is the about page")
else:
    st.title("Contact")
    st.write("This is the contact page")
