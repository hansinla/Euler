"""
A perfect number is a number for which the sum of its
proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors
is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis
even though it is known that the greatest number that cannot be expressed
as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum
of two abundant numbers.
"""
import time, math

def proper_div(n):
    divisors = [1]
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            if i not in divisors: divisors.append(i)
            if n//i not in divisors: divisors.append(n//i)
    return sum(divisors)



# main =====================
t1 = time.clock()

my_sum = 0
abun_nums = set()
for n in range(1, 28123):
    if (proper_div(n)) > n:
        abun_nums.add(n)
    if not any( (n-a in abun_nums) for a in abun_nums ):
        my_sum += n

print(my_sum)
print(time.clock() - t1, "seconds")
