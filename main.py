
import pandas as pd 
from bs4 import BeautifulSoup
import requests
import unicodedata



url = "https://www.ensenachile.cl/testimonios/"
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')
print(soup)
divs = soup.find_all('div',{'class':['row']})
div = divs.find_all('div',{'class':['container']})
print(div)
''' PANDAS CODIGO 
url = "https://en.wikipedia.org/wiki/History_of_Python"
dfs = pd.read_html(url)
df = dfs[0]
df2 = df[['Latest micro version','Release date']]
print(df2)
'''