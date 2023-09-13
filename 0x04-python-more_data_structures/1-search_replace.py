#!/usr/bin/python3
def search_replace(my_list, search, replace):
    modified_list = []
    for idx in my_list:
        if idx == search:
            modified_list.append(replace)
        else:
            modified_list.append(idx)
    return (modified_list)
