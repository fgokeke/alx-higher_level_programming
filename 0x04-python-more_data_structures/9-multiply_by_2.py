#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    list_of_keys = list(new_dict.keys())
    for idx in list_of_keys:
        new_dict[idx] *= 2
    return (new_dict)
