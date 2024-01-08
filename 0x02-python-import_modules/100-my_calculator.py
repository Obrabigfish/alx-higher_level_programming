#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    lenth = len(argv)
    if lenth != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if lenth == 4:
        a = int(argv[1])
        operand = argv[2]
        b = int(argv[3])
        if operand == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif operand == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif operand == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
        elif operand == '/':
            print("{} / {} = {}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
