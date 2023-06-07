import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
from funciones import *

st.set_page_config(page_title = "Newsline", page_icon = ":newspaper:", layout = "wide")

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
    pages = ["Inicio", "Córdoba", "Argentina", "Global"]
    selected_page = st.sidebar.selectbox("Seleciona una página", pages)
    
    if selected_page == "Inicio":
        st.header("¡Bienvenido, esto es Newsline!")
        st.markdown("### Las noticias ***que quieras***, de ***donde quieras*** y ***cuando quieras***")
        st.subheader("¿Qué es Newsline?")
        st.write("A más de uno alguna vez le incomodó tener que cambiar de página para poder ver las noticias de todas partes del mundo, ya que resulta tedioso. Por lo tanto Newsline busca ofrecernos todos estos servicios en UNA SOLA PÁGINA, y lo mejor de todo es que podrás encontrar noticias desde Córdoba al mundo entero.\n")
        st.markdown("Seguinos en Instagram, Facebook, Twitter, como: 'Newsline_on'")

    elif selected_page == "Córdoba":
        cba = pag_categoria("cordoba","a")

        st.header("Noticias de Córdoba")
        st.markdown("Podrás encontrar las últimas noticias de **Córdoba**")
        
        categoria(cba, 7)

    elif selected_page == "Argentina":
        argi = pag_categoria("infobae", "inicio")
        arge = pag_categoria("infobae", "economia")
        argd = pag_categoria("infobae", "deportes")
        args = pag_categoria("infobae", "sociedad")

        col1, col2 = st.columns(2)

        with col1:
            st.header("Noticias de Argentina")
            st.markdown("Podrás encontrar las últimas noticias de **Argentina**")

        sub_categ = st.selectbox("Selecione una opción", ["Inicio", "Economía", "Deportes", "Sociedad"])
        if sub_categ == "Inicio":
            st.write("Te encuentras en el Inicio")
            categoria(argi, 3) 
        
        elif sub_categ == "Economía":
            st.write("Selecionaste las noticias de Economía")
            categoria(arge, 3)
        
        elif sub_categ == "Deportes":
            st.write("Selecionaste las noticias de Deportes")
            categoria(argd, 3)
        
        elif sub_categ == "Sociedad":
            st.write("Selecionaste las noticias de Sociedad")
            categoria(args, 3)

    elif selected_page == "Global":
        gli = pag_categoria("bbc", "inicio")
        gle = pag_categoria("bbc", "economia")
        glc = pag_categoria("bbc", "ciencia")
        glcu = pag_categoria("bbc", "cultura")

        col1, col2 = st.columns(2)

        with col1:
            st.header("Noticias Globales")
            st.markdown("Podrás encontrar las últimas noticias del **Mundo**")
        
        sub_categ = st.selectbox("Selecione una opción", ["Inicio", "Economía", "Ciencia", "Cultura"])
        if sub_categ == "Inicio":
            st.write("Te encuentras en el Inicio")
            categoria(gli, 3)
        
        elif sub_categ == "Economía":
            st.write("Selecionaste las noticias de Economía")
            categoria(gle, 3)
        
        elif sub_categ == "Ciencia":
            st.write("Selecionaste las noticias de Ciencia")
            categoria(glc, 3)
        
        elif sub_categ == "Cultura":
            st.write("Selecionaste las noticias de Cultura")
            categoria(glcu, 3)


if __name__ == '__main__':
    main()