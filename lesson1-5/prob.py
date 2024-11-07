def is_prime(sum_three):
    def wrapper(*args):
        my_sum = sum_three(*args)
        if my_sum != 0 and my_sum % 1 == my_sum and my_sum % my_sum == 0:
            return ('Простое')
        else:
            return ('Составное')

    return wrapper


@is_prime
def sum_three(*numbers):
    return sum(numbers)


result = sum_three(2, 5, 0)
print(result)

