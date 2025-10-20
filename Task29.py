# Вы получаете из API список пользователей, но нужно отфильтровать
# и преобразовать данные перед загрузкой в базу.
#Создайте список email-адресов только для активных пользователей старше 18 лет.
# Задачу следует решить с использованием списковых включений

users = [
    {"name": "alice", "email": "alice@example.com", "age": 25, "active": True},
    {"name": "bob", "email": "bob@example.com", "age": 17, "active": True},
    {"name": "charlie", "email": "charlie@example.com", "age": 30, "active": False},
    {"name": "diana", "email": "diana@example.com", "age": 16, "active": True},
    # {"name": "kira", "email": "kira@example.com", "age": 35, "active": False},
    # {"name": "lisa", "email": "lisa@example.com", "age": 40, "active": False},
    # {"name": "char", "email": "char@example.com", "age": 20, "active": True},
    # {"name": "eloisa", "email": "eloisa@example.com", "age": 18, "active": True},
    # {"name": "charles", "email": "charles@example.com", "age": 20, "active": False},
]

#Результат ['alice@example.com']
for i in range(len(users)):
    r = list({users[i]["email"] for user in users if users[i]["active"] == True if users[i]["age"] > 18})
    print(r) if r else None

# new_list = []
# for user in range(len(users)):
#     r = {k:v for (k,v) in users[user].items() if users[user]["active"] is True if users[user]["age"] > 18}
#     if r:
#         i = 0
#         new_list.append(r)
#         new_list[i] = r
#         i +=1
# print(new_list)
# for filtered_user in new_list:
#     print(filtered_user["email"])