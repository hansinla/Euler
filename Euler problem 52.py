"""
It can be seen that the number, 125874, and its double, 251748,
contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
"""
import time

def compare_digits(a, b):
    a_set = set(str(a))
    b_set = set(str(b))
    return a_set == b_set

def chain_compare(i):
    if compare_digits(i, 2*i) and compare_digits(i, 3*i)\
       and compare_digits(i, 4*i) and compare_digits(i, 5*i)\
       and compare_digits(i, 6*i):
        return True

t1 = time.clock()
for i in range(1, 1000000):
    if chain_compare(i):
        for x in range(1,7):
            print(i * x)
        break
print()
print(time.clock() - t1, "seconds")
            
