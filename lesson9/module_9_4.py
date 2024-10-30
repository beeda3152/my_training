first = 'Мама мыла раму'
second = 'Рамена мало было'
rez = list(map(lambda x, y: x == y, first, second))
print(rez)

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for i in data_set:
                file.write(f"{i}\n")
        return
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
from random import choice


class MysticBall:
    def __init__(self, *args):
        self.args = args

    def __call__(self):
        word = choice(self.args)
        return word

first_ball = MysticBall('Да', 'Нет', 'Наверное','Да1', 'Нет1', 'Наверное1')
print(first_ball())
print(first_ball())
print(first_ball())