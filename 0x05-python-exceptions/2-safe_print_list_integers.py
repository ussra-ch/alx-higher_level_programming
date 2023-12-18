def safe_print_list_integers(my_list=[], x=0):
    nbr_printed = 0
    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end='')
                nbr_printed += 1
    except (IndexError, TypeError):
        pass
    print("")
    return nbr_printed
