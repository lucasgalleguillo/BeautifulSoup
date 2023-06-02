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
        st.image("https://assets.stickpng.com/images/5a0acb755a997e1c2cea10be.png")
        st.markdown("Seguinos en Instagram, Facebook, Twitter, como: 'Newsline_on'")

    elif selected_page == "Córdoba":
        st.header("Noticias de Córdoba")
        st.markdown("Podrás encontrar las últimas noticias de **Córdoba**")
        
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
            st.header("Noticias de Argentina")
            st.markdown("Podrás encontrar las últimas noticias de **Argentina**")

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
        {
            'titulo': argd[0][1],
            'texto': argd[2][0],
            'imagen': argd[1][1],
        },
        {
            'titulo': argd[0][0],
            'texto': argd[2][2],
            'imagen': argd[1][0],
        },
        {
            'titulo': argd[0][2],
            'texto': argd[2][1],
            'imagen': argd[1][2],
        },

        {
            'titulo': args[0][0],
            'texto': args[2][0],
            'imagen': args[1][0],
        },
        {
            'titulo': args[0][1],
            'texto': args[2][1],
            'imagen': args[1][1],
        },
        {
            'titulo': args[0][2],
            'texto': args[2][2],
            'imagen': args[1][2],
        },        
        ]

        df = pd.DataFrame(datos)

        for i, dato in df.iterrows():
            col1, col2 = st.columns([2, 1])
            col1.title(dato['titulo'])
            col1.write(dato['texto'])
            col2.image(dato['imagen'], width=400)    
        
    elif selected_page == "Global":
        col1, col2 = st.columns(2)

        with col1:
            st.header("Noticias Globales")
            st.markdown("Podrás encontrar las últimas noticias del **Mundo**")


            datos = [
            {
                'titulo': gli[0][0],
                'texto': gli[2][0],
                'imagen': gli[1][0],
            },
            {
                'titulo': gli[0][1],
                'texto': gli[2][1],
                'imagen': gli[1][1],
            },
            {
                'titulo': gli[0][2],
                'texto': gli[2][2],
                'imagen': gli[1][2],
            },
            {
                'titulo': gle[0][0],
                'texto': gle[2][0],
                'imagen': gle[1][0],
            },
            {
                'titulo': gle[0][1],
                'texto': gle[2][1],
                'imagen': gle[1][1],
            },
            {
                'titulo': gle[0][2],
                'texto': gle[2][2],
                'imagen': gle[1][2],
            },
            {
                'titulo': glc[0][0],
                'texto': glc[2][0],
                'imagen': glc[1][0],
            },
            {
                'titulo': glc[0][1],
                'texto': glc[2][1],
                'imagen': glc[1][1],
            },
            {
                'titulo': glc[0][2],
                'texto': glc[2][2],
                'imagen': glc[1][2],
            },
            {
                'titulo': glcu[0][0],
                'texto': glcu[2][0],
                'imagen': glcu[1][0],
            },
            {
                'titulo': glcu[0][1],
                'texto': glcu[2][1],
                'imagen': glcu[1][1],
            },
            {
                'titulo': glcu[0][2],
                'texto': glcu[2][2],
                'imagen': glcu[1][2],
            },
            ]
            df = pd.DataFrame(datos)

            for i, dato in df.iterrows():
                col1, col2 = st.columns([2, 1])
                col1.title(dato['titulo'])
                col1.write(dato['texto'])
                col2.image(dato['imagen'], width=600) 

if __name__ == '__main__':
    main()

