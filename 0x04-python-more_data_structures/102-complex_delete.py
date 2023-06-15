#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    target_keys = list(filter(lambda key:
                              a_dictionary[key] == value, a_dictionary.keys()))
    for key in target_keys:
        del a_dictionary[key]
    return a_dictionary
