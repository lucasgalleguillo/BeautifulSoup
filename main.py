from bs4 import BeautifulSoup
import requests

r = requests.get('https://listado.mercadolibre.com.ar/parlante-jbl')

r.status_code

soup = BeautifulSoup(r.content, 'html.parser')

titulos = soup.find_all('h2', attrs={"class":'ui-search-item__title shops__item-title'})
titulos = [i.text for i in titulos]

urls = soup.find_all ('a', attrs={"class":'ui-search-item__group__element shops__items-group-details ui-search-link'})
urls = [i.get('href') for i in urls]

