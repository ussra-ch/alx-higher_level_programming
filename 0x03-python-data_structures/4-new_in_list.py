#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    a = my_list
    if idx < 0:
        return (a)
    elif idx > len(my_list):
        return (a)
    else :
        for i in range(len(my_list)):
            if i == idx:
                a[i] = element
                return (a)
            else:
                continue
