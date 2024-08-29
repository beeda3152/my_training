immutable_var=(2, 'str', [2, 3, 'pri'], True, False)
print(immutable_var)
#immutable_var[0] = 'str'
mutable_var = [3, 5, 'ris',True]
print(mutable_var)
mutable_var[1] = 6
mutable_var.append(False)
mutable_var.remove(3)
print(mutable_var)