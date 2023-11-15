#!/usr/bin/env python3
"""Prefix calculator

How to use:

[operation] [n1] [n2]

Operations:
sim -> +
sub -> -
mul -> *
div -> /

Usage:
$ prefixcalc.py sum 5 2
7

$ prefixcalc.py mul 10 5
50

$ prefixcalc.py
operation: sum
n1:5
n2:4
9
"""
__author__ = "Juan Carlos"
__version__ = "0.1.0"
__license__ = "Unlicense"

import sys
arguments = sys.argv[1:]


# TODO: Exceptions
if not arguments:
    operation = input("Operation: ")
    n1 = input("n1: ")
    n2 = input("n2: ")
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    print("Number of arguments invalid")
    print("ex: `sum 5 5`")
    sys.exit(1)

operation, *nums = arguments

valid_operation = ("sum", "sub", "mul", "div")
if operation not in valid_operation:
    print("Invalid operation")
    print(valid_operation)
    sys.exit(1)

validated_nums = []
for num in nums:
    # TODO: Loop using while + exceptions
    if not num.replace(".", "").isdigit():
        print(f"Number invalid {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

n1, n2 = validated_nums

# TODO: Use dict of functions
if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2

print(f"O resultado é {result}")
