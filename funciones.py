import requests
from bs4 import BeautifulSoup

def cordoba_info():
    page = requests.get("https://viapais.com.ar/cordoba/")
    soup = BeautifulSoup(page.content, "html.parser")

    titulares_cba = soup.find_all("div", class_="article-inner")

    cont = 0
    titules_list = list()
    urls_list = list()
    urls_notice = list()

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
            
            titules_list.append(titule)
            urls_list.append(url)
            urls_notice.append(url_notice)

            print(url_notice)
            cont = cont +1
        else:
            break

    return urls_list, titules_list, urls_notice

# # ------------------------------------------------------------------------    

def mundo_info(url_page, class_li, type_titule):

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

    return titules_list, url_list,url_notice_list
    
# # ------------------------------------------------------------------------    


def arg_info(url_page,class_a, type_title, calss_type, num_notice):
    page = requests.get(url_page)
    soup = BeautifulSoup(page.content, "html.parser")

    titulares_arg = soup.find_all(calss_type, class_ = class_a)

    cont = 0

    titules_list = list()
    url_list = list()
    url_notice_list = list()

    for titulares_imp in titulares_arg:
        if cont != num_notice:
            titule = titulares_imp.find(type_title).text
            
            img = titulares_imp.find("img")
            url = img.get("src")
            url_notice = "https://www.infobae.com/" + titulares_imp.find_previous("a")["href"]
               
            titules_list.append(titule)
            url_list.append(url)
            url_notice_list.append(url_notice)

            cont = cont +1
        else:
            break

    return titules_list, url_list, url_notice_list
    
            

def pag_categoria(pag, categoria):
    if pag == "bbc":
        match categoria:
            case "inicio":
                return mundo_info("https://www.bbc.com/mundo", "ebmt73l0 bbc-lpu9rr e13i2e3d1", "h3")
            case "economia":
                return mundo_info("https://www.bbc.com/mundo/topics/c06gq9v4xp3t", "bbc-t44f9r", "h2")
            case "ciencia":
                return mundo_info("https://www.bbc.com/mundo/topics/ckdxnw959n7t", "bbc-t44f9r", "h2")
            case "cultura":
                return mundo_info("https://www.bbc.com/mundo/topics/c2dwq9zyv4yt", "bbc-t44f9r", "h2")
    
    elif pag=="infobae":
        match categoria:
            case "inicio":
                return arg_info("https://www.infobae.com/tag/argentina", "d23-feed-list-card", "h2", "a", 3)
            case "economia":
                return arg_info("https://www.infobae.com/economia/", "d23-story-card-ctn", "h2", "div", 3)
            case "deportes":
                return arg_info("https://www.infobae.com/deportes/","d23-story-card-ctn","h2", "div", 3)
            case "sociedad":
                return arg_info("https://www.infobae.com/sociedad/","d23-story-card-ctn","h2", "a", 3)
        
    else:
        return cordoba_info()
