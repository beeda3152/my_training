def kluch(num):
    kl=[]
    for i in range(1, 19):
        for j in range(i, num):
            if num % (i + j) == 0:
                if j == 1:
                    continue
                kl.append([i, j])
    return kl
l = True
while l:
    nam = int(input('Введите целое число от 1 до 20 '))
    print(*kluch(nam))
    a = input('Если хотите повторить - нажмите 0. Иначе любую другую клавишу ')
    if a == '0':
        continue
    else:
        break

