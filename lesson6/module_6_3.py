class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'
        super().__init__()
    def run(self,dx):
        self.x_distance += dx
        return self.x_distance

class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'
    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance

class Pegasus(Horse, Eagle):

    def move(self, dx, dy):
        dx = self.run(dx)
        dy = self.fly(dy)
        return dx, dy

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)
        h = Horse()
        print(h.sound)

p1 = Pegasus()
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
p1.voice()