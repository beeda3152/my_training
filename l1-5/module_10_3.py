import threading
from time import sleep
import random

class Bank(threading.Thread):
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
            #threading.Thread.__init__(self)

    def deposit(self):
        for i in range(1, 6):
            for dohod in [5, 6, 8, 4, 6]:   # random.randint(50,500)
                self.balance += dohod
                print(f"Пополнение: {dohod}. Баланс: {self.balance} {i} - операция {self.lock.locked()}")
                if self.balance < 500 and not(self.lock.locked()):
                    self.lock.acquire()
                    print(self.lock.locked(), i, 3)
                if self.balance >= 500 and self.lock.locked():
                    self.lock.release()
                    print(self.lock.locked(), i, 1)
            sleep(0.001)

    def take(self):
        for i in range(1,11):
            for rashod in [5, 7, 9, 4, 6]:     #rashod = random.randint(50,500)
                print(f"Запрос на {rashod}")
                if rashod <= self.balance:
                    self.balance -= rashod
                    print(f"Снятие: {rashod}. Баланс: {self.balance}  {i} - операция {self.lock.locked()}")

                else:
                    print(f"Запрос отклонён, недостаточно средств {i} - операция {self.lock.locked()}")
                    self.lock.acquire()
                    print(self.lock.locked(), i, 2)

if __name__ == '__main__':

    bk = Bank()

    thread1 = threading.Thread(target=Bank.deposit, args=(bk,))
    thread2 = threading.Thread(target=Bank.take, args=(bk,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f'Итоговый баланс: {bk.balance}')

"""
import threading
from time import sleep


class Bank():
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

            #threading.Thread.__init__(self)

    def deposit(self):
        i=0
        for dohod in [4, 6, 8, 4, 6, 8, 4, 6]:   # random.randint(50,500)
            i += 1
            self.balance += dohod
            print(f"Пополнение: {dohod}. Баланс: {self.balance} {i} - операция {self.lock.locked()}")
            if self.balance >= 10 and self.lock.locked():
                self.lock.release()

                print(self.lock.locked(), i, 1)
            sleep(0.001)

    def take(self):
        i = 0
        for rashod in [5, 7, 9, 14, 6]:     #rashod = random.randint(50,500)
            if self.lock.locked():
                self.lock.acquire()
            i += 1
            print(f"Запрос на {rashod} {i} - операция {self.lock.locked()}")
            if rashod <= self.balance:
                self.balance -= rashod
                print(f"Снятие: {rashod}. Баланс: {self.balance}  {i} - операция {self.lock.locked()}")

            else:
                print(f"Запрос отклонён, недостаточно средств {i} - операция {self.lock.locked()}")

                self.lock.acquire()
                #print(self.lock.locked(), i, 2)
"""