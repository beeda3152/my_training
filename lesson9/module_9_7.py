def is_prime(func):
    def wrapper(*args):
        ia = func(*args)
        l = True
        for i in range(2,ia//2+1):
            if ia/i == ia//i:
                print('Составное', end='  ')
                l = False
                break
        if l:
            print('Простое', end='    ')
        return ia
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)

for i in range(2,10):
    result = sum_three(i, 3, 6)
    print(result)