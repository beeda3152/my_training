my_dict = {'Max':1991, 'Nic':1992,'Nils':1993}
print(my_dict)
print(my_dict['Nic'])
print(my_dict.get('Pit','Такого нет'))
my_dict.update({'Fil':1994, 'Mila':1995})
print(my_dict)
d_dict = my_dict.pop('Nic')
print(d_dict)
print(my_dict)
#my_set = {True, 1, 2, 3, 's, ', 'sd',  2, 3, 's, ', 'sd', True}
my_set = {1, 2, 'dfg', 1, 2,   2, 'dfg', 1}
print(my_set)
my_set.update([5, 'sTr'])
my_set.discard(2)
print(my_set)