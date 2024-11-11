import threading
from time import sleep
import random
from queue import Queue

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        sleep(random.randint(3,5))

class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.q = Queue()

    def guest_arrival(self, *guests):
        for g in guests:
            tab_b = True
            for tab in self.tables:
                if tab.guest == None:
                    table = tab
                    tab.guest = g
                    print(f"{g.name} сел(-а) за стол номер {tab.number}")
                    g.start()
                    tab_b = False
                    break
            if tab_b:
                self.q.put(g)
                print(g.name,' в очереди')

    def discuss_guests(self):
        while not self.q.empty() or any(tab.guest is not None for tab in self.tables):
             for tab in self.tables:
                 if tab.guest and not tab.guest.is_alive():
                     print(f"{tab.guest.name} покушал(-а) и ушёл(ушла)")
                     print(f"Стол номер {tab.number} свободен")
                     tab.guest = None
                 if not self.q.empty() and tab.guest == None:
                     n_guest = self.q.get()
                     tab.guest = n_guest
                     print(f"{tab.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {tab.number}")
                     n_guest.start()










# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()


