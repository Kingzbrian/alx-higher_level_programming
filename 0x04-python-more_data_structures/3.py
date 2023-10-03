#!/usr/bin/python3
def common_elements(set_1, set_2):
    for i, j in zip(set_1, set_2):
        if i == j:
            return i

