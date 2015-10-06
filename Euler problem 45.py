"""
Triangle, pentagonal, and hexagonal numbers are generated
by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n-1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n-1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
"""
import time

def triangle(n):
    return n * (n + 1)//2

def pentagonal(n):
    return n * (3 * n - 1)//2

def hexagonal(n):
    return n * (2 * n - 1)

t1 = time.clock()

tri_set = set()
penta_set = set()
hexa_set = set()

"""
for n in range(286, 100000):
    tri_set.add(triangle(n))

for n in range(166, 100000):
    penta_set.add(pentagonal(n))

for n in range(144, 100000):
    hexa_set.add(hexagonal(n))


for item in tri_set:
    if item in penta_set and item in hexa_set:
        print(item)
"""


for n in range(166, 100000):
    penta_set.add(pentagonal(n))

for n in range(144, 100000):
    hexa_set.add(hexagonal(n))


for item in hexa_set:
    if item in penta_set:
        print(item)

print(time.clock() - t1)
