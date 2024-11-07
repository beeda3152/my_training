import threading
from time import sleep


class Knight(threading.Thread):
    def __init__(self, name:str, power:int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.day = 1

    def war(self):
        vrag = 100
        self.day = 1
        while vrag > 0:
            vrag -= self.power
            print(f"{self.name} сражается  {self.day} день(дня)..., осталось {vrag} воинов" )
            self.day += 1
            sleep(1)

    def run(self):
        print(f"{self.name}, на нас напали!")
        self.war()
        print(f"{self.name} одержал победу спустя {self.day - 1} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')