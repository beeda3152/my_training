first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(i)-len(j) for i, j in zip(first, second) if len(i)-len(j)!=0)
second_result =(len(first[i]) == len(second[i]) for i in range(len(first)))

print(list(first_result))
print(list(second_result))

def sr(x, y):
    return len(x) == len(y)
def fr(x,y):
    return len(x) - len(y)

first_result = filter(lambda i: (i != 0), map(fr, first, second))
print(list(first_result))
second_result = map(sr, first, second)
print(list(second_result))

first_result = filter(lambda i: (i != 0), map(lambda x,y: len(x) - len(y), first, second))
print(list(first_result))
second_result =map(lambda x,y: len(x) == len(y), first, second)
print(list(second_result))
