"""
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares
of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares
of the first one hundred natural numbers and the square of the sum.
"""

def sum_squared(n):
    alist = range(0,n+1)
    return sum(alist)**2

def squared_sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i ** 2
    return sum

sum1 = sum_squared(100)
sum2 = squared_sum(100)
print(sum1, sum2, sum1 - sum2)
