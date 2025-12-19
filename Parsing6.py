import requests
from bs4 import BeautifulSoup
from typing import List
import json

url = "https://englishan.com/six-letter-words-in-english/"
response = requests.get(url) #запрос к серверу методом GET, в response содержится ответ от сервера
html = response.text
# print(html)

#далее нужно распарсить эту страничку
# Создание объекта BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
td_elements: List[object] = soup.select('tr > td') #поиск по названию тега
th_elements: List[object] = soup.select('tr > th')
# print(td_elements)
# print(th_elements)
mass = []
for p in soup.select('tr > td'):
#     print(p.text)
# print(mass)
    if len(p.text) == 6:
        mass.append(p.text.upper())

for p in soup.select('tr > th'):
    if len(p.text) == 6:
        mass.append(p.text.upper())
print(mass)
#
txt = json.dumps(mass).encode("utf-8").decode("unicode-escape")
fd = open("Wordle6.json", "w", encoding="utf-8")
fd.write(txt)
fd.close()
