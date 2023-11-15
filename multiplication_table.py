#!/usr/bin/env python3
"""Print the multiplication table from 1 to 10

Multiplication table of 1
1
2
3
...
_____________
multiplication table of 2
1
2
3
...
_____________
"""
__version__ = "0.1.1"
__author__ = "Juan"

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# interable (percorriveis)
numbers = list(range(1,11))


# for each number in numbers
for n1 in numbers:
    print("{:-^18}".format(f"Multiplication table {n1}"))
    print()
    for n2 in numbers:
        result = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {result}"))
    print("#" * 18)
