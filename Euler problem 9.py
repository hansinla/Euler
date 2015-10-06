"""
A Pythagorean triplet is a set of three natural numbers,
a < b < c,
for which,
a^2 + b2^ = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which
a + b + c = 1000.
Find the product abc.
"""


def find_sum_triplets(n):
    for c in range( n - 2, 0, -1):
        for b in range(c - 1, 0, -1):
            for a in range(0, b):
                if (a+b+c) == n:
                    if is_pyth_triplet(a, b, c):
                        print (a, b, c)
                        print (a**2, b**2, c**2)
                        print(a * b * c)

                    
def is_pyth_triplet(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

find_sum_triplets(1000)
