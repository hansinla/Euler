"""
Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a is not b,
then a and b are an amicable pair and each of a and b
are called amicable numbers.

For example, the proper divisors of 220 are
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284
are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

import time, math

def proper_div(n):
    divisors = [1]
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            if i not in divisors: divisors.append(i)
            if n//i not in divisors: divisors.append(n//i)
    return sum(divisors)


# main =============
time1 = time.clock()

amicable_nums = []
for i in range(2, 10000):
    sum_div = proper_div(i)
    if not (sum_div == i):
        loop = proper_div(sum_div)
        if loop == i:
            if i not in amicable_nums: amicable_nums.append(i)
            if i not in amicable_nums: amicable_nums.append(sum_div)

print(amicable_nums)
print("Sum: ", sum(amicable_nums))
        

print (time.clock() - time1)

