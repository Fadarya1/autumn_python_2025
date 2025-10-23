# todo: Перепишите игру "Поле чудес" на классах.
import json
import random
import uuid
import datetime
from lesson_5.code.db import DICT_DEFENITION_WORD
# from db_pole import DICT_DEFENITION_WORD

# fd = open("db_pole.json", "r", encoding="utf-8")
# json_data = json.load(fd)
# DICT_DEFINITION = dict(json_data)


class Yakubovich:
    def __init__(self):
#инициализация состояния игры для пользователя
        self.name = input("Введите имя:")
        self.session_uuid = uuid.uuid4()


    def print_menu(self):
        print("""   
               1. Начать игру
               2. Сохранить игру
               3. Загрузить игру
               4. Выход из игры
               5. Настройки 
            """)
        num = int(input("Пункт меню:"))
        match num:
            case 1:
                self.key = self._generate_key()
                self.list_word = list(self.key)
                self.mask = ['#'] * len(self.key)
                self.start_game()
                # print('The UUID is: ' + str(session_uuid))
            case 2:
                pass
            case 3:
                self.load_game()
            case 4:
                print(f"Спасибо {self.name} за игру! Заходи еще! ")
                self.end_game()

    def start_game(self):
        print(DICT_DEFENITION_WORD[self.key])
        print(self.mask)
        # cnt_ = 1
        while '#' in self.mask:
            alfa = input("Введите букву:")
            if alfa == "2":
                print("Сохранение игры!")
                self.save_game()
            if alfa == "4": #ДОБАВИЛА ЭТОТ ПУНКТ
                print("Вы вышли из игры")
                exit(0)
            cnt = 0
            for i in self.key:
                if alfa == i or alfa.upper() == i:
                    self.mask[cnt] = i
                    cnt += 1
                    continue
                cnt += 1
            else:
                print(self.mask)
        print(f"{self.name}, Вы угадали это слово!")



    def save_game(self):
        # dt, id_session, name, word, mask
        f = open("save_game.csv", "at")
        dt = datetime.datetime.now()
        mask = "".join(self.mask)
        str = f"{dt}|{self.session_uuid}|{self.name}|{self.key}|{mask}\n"
        f.write(str)
        f.close()
        print("Сохранил игру!")


    def end_game(self):
        pass


    def load_game(self):
        f = open("save_game.csv", "tr")
        indx = 0
        list_str= f.readlines()
        new_list_str = []
        for csv_str in list_str:
            if self.name in csv_str:
                new_list_str.append(csv_str)
                csv_str_parts = csv_str.split("|")
                print(indx, ")", csv_str_parts[0], csv_str_parts[2])
                indx += 1
        if indx == 0:
            print("Для этого игрока нет сохраненных игр")
            exit(1)
        indx_load = int(input("Введите номер:"))
        sg = new_list_str[indx_load].split("|")
        self.key = sg[3]
        self.mask = list(sg[4].strip())
        self.start_game()
        exit(0)


    def _generate_key(self) -> str:
        keys = list(DICT_DEFENITION_WORD.keys())
        random.shuffle(keys)
        return keys.pop()


game = Yakubovich()
game.print_menu()