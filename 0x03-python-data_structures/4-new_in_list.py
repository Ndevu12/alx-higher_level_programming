#!/usr/bin/python3
def nen_list(my_list, idx, element):
    newlist = []

    for i in my_list:
        newlist.append(i)

    if idx < 0:
        return newlist
    elif idx > len(newlist):
        return newlist
    else:
        newlist[i] = element
    return newlist
