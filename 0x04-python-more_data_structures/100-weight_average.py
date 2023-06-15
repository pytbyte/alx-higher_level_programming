#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    product = sum(map(lambda tpl: tpl[0] * tpl[1], my_list))
    weights = sum(map(lambda tpl: tpl[1], my_list))

    weighted_average = product / weights

    return weighted_average
