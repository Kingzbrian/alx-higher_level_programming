#!/usr/bin/python3
def uppercase(str):
    res = ''
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <=122:
            res = chr(ord(ch)-32)
        else:
            res = ch
        print("{}".format(res), end="")
