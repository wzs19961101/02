
from urllib import request as re
from bs4 import BeautifulSoup as BS
import pandas as pd


url = 'http://www.pythonscraping.com/pages/page3.html'
html = re.urlopen(url)
bs = BS(html.read(), 'html.parser')


#1.1
bs_name_list = bs.find_all('span', {'class':'excitingNote'})
for name in bs_name_list:
    print(name.get_text())
name_list = [name.get_text() for name in bs_name_list]
d = pd.DataFrame(name_list)
print(d)

#1.2
my_text = bs.find_all('tr', {'id':'gift5'})[0].td.text
print(my_text)

#1.3
my_text2 = bs.find_all('div', {'id':'footer'})[0].text
print(my_text2)
