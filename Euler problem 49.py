"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
is unusual in two ways:
(i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""
import time
import itertools


def sieve_for_primes_to(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3, int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

def valid_candidate(prime):
    """int -> boolean
    returns True if prime doesn't contain excluded digits
    """
    for s in str(prime):
        if s in exclude:
            return False
    return True



# main
exclude = ["0", "2", "4", "5", "6", "8"]
"""
start_time = time.clock()
print(sum(sieve_for_primes_to(2000000)))
end_time = time.clock()
print("Time elapsed: ", end_time - start_time, " seconds")
"""

primes = sieve_for_primes_to(10000)
for prime in primes:
    if prime > 1000 and prime < 1500:
        list  = [x for x in itertools.permutations(str(prime))]
        prime_perms = []
        for a_tuple in list:
            number = ""
            for char in a_tuple:
                number += char
            if (int(number) not in prime_perms) and (number[-1] not in exclude) and (number[0] is not "0"):
                prime_perms.append(int(number))
        prime_perms.sort()
        print(prime_perms)

