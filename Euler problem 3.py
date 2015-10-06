# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor
# of the number 600851475143 ?

def prime_factors(n):
    factor_list = []
    i = 2
    while n > 1:
        while n % i == 0:
            factor_list.append(i)
            n /= i
        i += 1

    return factor_list




pfs = prime_factors(600851475143)
largest_prime_factor = max(pfs) # The largest element in the prime factor list


print(pfs)
print(largest_prime_factor)
    
