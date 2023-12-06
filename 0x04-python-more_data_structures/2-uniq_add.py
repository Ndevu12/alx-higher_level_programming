#!/usr/bin/python3
def uniq_add(my_list=[]):
    suming = 0
    unique = list(set(my_list))
    for x in unique:
        suming += x
    return (suming)
