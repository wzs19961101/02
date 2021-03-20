from urllib import request as re
from bs4 import BeautifulSoup as BS

url = 'https://en.wikipedia.org/wiki/Pawe%C5%82_Domaga%C5%82a'
html = re.urlopen(url)
bs = BS(html.read(), 'html.parser')

#1
d1 = bs.find_all('span', {'class':'bday'})[0].text
print(d1)
#2
d2 = bs.find_all('div', {'class':'hlist hlist-separated'})[0].ul.text
print(d2)
#3
d3 = bs.find_all('div', {'class':'mw-references-wrap mw-references-columns'})[0].text
print(d3)
