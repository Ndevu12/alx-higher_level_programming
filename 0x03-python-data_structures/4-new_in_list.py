#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newlist = []

    newlist = mylist.copy()

    if idx < 0:
        return newlist
    elif idx > len(newlist):
        return newlist
    else:
        newlist[idx] = element
    return newlist
