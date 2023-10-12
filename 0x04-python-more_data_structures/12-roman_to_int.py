#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return (0)
    num = 0
    roman_nums = {"I": 1, "V": 5, "X": 10, "L": 50,
                  "C": 100, "D": 500, "M": 1000}
    special_cases = {"IV": -2, "IX": -2, "XL": -20,
                     "XC": -20, "CD": -200, "CM": -200}

    for x in roman_string:
        num += roman_nums[x]
    for case in special_cases:
        if case in roman_string:
            num += special_cases[case]
    return num
