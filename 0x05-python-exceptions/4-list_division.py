#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            element_1 = my_list_1[i]
            element_2 = my_list_2[i]

            if type(element_1) not in (int, float):
                print("wrong type")
                result.append(0)
                continue

            if type(element_2) not in (int, float):
                print("wrong type")
                result.append(0)
                continue

            if element_2 == 0:
                print("division by 0")
                result.append(0)
                continue

            division_result = element_1 / element_2
            result.append(division_result)

        except IndexError:
            print("out of range")
            break

    return result
