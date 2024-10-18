import os
import time
directory = '.'
for root, dirs, files in os.walk(directory):
    for name in files:
        filepath = os.path.join(root,name)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл:{name}, Путь:{filepath}, Размер:{filesize} байт, Время изменения:{formatted_time},'
              f' Родительская дериктория:{parent_dir}')
