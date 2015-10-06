import time

def sieve_for_primes_to(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

# main
start_time = time.clock()
print(sum(sieve_for_primes_to(2000000)))
end_time = time.clock()
print("Time elapsed: ", end_time - start_time, " seconds")
