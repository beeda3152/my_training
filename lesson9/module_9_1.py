def apply_all_func(int_list, *functions):
    dic_rez_func = {}
    for fun in functions:
        dic_rez_func[fun.__name__] = fun(int_list)
    return dic_rez_func

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))