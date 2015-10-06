"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719,
are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

Hint: Any one digit prime is circular by default.
In base ten, any circular prime with two or more digits can only contain the digits 1, 3, 7 and 9.
Otherwise when we rotate a 0, 2, 4, 5, 6, or 8 into the units place, the result will be divisible by 2 or 5.
"""
import time

def prime_number_list(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

def are_all_primes(prime):
    """integer -> boolean
    returns true if all rotations of the prime are also primes"""
    for item in get_rotations(prime):
        if item not in primes:
            return False
    return True

def get_rotations(a):
    """Number -> list of rotations of that number"""   
    number_str = str(a)
    rotations = []
    rotations.append(a)
    for i in range(1, len(number_str)):
        rotations.append(int(number_str[i:]+number_str[:i]))                
    return rotations

def valid_candidate(prime):
    """int -> boolean
    returns True if prime doesn't contain excluded digits
    """
    for s in str(prime):
        if s in exclude:
            return False
    return True

#===================================================

time1 = time.clock()
primes = prime_number_list(1000000)
circular_primes = []
exclude = ["0", "2", "4", "5", "6", "8"]

for prime in primes:
    if prime <10:
        circular_primes.append(prime)
    else:
        if valid_candidate(prime):
            if are_all_primes(prime):
                circular_primes.append(prime)

print(len(circular_primes))
time2 = time.clock()
print("Elapsed: ", time2-time1)
