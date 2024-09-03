def count_calls():
    global calls
    calls += 1
def string_info(string):
    sum_= len(string)
    s1 = string.upper()
    s2 = string.lower()
    tuple_ = sum_, s1, s2
    count_calls()
    return tuple_
def is_contains(string, list_to_search):
    s1 = string.lower()
    for s2 in list_to_search:
        s2 = s2.lower()
        if s1 == s2:
            l =  True
            break
        else:
            l = False
    count_calls()
    return l
calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)