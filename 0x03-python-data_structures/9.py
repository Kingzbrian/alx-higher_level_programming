#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    x = my_list[0]
    for i in my_list:
        if i > x:
            x = i
    return x
    
    """
    e = sorted(my_list)
    return e[-1]
    """


