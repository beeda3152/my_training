import threading
from time import sleep
import random

class Bank(threading.Thread):
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
            #threading.Thread.__init__(self)

    def deposit(self):
        for i in range(100):
            dohod = random.randint(50,500)
            self.balance += dohod
            print(f"Пополнение: {dohod}. Баланс: {self.balance}")
            if self.balance < 500 and not(self.lock.locked()):
                self.lock.acquire()
                print(self.lock.locked())
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take(self):
        for i in range(100):
            rashod = random.randint(50,500)
            print(f"Запрос на {rashod}")
            if rashod <= self.balance:
                self.balance -= rashod
                print(f"Снятие: {rashod}. Баланс: {self.balance}")

            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()


if __name__ == '__main__':

    bk = Bank()

    thread1 = threading.Thread(target=Bank.deposit, args=(bk,))
    thread2 = threading.Thread(target=Bank.take, args=(bk,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f'Итоговый баланс: {bk.balance}')
