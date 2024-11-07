my_dict = {'Max':1991, 'Nic':1992,'Nils':1993}
print('Dic: ', my_dict)
print('Existing value:', my_dict['Nic'])
print('Not existing value: ', my_dict.get('Pit'))
my_dict.update({'Fil':1994, 'Mila':1995})
print(my_dict)
d_dict = my_dict.pop('Nic')
print('Deleted value: ', d_dict)
print('Modified dictionary: ', my_dict)
#my_set = {True, 1, 2, 3, 's, ', 'sd',  2, 3, 's, ', 'sd', True}
my_set = {1, 2, 'dfg', 1, 2, 2, (1, 2, 3), 'dfg', 1, False, (1, 2, 3)}
print(my_set)
my_set.update([5, 'sTr', (1, 2, 3)])
my_set.discard(2)
print(my_set)