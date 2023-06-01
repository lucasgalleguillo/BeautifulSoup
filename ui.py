import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

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
            'titulo': 'MESSISMO',
            'texto': 'Messi el mejor do mundo',
            'imagen': 'https://www.cleverfiles.com/howto/wp-content/uploads/2018/03/minion.jpg'
        },
        {
            'titulo': 'ANTONELISMO',
            'texto': 'Texto 2',
            'imagen': 'https://www.cleverfiles.com/howto/wp-content/uploads/2018/03/minion.jpg'
        },
        # Agrega más elementos si es necesario
        ]

        # Crear un DataFrame de Pandas con los datos
        df = pd.DataFrame(datos)

        for i, dato in df.iterrows():
            col1, col2 = st.columns([2, 1])
            col1.title(dato['titulo'])
            col1.write(dato['texto'])
            col2.image(dato['imagen'], width=200)

    elif selected_page == "Argentina":
        col1, col2 = st.columns(2)

        with col1:
            st.header("Argentine news")
            st.markdown("Here we can find the latest news from **Argentina**")

        with col2:
            option = st.selectbox(
                "How would you like to read?",
                ("All", "Sport", "Economy", "Society"),
            )

        
    
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
