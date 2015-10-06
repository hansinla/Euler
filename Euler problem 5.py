"""
2520 is the smallest number
that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number
that is evenly divisible by all of the numbers
from 1 to 20?
"""

def smallest_mult(a):
    smallest_number = a
    while not evenly_div(smallest_number, a):
        smallest_number += a
    return smallest_number

def evenly_div(x, a):
    evenly = True
    for i in range(1, a):
        if (x % i != 0):
            return False
    return evenly

print(smallest_mult(20))
