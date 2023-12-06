#!/usr/bin/python3
def best_score(a_dictionary):
    maxi = 0
    result = 0
    if a_dictionary:
        for k, value in a_dictionary.items():
            if value > maxi:
                result = k
                maxi = value
        return result
    else:
        return None
