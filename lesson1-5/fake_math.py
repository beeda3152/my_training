def divide(first, second):
    if second == 0:
        return ('Ошибка. Деление на 0')
    else:
        c = first/second
        return (f'{first} деленное на {second} раврно {c}')
