from math import inf
def divide (first, second):
    try:
        c = first/second
    except ZeroDivisionError:
        c = inf
    return(c)
