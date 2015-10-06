"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def prime_number_list(length):
    primes = []
    num = 2
    while len(primes) < length:
        is_prime = [num for i in primes if num % i == 0]
        primes  += [] if is_prime else [num]
        num += 1
        
    return primes
    


print(prime_number_list(10001)[-1])
