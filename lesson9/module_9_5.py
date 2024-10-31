class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')
        self.step = step
        self.pointer = start
        if self.step > 0 and self.start >= self.stop:
            raise StepValueError('Несоответствие "старт" и "стоп"')

    def __iter__(self):
        #self.pointer = self.start
        return self

    def __next__(self):
        i = self.pointer
        if self.step > 0:
            if self.pointer > self.stop:
                raise StopIteration
        else:
            if self.pointer < self.stop:
                raise StopIteration
        self.pointer += self.step
        return i
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter6 = Iterator(10, -3, -2)


for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()

try:
    iter5 = Iterator(10, 1)
    for i in iter5:
        print(i, end=' ')
except StepValueError:
    print(('Несоответствие "старт" и "стоп"'))

for i in iter6:
    print(i, end=' ')
print()