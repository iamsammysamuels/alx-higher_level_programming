#!/usr/bin/python3
if __name__ != "__main__":
    exit(1)

from calculator_1 import add, sub, mul, div
from sys import argv

argc = len(argv)
a = int(argv[1])
if argv[2] != '*':
    b = int(argv[3])
sign = argv[2]

if argc != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
if sign == "+":
    print("{:d} {:s} {:d} = {:d}".format(a, sign, b, add(a, b)))
elif sign == "-":
    print("{:d} {:s} {:d} = {:d}".format(a, sign, b, sub(a, b)))
elif sign == '*':
    print("{:d} {:s} {:d} = {:d}".format(a, sign, b, mul(a, int(argv[2]))))
elif sign == "/":
    print("{:d} {:s} {:d} = {:d}".format(a, sign, b, div(a, b)))
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
