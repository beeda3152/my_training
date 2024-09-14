def kl(ad):
    if ad == []:
        return ad
    if isinstance(ad[0], (tuple, set)):
        ad[0] = list(ad[0])
    if isinstance(ad[0], dict):
        ad[0] = [[key, value] for key,value in ad[0].items()]
    if isinstance(ad[0], list):
        return kl(ad[0]) + kl(ad[1:])
    return ad[:1] + kl(ad[1:])

def kl1(lst):
    if lst == []:
        return 0
    if isinstance(lst[0], (tuple, set)):
        lst[0] = list(lst[0])
    if isinstance(lst[0], dict):
        lst[0] = [[key, value] for key, value in lst[0].items()]
    if isinstance(lst[0], (list)):
        return kl1(lst[0]) + kl1(lst[1:])
    if isinstance(lst[0], str):
        lst[0] = len(lst[0])
    return int(*lst[:1]) + kl1(lst[1:])
s = 0
data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}),
                  "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
a2 = kl(data_structure)
for i in a2:
    if isinstance(i, int):
        s += i
    else:
        s += len(i)
print(kl(a2))
print(f'Сумма = {s}')
print(kl1(data_structure))
