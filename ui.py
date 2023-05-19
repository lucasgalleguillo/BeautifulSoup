import streamlit as st
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Create a BeautifulSoup object
        soup = BeautifulSoup(response.content, 'html.parser')

        # Perform web scraping here and extract the desired information
        # For example, let's extract all the reviews from the webpage
        reviews = soup.find_all('div', class_='review')

        # Return the extracted information
        return reviews

    else:
        # If the request was unsuccessful, return None
        return None

# Streamlit app
def main():
    # Set title and description
    st.title("Web Scraping de Opiniones")
    st.write("Esta es una aplicacion con el objetivo de realizar web scraping de opiniones destacadas de ciertos libros.")

    # Create a sidebar menu
    st.sidebar.title("Menú")
    pages = ["Inicio", "Web Scraping", "Acerca de"]
    selected_page = st.sidebar.selectbox("Seleccione una página", pages)

    if selected_page == "Inicio":
        st.header("¡Bienvenido!")
        st.write("Esta es una aplicación de web scraping que extrae opiniones de páginas web.")

    elif selected_page == "Web Scraping":
        st.header("Web Scraping de Opiniones")
        st.write("Ingrese la URL de una página y haga clic en el botón 'Extraer' para obtener las opiniones.")

        # Get user input
        url = st.text_input("Ingrese una URL")

        # Create a button to trigger the scraping process
        if st.button("Extraer"):
            # Call the scrape_website function
            reviews = scrape_website(url)

            if reviews is not None:
                # Display the extracted reviews
                st.header("Opiniones Extraídas")
                for review in reviews:
                    st.write(review.text)
            else:
                # Display an error message if the scraping failed
                st.write("La extracción falló. Por favor, verifique la URL e intente nuevamente.")

    elif selected_page == "Acerca de":
        st.header("Acerca de nosotros")
        st.write("Esta es una aplicación de web scraping desarrollada por alumnos de 6to año del colegio Villada con Streamlit y BeautifulSoup en Python.")

if __name__ == '__main__':
    main()
