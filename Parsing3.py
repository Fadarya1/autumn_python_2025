import requests
from bs4 import BeautifulSoup
from typing import List
import json

url = "https://www.vocabineer.com/3-letter-words/"
response = requests.get(url) #запрос к серверу методом GET, в response содержится ответ от сервера
html = response.text
# print(html)

#далее нужно распарсить эту страничку
# Создание объекта BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
li_elements: List[object] = soup.select('ul > li') #поиск по названию тега
mass = []
for p in soup.select("ul > li"):
    if len(p.text) == 3:
        mass.append(p.text.upper())

txt = json.dumps(mass).encode("utf-8").decode("unicode-escape")
fd = open("Wordle3.json", "w", encoding="utf-8")
fd.write(txt)
fd.close()
