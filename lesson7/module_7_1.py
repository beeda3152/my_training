#from pprint import pprint
import os
class Product:
    def __init__(self, name:str, weight:float, category:str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return '{}, {}, {}\n'.format(self.name, self.weight, self.category)

class Shop:
    __file_name = 'products.txt'

    def exists_file(self, fl):
        if os.path.isfile(fl):
            print("Файл существует")
            return True
        else:
            print("Файл не существует")
            return False

    def get_products(self):
        file = open(self.__file_name, 'r')
        all_prod = file.read().__str__()
        file.close()
        return all_prod

    def add(self, *products):
        if self.exists_file(self.__file_name):
            shop_prod = self.get_products()
            file = open(self.__file_name, 'a')
            for pr in products:
                if str(pr) in shop_prod:
                    print(f'Продукт {pr.name} уже есть в магазине')
                else:
                    file.write(f"{pr}")
            file.close()
        else:
            file = open(self.__file_name, 'w')
            for pr in products:
                file.write(f'{pr}')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

