import random
import uuid
import datetime
# from lesson_5.code.db import DICT_DEFENITION_WORD
from db_pole import DICT_DEFINITION

name = input("Введите имя:")

def print_menu():
    print("""   
       1. Начать игру
       2. Сохранить игру
       3. Загрузить игру
       4. Выход из игры
       5. Настройки 
    """)

print_menu()
num = int(input("Пункт меню:"))


def generate_key() -> str:
    keys = list(DICT_DEFINITION.keys())
    random.shuffle(keys)
    return keys.pop()


def save_game(id_session, word, mask):
    # dt, id_session, name, word, mask
    f = open("save_game.csv", "at")
    dt = datetime.datetime.now()
    mask = "".join(mask)
    str = f"{dt}|{id_session}|{name}|{word}|{mask}\n"
    f.write(str)
    f.close()
    return word
    print("Сохранил игру!")


def load_game():
    f = open("save_game.csv", "tr")
    indx = 0
    list_str= f.readlines()
    for csv_str in list_str:
        if name in csv_str:
            print(indx, ") ", csv_str[0:70])
            indx += 1
    if indx == 0:
        print("Для этого игрока нет сохраненных игр")
        exit(1)
    indx_load = int(input("Введите номер:"))
    sg = list_str[indx_load].split("|")
    key = sg[3]
    mask = sg[4]
    session_uuid = sg[1]
    # print(session_uuid,key, list(mask))
    start_game(session_uuid, key.strip(), list(mask.strip()))


def start_game(session_uuid, key, mask ):

    print(DICT_DEFINITION[key])
    print(mask)
    # cnt_ = 1
    while '#' in mask:
        alfa = input("Введите букву:")
        if alfa == "2":
            print("Сохранение игры!")
            save_game(session_uuid, key, mask)
        if alfa == "4":
            print("Вы вышли из игры")
            exit(0)
        cnt = 0
        for i in key:
            if alfa == i:
                mask[cnt] = alfa
                cnt += 1
                continue
            # else:
            #     cnt_ += 1
            cnt += 1
        else:
            print(mask)
    print(f"{name}, Вы угадали это слово!")
match num:
    case 1:
        key = generate_key()
        list_word = list(key)
        mask = ['#'] * len(key)
        session_uuid = uuid.uuid4()
        start_game(session_uuid,key,mask)
        # print('The UUID is: ' + str(session_uuid))
    case 2:
        pass
    case 3:
        load_game()
    case 4:
        print(f"Спасибо {name} за игру! Заходи еще! ")
        pass