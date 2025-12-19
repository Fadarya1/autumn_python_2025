from config import token
import telebot, json, random, time
from telebot import types

bot = telebot.TeleBot(token)

# Словарь для хранения состояния игры каждого пользователя
game_states = {}

# список существующих размеров слов
list_of_possible_word_sizes = ['3', '4', '5', '6']

# Функция для получения пользовательских состояний
def get_user_state(user_id):
    if user_id not in game_states:
        game_states[user_id] = {
            'THE_WORD_U_NEED_TO_GUESS': None,
            'CURRENT_MASK': None,
            'WORD_LENGTH': None,
            'DIFFICULTY': None,
            'START_TIME': None,
            'TOTAL_TIME': None
        }
    return game_states[user_id]


@bot.message_handler(commands=['start'])
def welcome_message(message):
    user_id = message.from_user.id
    bot.send_message(user_id, f"Welcome to MyWordleGame, {message.from_user.first_name}!\n")
    choosing_difficulty(message)

def creating_word(number, message):
    try:
        with open(f"Wordle{int(number)}.json", "r", encoding="utf-8") as fd:
            json_data = json.load(fd)
            random.shuffle(json_data)
            return json_data.pop()
    except FileNotFoundError:
        bot.send_message(message.chat.id, "File not found.")
        return None


class GuessTry:
    def __init__(self, word, the_word_you_need_to_guess):
        self.word = word.text.upper()
        if not self.word.isalpha():
            bot.send_message(word.from_user.id, "You should use only letters of English alphabet")
            return
        elif len(self.word) != len(the_word_you_need_to_guess):
            bot.send_message(word.from_user.id, f"The word's length is {len(the_word_you_need_to_guess)}")
            return

def word_check(guess, mask, the_word_you_need_to_guess, message):
    user_id = message.from_user.id
    user_state = get_user_state(user_id)

    with open(f"Wordle{user_state['WORD_LENGTH']}.json", "r", encoding="utf-8") as fd:
        json_data = json.load(fd)
        if guess in json_data and user_state['DIFFICULTY'] == "EASY LEVEL":
            for position in range(len(the_word_you_need_to_guess)):
                if the_word_you_need_to_guess[position] == guess[position]:
                    mask[position] = the_word_you_need_to_guess[position]
                elif guess[position] in the_word_you_need_to_guess:
                    mask[position] = "☯️"
                else:
                    mask[position] = "❌"
            return mask
        elif guess in json_data and user_state['DIFFICULTY'] == "HARD LEVEL":
            absolutely_correct = 0
            letter_exists = 0
            wrong_letters = 0
            for position in range(len(the_word_you_need_to_guess)):
                if the_word_you_need_to_guess[position] == guess[position]:
                    absolutely_correct += 1
                elif guess[position] in the_word_you_need_to_guess:
                    letter_exists += 1
                else:
                    wrong_letters += 1
            mask = f"{wrong_letters} ❌ {letter_exists} ☯️ {absolutely_correct} ✅"
            return mask
        else:
            bot.send_message(message.from_user.id, "This word is not in my dictionary. Please try another word.")
            return mask


def creating_mask(the_word_u_need_to_guess):
    return ["❌"] * len(the_word_u_need_to_guess)


# Функция выбора уровня сложности
def choosing_difficulty(message):
    user_id = message.from_user.id
    # user_state = get_user_state(user_id)


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn7 = types.KeyboardButton("EASY LEVEL")
    btn8 = types.KeyboardButton("HARD LEVEL")
    markup.add(btn7, btn8)

    bot.send_message(
        user_id,
        "Choose difficulty of the game: ",
        reply_markup=markup
    )

    bot.register_next_step_handler(message, choosing_word_size)


# Функция выбора размера слова
def choosing_word_size(message):
    user_id = message.from_user.id
    user_state = get_user_state(user_id)
    if message.text == "EASY LEVEL" or message.text == "HARD LEVEL":
        user_state['DIFFICULTY'] = message.text
    elif message.text == "/howto":
        rules(message)
    elif message.text == "/score":
        score(message)
    if user_state['DIFFICULTY'] is None:
        return

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn3 = types.KeyboardButton("3")
    btn4 = types.KeyboardButton("4")
    btn5 = types.KeyboardButton("5")
    btn6 = types.KeyboardButton("6")
    markup.add(btn3, btn4, btn5, btn6)

    bot.send_message(
        user_id,
        "Now choose a number between 3 and 6 (word size)",
        reply_markup=markup
    )

    bot.register_next_step_handler(message, processing_game)


