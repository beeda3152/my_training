import time
from multiprocessing import Pool
from threading import Thread, Event

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            str1 = file.readline()
            if not str1:
                break
            all_data.append(str1)

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    def potok1():
        print(f'Время начала работы линейным способом: {time.strftime('%H:%M:%S')}')
        start = time.time()
        for nam in filenames:
            read_info(nam)
        fin = time.time()
        print(f'Время работы линейного способа: {round((fin - start),3)}')
        ev.set()

    def potok2():
        ev.wait()
        print(f'Время начала работы многопроцессорным способом: {time.strftime('%H:%M:%S')}')
        start = time.time()
        with Pool(processes=4) as pool:
            pool.map(read_info, filenames)
        fin = time.time()
        print(f'Время работы многопроцессорного способа: {round((fin - start),3)}')


    ev = Event()
    th1 = Thread(potok1())
    th2 = Thread(potok2())
    th1.start()
    th2.start()
    


