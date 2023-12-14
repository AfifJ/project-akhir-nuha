import streamlit as st

from streamlit_option_menu import option_menu

import about, sampah.book as book, home, main

page_title = "DIGITAL BOOKSTORE"
page_icon = "books"


st.set_page_config(page_title=page_title, page_icon=page_icon)


def app():
    st.title("DIGITAL BOOKSTORE")
    with st.sidebar:
        app = option_menu(
            menu_title='Digital Bookstore',
            options=['Home','Book','About'],
            icons=['house-fill','book-fill','info-circle-fill'],
            menu_icon='journal-bookmark',
            default_index=0,
            styles={
                "container": {"padding": "5!important","background-color":'black'},
                "icon": {"color": "white", "font-size": "23px"}, 
                "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
                "nav-link-selected": {"background-color": "#02ab21"},}
            )

        logout_clicked = st.button("Logout")     
        if logout_clicked:
          main.FirebaseAuthenticator().logout_user()
          st.rerun()
    
    if app == "Home":
        home.app()
    if app == "Book" :
        book.app()
    if app == 'About':
        about.app()        