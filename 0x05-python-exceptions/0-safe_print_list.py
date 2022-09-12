#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    no_elem = 0
    for index in range(x):
        try:
            print("{:d}".format(my_list[index]), end="")
            no_elem += 1
        except ValueError:
            continue
        except IndexError:
            continue
    print()
    return no_elem
