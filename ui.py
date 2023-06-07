import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
from funciones import *

st.set_page_config(page_title = "Newsline", page_icon = ":newspaper:", layout = "wide")

cba = pag_categoria("cordoba","a")
argi = pag_categoria("infobae", "inicio")
arge = pag_categoria("infobae", "economia")
argd = pag_categoria("infobae", "deportes")
args = pag_categoria("infobae", "sociedad")
gli = pag_categoria("bbc", "inicio")
gle = pag_categoria("bbc", "economia")
glc = pag_categoria("bbc", "ciencia")
glcu = pag_categoria("bbc", "cultura")


def categoria(categoria, num):
    datos = []
    for i in range(num):
        var ={
            'titulo': categoria[i].titulo,
            'texto': categoria[i].url,
            'imagen': categoria[i].img,
        }
        datos.append(var)

    # Crear un DataFrame de Pandas con los datos
    df = pd.DataFrame(datos)

    for i, dato in df.iterrows():
        col1, col2 = st.columns([2, 1])
        col1.subheader(dato['titulo'])
        col1.write(dato['texto'])
        col2.image(dato['imagen'], width=400)

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

    st.sidebar.title("Menu")
    pages = ["Home", "Córdoba", "Argentina", "Global"]
    selected_page = st.sidebar.selectbox("Seleciona una página", pages)
    
    if selected_page == "Home":
        st.header("¡Bienvenido, esto es Newsline!")
        st.markdown("### Las noticias ***que quieras***, de ***donde quieras*** y ***cuando quieras***")
        st.markdown("Seguinos en Instagram, Facebook, Twitter, como: 'Newsline_on'")

    elif selected_page == "Córdoba":
        st.header("Noticias de Córdoba")
        st.markdown("Podrás encontrar las últimas noticias de **Córdoba**")
        
        categoria(cba, 7)

    elif selected_page == "Argentina":
        col1, col2 = st.columns(2)

        with col1:
            st.header("Noticias de Argentina")
            st.markdown("Podrás encontrar las últimas noticias de **Argentina**")

        categoria(argi, 3)    
        categoria(arge, 3)
        categoria(argd, 3)
        categoria(args, 3)

    elif selected_page == "Global":
        col1, col2 = st.columns(2)

        with col1:
            st.header("Noticias Globales")
            st.markdown("Podrás encontrar las últimas noticias del **Mundo**")

            categoria(gli, 3)
            categoria(gle, 3)
            categoria(glc, 3)
            categoria(glcu, 3)

if __name__ == '__main__':
    main()