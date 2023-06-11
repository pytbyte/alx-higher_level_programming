#!/usr/bin/python3
def element_at(my_list, idx):
    target_ellement = my_list[idx]
    element_count = len(my_list)
    if target_ellement < 0:
        return (None)
    elif target_ellement > element_count:
        return None
    return target_ellement
