#!/usr/bin/python3
number = 98
if isinstance(number, str):
    raise ValueError("Unknown format code 'd' for object of type 'str'")
else:
    print(f"{number} Battery street")
