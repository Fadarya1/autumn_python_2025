# Модель учебных материалов
# todo: Создайте иерархию классов для представления различных типов учебных материалов.
#
# Требования: Базовый класс LearningMaterial:
import inspect


class LearningMaterial:
    def __init__(self, title, author, duration_minutes):
        self.title = title
        self.duration_minutes = duration_minutes
        self.author = author
    # Свойства: title, author, duration_minutes
    # Методы:
    # display_info() - выводит основную информацию
    # get_difficulty() - возвращает сложность материала (должен быть переопределен в дочерних классах)


    def display_info(self):
        print(f"Название: {self.title}\tАвтор: {self.author}\tДлительность: {self.duration_minutes}\t")

    # @classmethod
    def get_difficulty(self):
        return self.get_difficulty()

# Дочерние классы:
# VideoLesson:
# Дополнительные свойства: video_quality, subtitles_available
# Сложность: "Средняя"
class VideoLesson(LearningMaterial):
    def __init__(self, title, author, duration_minutes, video_quality, subtitles_available):
        super().__init__(title, author, duration_minutes)
        self.video_quality = video_quality
        self.subtitles_available = subtitles_available
    def get_difficulty(self):
        return "Средняя"
         # "Средняя"

# Article:
# Дополнительные свойства: word_count, reading_level
# Сложность: рассчитывается как word_count / 1000 (легкая если <1, средняя 1-3, сложная >3)
class Article(LearningMaterial):
    def __init__(self, title, author, word_count, reading_level):
        super().__init__(title, author, None)
        self.word_count = word_count
        self.reading_level = reading_level

    def get_difficulty(self):
        if self.word_count / 1000 < 1:
            return "Легкая"
        elif self.word_count / 1000 > 1 and self.word_count / 100 < 3:
            return "Средняя"
        else:
            return "Сложная"


    # Quiz:
    # Дополнительные свойства: questions_count, passing_score
    # Сложность: "Высокая" если passing_score > 80, иначе "Средняя"

class Quiz(LearningMaterial):
    def __init__(self, title, author, duration_minutes, questions_count, passing_score):
        super().__init__(title, author, duration_minutes)
        self.questions_count = questions_count
        self.questions_count = questions_count
        self.passing_score = passing_score

    def get_difficulty(self):
        if self.passing_score > 80:
            return "Высокая"
        else:
            return "Средняя"

# Этот код должен работать после реализации:
materials = [
    VideoLesson("Python ООП", "Иван Иванов", 45, "1080p", True),
    Article("Глубокое обучение", "Анна Петрова", 1200, "advanced"),
    Quiz("Проверка знаний", "Платформа", 20, 75, 10)
]

for material in materials:
    print(f"{material.title}: {material.get_difficulty()}")
    # material.display_info()
