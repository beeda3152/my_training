import hashlib
import time

class Video:
    v= {}

    def __init__(self,film, time1, adult_mode=False):
        self.film = film
        self.time1 = time1
        self.adult_mode = adult_mode

    def add(self):
        if self.film in self.v:
            print('Film exsist')
        else:
            self.v[self.film] = {'time': self.time1, 'ad': self.adult_mode}
        return self.v

class User:
    def __init__(self, data):
        self.data = data

    def hash_password(self,pawo):
        h1 = hashlib.md5(pawo.encode())
        h = h1.hexdigest()
        return h

    def add_us(self, usna, pawo, paco):
        pawo = self.hash_password(pawo)
        self.data[usna] = {"password": pawo, 'age': paco}
        return self.data

class UrTube:
    users = {}
    us1 = User(users)
    current_user = None

    def log_in(self, nickname, password):
        if nickname in self.users:
            password = self.us1.hash_password(password)
            if password == self.users[nickname]['password']:
                self.current_user = nickname

    def register(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
        if nickname in self.users:
            print(f'Пользователь {nickname} уже существует')
        else:
            b = self.us1.add_us(self.nickname, self.password, self.age)
            self.current_user = self.nickname

    def log_out(self):
        self.current_user = None
# блок с видео
    def add(self, *args):
        for j in args:
            self.video = Video.add(j)

    def get_videos(self, str1):
        spisok = []
        str1 = str1.lower()
        for str2 in self.video:
            str3 = str2.lower()
            if str1 in str3:
                spisok.append(str2)
        return spisok

    def watch_video(self,str1):
        if str1 in self.video:
            if self.current_user != None:
                if self.users[self.current_user]['age'] < 18 and self.video[str1]['ad']:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    for i in range(self.video[str1]['time']):
                        time.sleep(1)
                        print(f'{i + 1} ', end = '')
                    print(' Конец видео')
            else:
                print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            print(f"Видео: '{str1}' - нет")


v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
ur = UrTube()
# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')