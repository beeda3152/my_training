def g():
    global l, i, j, o

    l[i][j] = ' ' + o + ' '
    for i in l:
        print(*i)

    if l[0][0] != ' * ' and l[0][0] == l[0][1] and l[0][0] == l[0][2]:
        con(1)
        return True
    if l[0][0] != ' * ' and l[0][0] == l[1][0] and l[0][0] == l[2][0]:
        con(2)
        return True
    if l[0][0] != ' * ' and l[0][0] == l[2][2] and l[0][0] == l[1][1]:
        con(3)
        return True
    if l[1][0] != ' * ' and l[1][0] == l[1][2] and l[1][0] == l[1][1]:
        con(4)
        return True
    if l[2][0] != ' * ' and l[2][0] == l[2][1] and l[2][0] == l[2][2]:
        con(5)
        return True
    if l[2][0] != ' * ' and l[2][0] == l[0][2] and l[2][0] == l[1][1]:
        con(6)
        return True
    if l[0][1] != ' * ' and l[0][1] == l[1][1] and l[0][1] == l[2][1]:
        con(7)
        return True
    if l[0][2] != ' * ' and l[0][2] == l[1][2] and l[0][2] == l[2][2]:
        con(8)
        return True
def con(j1):
    match j1:
        case 1:
            print('Выиграла линия 1,1 1,2 1,3')
        case 2:
            print('Выиграла линия 1,1 2,1 3,1')
        case 3:
            print('Выиграла линия 1,1 2,2 3,3')
        case 4:
            print('Выиграла линия 2,1 2,2 2,3')
        case 5:
            print('Выиграла линия 3,1 3,2 3,3')
        case 6:
            print('Выиграла линия 1,3 2,2 3,1')
        case 7:
            print('Выиграла линия 1,2 2,2 3,2')
        case 8:
            print('Выиграла линия 1,3 2,3 3,3')


l=[[' * ',' * ',' * '],[' * ',' * ',' * '],[' * ',' * ',' * ']]
o = 'X'
i1 = 0
while i1 <= 9:
    print(f'Ходят {o}')
    i = int(input("Введите № строки (1, 2, 3) ")) -1
    j = int(input("Введите № столбца (1, 2, 3) ")) - 1
    if l[i][j] != ' * ':
        print('Место занято. Введите другой адрес')
        continue
    i1 += 1
    if g():
        break
    if o == 'X':
        o = 'O'
    else:
        o = 'X'
