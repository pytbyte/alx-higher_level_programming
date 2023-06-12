#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_mpya = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            list_mpya.append(True)
        else:
            list_mpya.append(False)
    return list_mpya
