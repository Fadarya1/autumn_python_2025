# # todo: добавьте во Flask маршруты для страниц (endpoint)
# - О компании
# - Контакты
# - Список постов

from flask import Flask
from flask import request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def main_website_page():
    # name = request.args.get("name", "Flask")  #htt[p:// ..../?prompt=Когда это закончится?
    # name = request.args.get("prompt", "Задай вопрос!")
    # # return "<p>Hello, World!</p>"
    # clid = request.args.get("clid", "ID")
    return "<html><H1 align='center'; style='font-family: cursive; background-color: chocolate; font-size: xxx-large'>Главная страница</H1><body style='background-color: olive'></body></html>"
@app.route("/about") #РУЧКА
def page_about():
    return "<html><H1 align='center'; style='font-family=fantasy; background-color:cadetblue'><body style='background-color: blueviolet';><p>О компании</p></H1></html>"

@app.route("/contacts") #РУЧКА
def page_contacts():
    return "<html><p><H1 align='center'; style='font-family=fantasy; background-color: hotpink'><body style='background-color: deeppink'>Контакты</p></H1></html>"

@app.route("/posts") #РУЧКА
def page_posts():
    return "<html><p><H1 align='center'; style='font-family=fantasy; background-color: goldenrod'><body style='background-color: gold'>Список постов</p></H1></html></body>"