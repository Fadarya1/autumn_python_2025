import requests
from bs4 import BeautifulSoup
from typing import List
import json

url = "https://gist.github.com/shmookey/b28e342e1b1756c4700f42f17102c2ff"
response = requests.get(url) #запрос к серверу методом GET, в response содержится ответ от сервера
html = response.text
# print(html)

# #далее нужно распарсить эту страничку
# # Создание объекта BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
li_elements: List[object] = soup.select('tr > td') #поиск по названию тега
# print(li_elements)
mass = []
for p in soup.select("tr > td"):
    if len(p.text) == 5:
        mass.append(p.text.upper())
# print(mass)
#
txt = json.dumps(mass).encode("utf-8").decode("unicode-escape")
fd = open("Wordle5.json", "w", encoding="utf-8")
fd.write(txt)
fd.close()
