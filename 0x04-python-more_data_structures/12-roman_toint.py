#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    values = list(map(lambda char: roman[char], roman_string))
    result = 0
    original_value = 0

    for i in range(len(values) - 1, -1, -1):
        new_value = values[i]

        if new_value >= original_value:
            result += new_value
        else:
            result -= new_value

        original_value = new_value

    return result
