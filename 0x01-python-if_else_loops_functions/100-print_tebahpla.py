#!/usr/bin/python3
for num in range(122, 96, -1):
    if num % 2 == 1:
        num = num - 32
        num = chr(num)
    else:
        num = chr(num)
    print("{}".format(num), end='')
