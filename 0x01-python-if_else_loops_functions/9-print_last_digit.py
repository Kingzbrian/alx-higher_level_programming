#!/usr/bin/python3
def print_last_digit(number):
    num = str(number)
    num = num[-1]
    print("{}".format(num), end="")
    return num
