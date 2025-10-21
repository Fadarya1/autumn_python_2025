#todo: Вы пишете скрипт для очистки временных файлов. Создайте список полных путей к временным файлам
# (с расширениями .tmp, .bak),
# добавив к каждому путь "/tmp/".
files = [
    "document.pdf",
    "temp_backup.tmp",
    "image.jpg",
    "cache.tmp",
    "report.docx",
    "old_data.bak"
]

# for line in files:
#     extension = line.split(".")
#     if extension[1] == "tmp" or extension[1] == "bak":
#         line = "/tmp/" + line
#         print(line)
# результат: ['/tmp/temp_backup.tmp', '/tmp/cache.tmp', '/tmp/old_data.bak']

temp = [f"/tmp/{line}" for line in files if ".bak" in line or ".tmp" in line]
print(temp)