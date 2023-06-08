import requests
from bs4 import BeautifulSoup


class Noticia:
    def __init__(self, titulo, url, img):
        self.titulo = titulo
        self.url = url
        self.img = img
    



def cordoba_info():
    page = requests.get("https://viapais.com.ar/cordoba/")
    soup = BeautifulSoup(page.content, "html.parser")

    titulares_cba = soup.find_all("div", class_="article-inner")

    cont = 0
    lista_noticia = list()

    for titulares_imp in titulares_cba:
        if cont != 7:
            titule = titulares_imp.find(class_="article-title").text
            
            img = titulares_imp.find("img")
            if cont == 0:
                url = img.get("src")
            else:
                url = img.get("data-src")
            
            notice = titulares_imp.find("a")
            url_notice = "https://viapais.com.ar" + notice.get("href")
            

            noticia = Noticia(titule, url_notice, url)
            lista_noticia.append(noticia)

            print(url_notice)
            cont = cont +1
        else:
            break

    return lista_noticia

# # ------------------------------------------------------------------------    

def mundo_info(url_page, class_li, type_titule, val):

    page = requests.get(url_page)
    soup = BeautifulSoup(page.content, "html.parser")

    titulares_mundo = soup.find_all("li", class_=class_li)

    cont = 0   

    lista_noticia=list()

    for titulares_imp in titulares_mundo:
        if cont != 6:
            titule = titulares_imp.find(type_titule).text
            
            img = titulares_imp.find("img")
            url = img.get("src")
            
            notice = titulares_imp.find("a")
            if val == 1:
                url_notice = "https://www.bbc.com" + notice.get("href")
            else:
                url_notice = notice.get("href")
                
            noticia = Noticia(titule, url_notice, url)
            lista_noticia.append(noticia)
            
            cont = cont +1
        else:
            break

    return lista_noticia
    
# # ------------------------------------------------------------------------    

def arg_info(url_page,class_a, type_title, calss_type):
    page = requests.get(url_page)
    soup = BeautifulSoup(page.content, "html.parser")

    titulares_arg = soup.find_all(calss_type, class_ = class_a)

    cont = 0

    lista_noticia = list()

    for titulares_imp in titulares_arg:
        if cont != 3:
            titule = titulares_imp.find(type_title).text
            
            img = titulares_imp.find("img")
            url = img.get("src")
        
            if calss_type == 'div':
                a = titulares_imp.find("a")
                url_notice = "https://www.infobae.com" + a.get("href")
            elif calss_type == 'a':
                url_notice = "https://www.infobae.com" + titulares_imp.get("href")
               
            noticia = Noticia(titule, url_notice, url)
            lista_noticia.append(noticia)

            cont = cont +1
        else:
            break

    return lista_noticia
    
# # ------------------------------------------------------------------------    
            
def pag_categoria(pag, categoria):
    if pag == "bbc":
        match categoria:
            case "inicio":
                return mundo_info("https://www.bbc.com/mundo", "ebmt73l0 bbc-lpu9rr e13i2e3d1", "h3", 1)
            case "economia":
                return mundo_info("https://www.bbc.com/mundo/topics/c06gq9v4xp3t", "bbc-t44f9r", "h2", 2)
            case "ciencia":
                return mundo_info("https://www.bbc.com/mundo/topics/ckdxnw959n7t", "bbc-t44f9r", "h2", 2)
            case "cultura":
                return mundo_info("https://www.bbc.com/mundo/topics/c2dwq9zyv4yt", "bbc-t44f9r", "h2", 2)
    
    elif pag=="infobae":
        match categoria:
            case "inicio":
                return arg_info("https://www.infobae.com/tag/argentina", "d23-feed-list-card", "h2", "a")
            case "economia":
                return arg_info("https://www.infobae.com/economia/", "d23-story-card-ctn", "h2", "div")
            case "deportes":
                return arg_info("https://www.infobae.com/deportes/","d23-story-card-ctn","h2", "div")
            case "sociedad":
                return arg_info("https://www.infobae.com/sociedad/","d23-feed-list-card","h2", "a")
        
    else:
        return cordoba_info()
