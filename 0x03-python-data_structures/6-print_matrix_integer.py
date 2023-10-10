#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for my_list in matrix:
        end = ' '
        length = len(my_list)
        for i in range(length):
            if i == length - 1:
                end = ""
            print("{:d}".format(my_list[i]), end=end)
        print()
