import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
from funciones import *

st.set_page_config(page_title = "Newsline", page_icon = ":newspaper:", layout = "wide")

def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Create a BeautifulSoup object
        soup = BeautifulSoup(response.content, 'html.parser')

        reviews = soup.find_all('div', class_='review')

        # Return the extracted information
        return reviews

    else:
        # If the request was unsuccessful, return None
        return None

cba = pag_categoria("cordoba","a")

argi = pag_categoria("infobae", "inicio")
arge = pag_categoria("infobae", "economia")
argd = pag_categoria("infobae", "deportes")
args = pag_categoria("infobae", "sociedad")

# Streamlit app
def main():

    st.markdown(
    """
    <style>
    body {
        background-color: #0E1117;
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    # Create a sidebar menu
    st.sidebar.title("Menu")
    pages = ["Home", "Córdoba", "Argentina", "Global"]
    selected_page = st.sidebar.selectbox("Select a page", pages)
    
    if selected_page == "Home":
        st.header("¡Well come, we are Newsline!")
        st.markdown("We have all the news you want, from **wherever** you want and **whenever** you want")
        

    elif selected_page == "Córdoba":
        st.header("Córdoba news")
        st.markdown("Here we can find the latest news from **Córdoba**")
        
        datos = [
        {
            'titulo': cba[1][0],
            'texto': cba[2][0],
            'imagen': cba[0][0],
        },
        {
            'titulo': cba[1][1],
            'texto': cba[2][1],
            'imagen': cba[0][1],
        },    
        {
            'titulo': cba[1][2],
            'texto': cba[2][2],
            'imagen': cba[0][2],
        },
        {
            'titulo': cba[1][3],
            'texto': cba[2][3],
            'imagen': cba[0][3],
        },   
        {
            'titulo': cba[1][4],
            'texto': cba[2][4],
            'imagen': cba[0][4],
        },   
        ]

        

        # Crear un DataFrame de Pandas con los datos
        df = pd.DataFrame(datos)

        for i, dato in df.iterrows():
            col1, col2 = st.columns([2, 1])
            col1.title(dato['titulo'])
            col1.write(dato['texto'])
            col2.image(dato['imagen'], width=400)

    elif selected_page == "Argentina":
        col1, col2 = st.columns(2)

        with col1:
            st.header("Argentine news")
            st.markdown("Here we can find the latest news from **Argentina**")

        datos = [
        {
            'titulo': argi[0][0],
            'texto': argi[2][1],
            'imagen': argi[1][0],
        },
        {
            'titulo': argi[0][1],
            'texto': argi[2][2],
            'imagen': argi[1][1],
        },
        {
            'titulo': argi[0][2],
            'texto': argi[2][0],
            'imagen': argi[1][2],
        },

        {
            'titulo': arge[0][0],
            'texto': arge[2][1],
            'imagen': arge[1][0],
        },
        {
            'titulo': arge[0][1],
            'texto': arge[2][2],
            'imagen': arge[1][1],
        },
        {
            'titulo': arge[0][2],
            'texto': arge[2][0],
            'imagen': arge[1][2],
        },        
        ]

        df = pd.DataFrame(datos)

        for i, dato in df.iterrows():
            col1, col2 = st.columns([2, 1])
            col1.title(dato['titulo'])
            col1.write(dato['texto'])
            col2.image(dato['imagen'], width=400)    

        """        with col2:
                    option = st.selectbox(
                        "How would you like to read?",
                        ("All", "Sport", "Economy", "Society"),
                    )
                    if option == "All":
                        st.image(cba[0][0])

                    elif option == "Sport":
                        st.image(cba[2][0])

                    elif option == "Economy":
                        st.image(cba[1][0])"""

        
    
    elif selected_page == "Global":
        col1, col2 = st.columns(2)

        with col1:
            st.header("Global news")
            st.markdown("Here we can find the latest news from the **World**")

        with col2:
            option = st.selectbox(
                "How would you like to read?",
                ("All", "Science", "Economy", "Culture"),
            )


if __name__ == '__main__':
    main()

