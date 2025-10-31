# todo: Создайте иерархию классов для экспорта данных в разные форматы.
# Требования:
import csv
import datetime

from flask import url_for

# Абстрактный базовый класс DataExporter:
class DataExporter:
    # Методы:
    # export(self, data) - абстрактный метод
    def export(self, data):
        self.data = data

    # get_format_name(self) - возвращает название формата
    def get_format_name(self):
        return "Формат документа"

    # validate_data(self, data) - общий метод проверки данных (не пустые ли)
    @classmethod
    def validate_data(cls, data):
        cls.data = data
        if not data:
            print("Не хватает данных")
            exit(1)

# Конкретные реализации:
# JSONExporter:
# Экспортирует данные в JSON-формат

class JSONExporter(DataExporter):
    def export(self, data):
        # data.validate_data(self.data)
        time = datetime.datetime.now()
        f = open("jsonexporter.json", "wt+", encoding="utf-8")
        for item in data:
            for key in item:
                f.write(f"'{key}': '{item[key]}'\n")
                # f.write("{}: {}\n".format(key, item[key]))
            # f.write(f"{item}\n")
            # Добавляет поле "export_timestamp" с текущим временем
        f.write(f"'export timestamp' : '{time}'")
        f.close()
    def get_format_name(self):
        return "json"


# CSVExporter:
# Экспортирует данные в CSV (если data - список словарей)
# Автоматически определяет заголовки из ключей первого элемента

class CSVExporter(DataExporter):
    def export(self, data):
        # data.validate_data(self.data)
        if type(data) is list:
            for element in data:
                if type(element) != dict:
                    print("This is not a dictionary")
                    exit()
            f= open("csvexporter.csv", "wt+", encoding="utf-8", newline='')
            writer = csv.writer(f, delimiter=',')
            writer.writerow(data[0].keys())
            for item in data:
                writer.writerow(item.values())
            f.close()

    def get_format_name(self):
        return "csv"


# XMLExporter:
# Создает XML структуру с корневым элементом <report>
class XMLExporter(DataExporter):
    def export(self, data):
        # data.validate_data(self.data)
        f = open("xmlexporter.xml", "wt+", encoding="utf-8")
        f.write('<report>\n')
        for item in data:
            for key, value in item.items():
                f.write(f'name="{key}" value="{value}"\n')
        f.write('</report>')
        f.close()
    def get_format_name(self):
        return "xml"

# HTMLExporter (дополнительно):
# Создает красивую HTML-таблицу с CSS-стилями
class HTMLExporter(DataExporter):
    def export(self, data):
        # data.validate_data(self.data)
        f_ = open("htmlexporter_style.css", "wt+", encoding="utf-8")
    #СТИЛЬ ДЛЯ СТРАНИЧКИ HTML
        f_.write("""
table {
  width: 800px;
  border-collapse: collapse;
  overflow: hidden;
  box-shadow: 0 0 20px rgba(0,0,0,0.1);
}
th { border: 1px solid grey; background-color: #90CAF9 }
td { border: 1px solid grey; background-color: #BBDEFB}
body {
    text-align: center;
    margin: 10;
    font-family: Verdana, Arial, sans-serif;
    font-size: 20px;
    color: darkslategrey;
    background-color: #E3F2FD;
}
""")
        f_.close()
        f = open("htmlexporter.html", "wt+", encoding="utf-8")
        f.write('<!DOCTYPE html> <html>\n <link href="htmlexporter_style.css" rel="stylesheet">\n'
                '<table align ="center" valign ="middle">\n <tr>\n <th> Product </th>\n <th> Price </th>\n <th> Quantity </th>\n</tr>')
        for item in data:
            f.write(f"<tr>\n")
            for k, v in item.items():
                f.write(f"<td> {v} </td>\n")
            f.write(f"</tr>\n")
        f.write(f"</table>\n</html>")
        f.close()
    def get_format_name(self):
        return "html"

# Этот код должен работать после реализации:
sales_data = [
    {"product": "Laptop", "price": 1000, "quantity": 2},
    {"product": "Mouse", "price": 50, "quantity": 10}
]

exporters = [
    JSONExporter(),
    CSVExporter(),
    XMLExporter(),
    HTMLExporter()
]

for exporter in exporters:
    print(f"Формат: {exporter.get_format_name()}")
    # exporter.validate_data(sales_data)
    exporter.export(sales_data)
    print("---")