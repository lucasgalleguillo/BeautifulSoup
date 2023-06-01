<<<<<<< HEAD
from bs4 import BeautifulSoup
import requests

r = requests.get('https://listado.mercadolibre.com.ar/parlante-jbl')

r.status_code

soup = BeautifulSoup(r.content, 'html.parser')

titulos = soup.find_all('h2', attrs={"class":'ui-search-item__title shops__item-title'})
titulos = [i.text for i in titulos]

urls = soup.find_all ('a', attrs={"class":'ui-search-item__group__element shops__items-group-details ui-search-link'})
urls = [i.get('href') for i in urls]

=======
import requests
from bs4 import BeautifulSoup

def cordoba_info():
    page = requests.get("https://viapais.com.ar/cordoba/")
    soup = BeautifulSoup(page.content, "html.parser")

    titulares_cba = soup.find_all("div", class_="article-inner")

    cont = 0
    titules_list = list()
    urls_list = list()

    for titulares_imp in titulares_cba:
        if cont != 7:
            titule = titulares_imp.find(class_="article-title").text
            img = titulares_imp.find("img")
            
            if cont == 0:
                url = img.get("src")
            else:
                url = img.get("data-src")
            
            titules_list.append(titule)
            urls_list.append(url)
            
            cont = cont +1
        else:
            break

    print(urls_list)
    print(titules_list)

def mundo_info(url_page, class_li, type_titule ):

    page = requests.get(url_page)
    soup = BeautifulSoup(page.content, "html.parser")

    titulares_mundo = soup.find_all("li", class_=class_li)

    cont = 0   

    titules_list = list()
    url_list = list()
    url_notice_list = list()

    for titulares_imp in titulares_mundo:
        if cont != 6:
            titule = titulares_imp.find(type_titule).text
            
            img = titulares_imp.find("img")
            url = img.get("src")
            
            notice = titulares_imp.find("a")
            url_notice = notice.get("href")
                
            titules_list.append(titule)
            url_list.append(url)
            url_notice_list.append(url_notice)

            cont = cont +1
        else:
            break

    print(titules_list)
    print(url_list)
    print(url_notice_list)

categoria = int(input("ingrese categoria: "))

match categoria:
        case 1:
            mundo_info("https://www.bbc.com/mundo", "ebmt73l0 bbc-lpu9rr e13i2e3d1", "h3")
        case 2:
            mundo_info("https://www.bbc.com/mundo/topics/c06gq9v4xp3t", "bbc-t44f9r", "h2")
        case 3:
            mundo_info("https://www.bbc.com/mundo/topics/ckdxnw959n7t", "bbc-t44f9r", "h2")
        case 4:
            mundo_info("https://www.bbc.com/mundo/topics/c2dwq9zyv4yt", "bbc-t44f9r", "h2")

        
""""
if __name__ == "__main__":
    cordoba_info() 
"""
>>>>>>> 8b2218ebb7169d8e45980719a5cbe19c3045b5ee
