#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    j = len(argv)
    if j != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    operators = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': div
            }
    if op not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    result = operators[op](a, b)
    print("{} {} {} = {}".format(a, op, b, result))
    exit(0)