# Получение необходимых параметров для игры
def processing_game(message):
    user_id = message.from_user.id
    user_state = get_user_state(user_id)
    if message.text == "/howto":
        rules(message)
    elif message.text == "/score":
        score(message)
    if message.text in list_of_possible_word_sizes:
        user_state['WORD_LENGTH'] = message.text
    elif user_state['WORD_LENGTH'] is None:
        return

    user_state['THE_WORD_U_NEED_TO_GUESS'] = creating_word(user_state['WORD_LENGTH'], message)
    print(user_state['THE_WORD_U_NEED_TO_GUESS'])
    if user_state['THE_WORD_U_NEED_TO_GUESS'] is None:
        bot.send_message(user_id, "Sorry, couldn't load words. Please try again.")
        return

    user_state['CURRENT_MASK'] = creating_mask(user_state['THE_WORD_U_NEED_TO_GUESS'])
    user_state['START_TIME'] = time.time()
    bot.send_message(
        user_id,
        f"Now guess the word!\n{''.join(user_state['CURRENT_MASK'])}"
    )

    bot.register_next_step_handler(message, handling_the_guesses)

# Обработка попыток угадывания
@bot.message_handler(content_types=['text'])
def handling_the_guesses(message):
    user_id = message.from_user.id
    user_state = get_user_state(user_id)
    if message.text == "/howto":
        rules(message)
    elif message.text == "/score":
        score(message)
    elif (user_state['THE_WORD_U_NEED_TO_GUESS'] is None or
          user_state['WORD_LENGTH'] is None or
          user_state['DIFFICULTY'] is None):
        return
    else:
        guess_try = GuessTry(message, user_state['THE_WORD_U_NEED_TO_GUESS'])
        if guess_try.word is None:
            return

        user_state['CURRENT_MASK'] = word_check(
            guess_try.word.upper(),
            user_state['CURRENT_MASK'],
            user_state['THE_WORD_U_NEED_TO_GUESS'],
            message
        )

        bot.send_message(
            user_id,
            f"Current state: {''.join(user_state['CURRENT_MASK'])}"
        )

        if ''.join(user_state['CURRENT_MASK']) == user_state['THE_WORD_U_NEED_TO_GUESS']\
                or user_state['CURRENT_MASK'] == f"0 ❌ 0 ☯️ {len(user_state['THE_WORD_U_NEED_TO_GUESS'])} ✅":
            finish_game(message)

# Функция завершения игры

def finish_game(message):
    user_id = message.from_user.id
    user_state = get_user_state(user_id)
    user_state['TOTAL_TIME'] = round(time.time() - user_state['START_TIME'])
    bot.send_message(user_id, f"<b>Congratulations, {message.from_user.first_name}, you won!</b>\n" f"Your time is <b>{user_state['TOTAL_TIME']}</b> seconds.", parse_mode= "HTML")

    # Сброс состояния игры для текущего пользователя
    user_state['THE_WORD_U_NEED_TO_GUESS'] = None
    user_state['CURRENT_MASK'] = None
    user_state['WORD_LENGTH'] = None
    user_state['DIFFICULTY'] = None
    user_state['START_TIME'] = None
    user_state['TOTAL_TIME'] = None


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("YES, OF COURSE")
    btn2 = types.KeyboardButton("NO, THANK YOU")
    markup.add(btn1, btn2)

    bot.send_message(
        user_id,
        "Do you want to play again?",
        reply_markup=markup
    )
    bot.register_next_step_handler(message, play_again_handler)

# Функция с предложением поиграть еще раз

