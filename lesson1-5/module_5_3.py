class House:
    def __init__(self, name, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors
        if not isinstance(self.number_of_floors, int):
            raise TypeError("Кол-во этажей - целое число.")
    def prov1(self, other):
        if not (isinstance(self, House) and isinstance(other, House)):
            raise TypeError("Должны принадлежеть классу House")
    def prov2(self, value):
        if not (isinstance(self, House) and isinstance(value, int)):
            raise TypeError("1-й оперант должен принадлежать классу House, 2-й целое цисло")
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей {self.number_of_floors}"
    def __eq__(self, other):
        House.prov1(self,other)
        return self.number_of_floors == other.number_of_floors
    def __le__(self, other):
        House.prov1(self,other)
        return self.number_of_floors <= other.number_of_floors
    def __lt__(self, other):
        House.prov1(self, other)
        return self.number_of_floors < other.number_of_floors
    def __gt__(self, other):
        House.prov1(self, other)
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        House.prov1(self, other)
        return self.number_of_floors >= other.number_of_floors
    def __radd__(self, value):
        House.prov2(self, value)
        return  House(self.name, self.number_of_floors + value)
    def __iadd__(self, value):
        House.prov2(self, value)
        self.number_of_floors += value
        return self #House(self.name, self.number_of_floors)
    def __add__(self, value):
        House.prov2(self, value)
        return House(self.name,  self.number_of_floors + value)
    def __ne__(self, other):
        House.prov1(self, other)
        return self.number_of_floors != other.number_of_floors

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)
print(h1 == h2)
h1 = h1 + 10
print(h1)
print(h1 == h2)
h1 +=10
print(h1)
h2 = 10 + h2
print(h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)