class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def eat (self, food):
        if food.edible is True:
            print(f'{self.name} съел {self.food}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.fed = False

class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False

class Mammal (Animal):
    pass

class Predator (Animal):
    pass

class Flower (Plant):
    pass

class Fruit (Plant):
    edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)
print(p2.name, p2.edible)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)