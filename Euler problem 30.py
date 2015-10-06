"""
Surprisingly there are only three numbers
that can be written as the sum of fourth powers
of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4


The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written a
the sum of fifth powers of their digits.

Note: upper limit 354300
"""

numbers = []
for i in range(2, 354300):
    sum_powers = 0
    for digit in str(i):
        sum_powers += int(digit)**5
    if i == sum_powers:
        numbers.append(i)
    
print(numbers)
print(sum(numbers))
