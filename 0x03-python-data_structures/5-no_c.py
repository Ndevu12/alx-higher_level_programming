#!/usr/bin/python3
def no_c(my_string):
    newlist = []
    i = 0
    while i < len(my_string):
        if my_string[i] == 'c' or my_string[i] == 'C':
            pass

        else:
            newlist.append(my_string[i])

        i += 1

    return ''.join(newlist)

