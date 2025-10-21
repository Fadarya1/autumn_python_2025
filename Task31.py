# todo: Извлеките IP-адреса всех запросов, которые завершились с ошибкой
# (коды ответа 4xx или 5xx).

log_entries = [
    "192.168.1.1 - GET /home 200 1.2s",
    "192.168.1.2 - POST /login 404 0.8s",
    "192.168.1.3 - GET /profile 500 2.1s",
    "192.168.1.4 - GET /about 200 0.5s",
    "192.168.1.5 - POST /submit 403 1.5s"
]

# for line in log_entries:
#     line = line.split(" ")
#     if (line[4][0] == "4") or (line[4][0] == "5"):
#         print(line[0])

#Результат: ['192.168.1.2', '192.168.1.3', '192.168.1.5']
ids = [line.split(" ")[0] for line in log_entries
       if (line.split(" ")[4][0] == "4") or (line.split(" ")[4][0] == "5")]
print(ids)

# ip_200 = [line for line in log_entries if "200" in line]
# all_entries_with_errors = [item for item in log_entries if item not in ip_200]
#
# for ip in all_entries_with_errors:
#     show_ip = ip.split(" - ")
#     print(show_ip[0])
