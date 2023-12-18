
def safe_print_list(my_list=[], x=0):
    printed_elem = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            printed_elem += 1
    except IndexError:
        pass
    print("")
    return printed_elem
