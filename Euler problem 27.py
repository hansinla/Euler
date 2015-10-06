"""
Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes
for the consecutive values n = 0 to 39. However, when
n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41,
and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² - 79n + 1601 was discovered,
which produces 80 primes for the consecutive values n = 0 to 79.
The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4
Find the product of the coefficients, a and b,
for the quadratic expression that produces the maximum number of primes
for consecutive values of n, starting with n = 0.
"""

import time

def sieve_for_primes_to(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

def f(a, b, n):
    return n * n + a * n + b

def is_prime(x):
    return x in primes
    

t1 = time.clock()
primes = sieve_for_primes_to(1000)
nmax = 0;

for a in range(-999,999,2):
  for b in primes:
    n = 1
    while is_prime(f(a, b, n)): n += 1
    if n>nmax: nmax, p = n, a*b

print(p)



print(time.clock() - t1,"seconds")
