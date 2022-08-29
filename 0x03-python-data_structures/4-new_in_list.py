#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    """
        a function that replaces an element in a list at a
        specific position without modifying the original list

    """
    if type(my_list) != list:
        exit(1)
    new_string = my_list.copy()
    if idx < 0:
        return (new_string)
    elif idx > (len(new_string) - 1):
        return (new_string)
    else:
        new_string[idx] = element
        return (new_string)
