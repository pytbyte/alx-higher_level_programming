#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    element_count = 0

    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end=" ")
                element_count += 1

        if x > element_count:
            raise IndexError("x exceeds the length of my_list")

    except IndexError as e:
        print("\nException:", str(e))
        return element_count

    print("\n", end="")
    return element_count
