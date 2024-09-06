def print_params(a=1, b='строка', c =True):
    print(a, b, c)

l = [1, 2, 3]
print_params(l)
print_params(*l)
print_params("num",l)
print_params(b = 25)
print_params(c = l)
print_params(b = ['dfg', 3, False])

valies_list = [1, 'dubl', False]
values_dict = {'a': 5, 'b':'str', 'c': [2,'w']}
valies_list_2 = [2, 'prob']
print_params(valies_list)
print_params(*valies_list)
print_params(c = values_dict)
print_params(**values_dict) # Если поменять ключ на другой - программа остановится на этой строке
print_params(valies_list_2)
print_params(*valies_list_2) #Заполняются первые 2, 3-й по умолчанию

valies_list_2 = [54.32, 'Строка']
print_params(*valies_list_2, 42)
