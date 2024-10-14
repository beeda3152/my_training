import os
def exists_file(fl):
    if os.path.isfile(fl):
        print(f"Файл {fl} существует и открыт для добавления")
        file = open(fl, 'a', encoding='utf-8')
    else:
        print(f"Файл {fl} создан для записи.")
        file = open(fl, 'w', encoding='utf-8')
    return file

def custom_write(file_name,strings):
    resul = {}
    n_str = 1
    file = open(file_name, 'w', encoding='utf-8')
    for i in strings:
        n_byte = file.tell()
        file.write(f"{i}\n")
        resul[(n_str, n_byte)] = i
        n_str += 1
    file.close()
    return resul

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)