def play_again_handler(message):
    user_id = message.from_user.id
    # user_state = get_user_state(user_id)

    if message.text.upper() == "YES, OF COURSE":
        welcome_message(message)  # Запускаем игру заново
    elif message.text.upper() == "NO, THANK YOU":
        bot.send_message(
            user_id,
            f"Thank you for playing {message.from_user.first_name}\n"
            "Type '/start' to play again when you're ready."
        )
    elif message.text == "/howto":
        rules(message)
    elif message.text == "/score":
        score(message)
    else:
        bot.send_message(
            user_id,
            "Invalid input. Please try again."
        )
        bot.register_next_step_handler(message, welcome_message)


# Обработка ошибок
@bot.message_handler(func=lambda message: True)
def handle_other_messages(message):
    user_id = message.from_user.id
    bot.send_message(
        user_id,
        "I don't understand you. Please try again."
    )

# # Демонстрация статистики
@bot.message_handler(commands=['score'])
def score(message):
    bot.send_message(message.from_user.id, "<<<Here soon is gonna be information about your statistics>>>")
    return
#     try:
#         bot.send_message(message.from_user.id, f"""
#             Here is your score board: \n
#             {get_user_stats(message.from_user.id)}\n
#             Well done, {message.from_user.first_name}!\n
#         """)
#         return get_user_state(message.from_user.id)
#     except:
#         bot.send_message(message.from_user.id, "There is no data")
#         return None

# Демонстрация правил игры

@bot.message_handler(commands=['howto'])
def rules(message):
    bot.send_message(message.from_user.id, f"""
    How to play this game?\n
    There are 3 main symbols in the game:  ❌ , ☯️ and ✅\n
    ❌ means that this letter in NOT in the word you are trying to guess. \n
    ☯️ means that this letter is in the word, but the position is wrong.\n
    Finally, ✅ means that this letter is in the word and in the right place.\n
    There are two levels: easy and hard.\n
    On easy level it shows you exactly which letters are ❌, ☯️ or ✅ \n
    Meanwhile, the hard level requires you to figure it out on your own!\n
    Good luck, {message.from_user.first_name}!\n
""")
    return get_user_state(message.from_user.id)

# Запуск бота
if __name__ == '__main__':
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        bot.stop_polling()

#
# DATABASE = 'wordle_stats.db'
# #_______________________________________
# # ФУНКЦИИ ДЛЯ РАБОТЫ С БАЗОЙ ДАННЫХ:
# #_______________________________________
#
# # Функция создания даты базы для хранения лучшего времени
# def init_db():
#     conn = sqlite3.connect('wordle_stats.db')
#     cursor = conn.cursor()
#
#     # Создаем таблицу, если она не существует
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS stats (
#                                              user_id INTEGER,
#                                              difficulty TEXT,
#                                              word_length INTEGER,
#                                              best_time REAL,
#                                              PRIMARY KEY(user_id,difficulty,word_length)
#             )
#         ''')
#     conn.commit()
#     conn.close()
#
#
# # Функция сохранения статистики
# def save_stats(user_id, difficulty, word_length, total_time):
#     conn = sqlite3.connect('wordle_stats.db')
#     cursor = conn.cursor()
#
#     # Проверяем, есть ли уже запись для этого пользователя и параметров
#     cursor.execute('''
#                    SELECT best_time
#                    FROM stats
#                    WHERE user_id = ?
#                      AND difficulty = ?
#                      AND word_length = ?
#                    ''', (user_id, difficulty, word_length))
#
#     result = cursor.fetchone()
#
#     # Если записи нет или новое время лучше, сохраняем его
#     if not result or total_time < result[0]:
#         cursor.execute('''
#             INSERT OR REPLACE INTO stats (
#                 user_id, difficulty, word_length, best_time
#             ) VALUES (?, ?, ?, ?)
#         ''', (user_id, difficulty, word_length, total_time))
#         conn.commit()
#     conn.close()
#
# # Функция получения статистики по пользователю
#
# def get_user_stats(user_id):
#     conn = sqlite3.connect('wordle_stats.db')
#     cursor = conn.cursor()
#
#     cursor.execute('''
#                    SELECT difficulty, word_length, best_time
#                    FROM stats
#                    WHERE user_id = ?
#                    ''', (user_id,))
#
#     results = cursor.fetchall()
#     conn.close()
#
#     return results