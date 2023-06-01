import streamlit as st
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
    selected_page = st.sidebar.selectbox("Seleccione una página", pages)
    

    if selected_page == "Home":
        st.header("¡Well come, we are Newsline!")
        st.markdown("We have all the news you want, from **wherever** you want and **whenever** you want")

    elif selected_page == "Córdoba":
        st.header("Córdoba news")
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

    elif selected_page == "Argentina":
        st.header("Argentine news")
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
    
    elif selected_page == "Global":
        st.header("Global news")
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

if __name__ == '__main__':
    main()
