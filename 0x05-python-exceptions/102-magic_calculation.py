#!/usr/bin/env/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too Far")
        except Exception:
            pass
        result += ((a + b) ** i) / i
    result += b + a

    return result
