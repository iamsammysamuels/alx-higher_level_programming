#!/usr/bin/python3
def element_at(my_list, idx):
    li_len = len(my_list) - 1
    if idx < 0:
        return (None)
    elif li_len < idx:
        return (None)
    else:
        return (my_list[idx]) 
