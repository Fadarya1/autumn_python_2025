#todo: Задан шаблон config_default.txt, где каждому в текстовом файле параметру
# нужно сопоставить данные для подстановки.

# Данные для подстановки
config_values = {
    'app_name': 'NextGen',
    'version': '1.0.0',
    'debug':  True,
    'db_host': 'localhost',
    'db_port': 5432,
    'db_name': 'my_database',
    'db_user': 'admin',
    'db_password': 'secret123',
    'api_key': 'ak_123456789',
    'api_secret': 'sk_987654321',
    'base_url': 'https://api.example.com',
    'log_file': '/var/log/app.log',
    'data_dir': '/opt/app/data',
    'temp_dir': '/tmp/app',
    'max_workers': 10,
    'timeout': 30,
    'retry_attempts': 3
}
config_default = open("config_default.txt", "tr", encoding="utf-8")
list_of_data = config_default.readlines()

config = open("config.txt","w+t", encoding="utf-8")
i = 0
list_of_values = list(config_values.values())
j = 0
for line in list_of_data:
    if line.isspace() == False:
        list_of_data[i] = line.strip()
        config.writelines(f"{list_of_data[i]}\n")
        last_char = list_of_data[i][len(list_of_data[i])-1]

        if last_char == "?":
            position = config.tell()
            config.seek(position - 3)
            config.write(f"{list_of_values[j]}\n")
            j = j + 1
        i += 1
    # print(position)
    # print(position-1)
config.close()
config_default.close()
# # В итоге вместо "?" должны подставиться значения и получиться файл config.txt:
#
# # Конфигурация приложения
# app_name    =  "NextGen"
# version     =  '1.0.0'
# debug       =  True
#
# # Настройки базы данных
# db_host     =  5432


# with open("config_default.txt", "tr", encoding="utf-8") as config_default:
#     config_default.readlines()
#     print(config_default.readlines())
# with open('config_default.txt', "tr", encoding="utf-8") as config_default:
#     i = 0
#     config =list()
#     for line in config_default:
#         config.append(i)
#         config[i] = config_default.readline()
#         print(config[i])
#         i += 1