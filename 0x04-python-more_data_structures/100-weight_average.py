#!/usr/bin/python3
def weight_average(my_list=[]):
    """Return the weighted average of all integers tuple"""

    if my_list == []:
        return 0
    summation = sum(list(map(lambda x: x[0] * x[1], my_list)))
    count = sum([x[1] for x in my_list])
    return summation / count
