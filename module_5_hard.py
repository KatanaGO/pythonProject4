import time
import hashlib

class User:
    def __init__(self, nickname, password, age):
        """
        Инициализация пользователя.
        :param nickname: Имя пользователя.
        :param password: Пароль (в виде строки, будет захэширован).
        :param age: Возраст пользователя.
        """
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    @staticmethod
    def hash_password(password):
        """
        Хэширование пароля.
        :param password: Пароль (строка).
        :return: Хэш пароля (число).
        """
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)

    def __repr__(self):
        return f"User({self.nickname}, {self.age} лет)"


class Video:
    def __init__(self, title, duration, adult_mode=False):
        """
        Инициализация видео.
        :param title: Заголовок видео.
        :param duration: Продолжительность видео (в секундах).
        :param adult_mode: Ограничение по возрасту (по умолчанию False).
        """
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __repr__(self):
        return f"Video({self.title}, {self.duration} сек, Adult: {self.adult_mode})"


class UrTube:
    def __init__(self):
        """
        Инициализация платформы UrTube.
        """
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        """
        Авторизация пользователя.
        :param nickname: Имя пользователя.
        :param password: Пароль.
        """
        hashed_password = User.hash_password(password)
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                print(f"Пользователь {nickname} успешно вошёл!")
                return
        print("Неверное имя пользователя или пароль.")

    def register(self, nickname, password, age):
        """
        Регистрация пользователя.
        :param nickname: Имя пользователя.
        :param password: Пароль.
        :param age: Возраст.
        """
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует.")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Пользователь {nickname} успешно зарегистрирован!")

    def log_out(self):
        """
        Выход из текущего аккаунта.
        """
        if self.current_user:
            print(f"Пользователь {self.current_user.nickname} вышел из системы.")
            self.current_user = None
        else:
            print("Вы не вошли в систему.")

    def add(self, *videos):
        """
        Добавление видео на платформу.
        :param videos: Видео (один или несколько объектов Video).
        """
        for video in videos:
            if all(v.title != video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, search_word):
        """
        Поиск видео по ключевому слову.
        :param search_word: Ключевое слово.
        :return: Список названий видео, содержащих ключевое слово.
        """
        search_word = search_word.lower()
        return [video.title for video in self.videos if search_word in video.title.lower()]

    def watch_video(self, title):
        """
        Просмотр видео.
        :param title: Название видео.
        """
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео.")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу.")
                    return

                for second in range(video.time_now + 1, video.duration + 1):
                    print(second, end=" ", flush=True)
                    time.sleep(1)
                print("Конец видео")
                video.time_now = 0
                return

        print("Видео не найдено.")


# Тестирование
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 10)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))  # ['Лучший язык программирования 2024 года']
print(ur.get_videos('ПРОГ'))    # ['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')  # Войдите в аккаунт, чтобы смотреть видео
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')  # Вам нет 18 лет, пожалуйста покиньте страницу
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')  # Проигрывается видео

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)  # Пользователь vasya_pupkin уже существует
print(ur.current_user)  # urban_pythonist

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')  # Видео не найдено
