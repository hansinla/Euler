"""
145 is a curious number,
as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal
to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums
they are not included.
"""
from math import factorial

def is_curious(n):
    sum = 0
    for digit in str(n):
        sum += factorial(int(digit))
    return sum == n

total = 0
for i in range(3, 1000000):
    if is_curious(i):
        total += i

print(total)
    
