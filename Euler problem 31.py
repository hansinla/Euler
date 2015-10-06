"""
In England the currency is made up of pound, £, and pence, p,
and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1£1 + 150p + 220p + 15p + 12p + 31p
How many different ways can £2 be made using any number of coins?
"""
"""
penny1  =   1
penny2  =   2
penny5  =   5
penny10 =  10
penny20 =  20
penny50 =  50
pound1  = 100
pound2  = 200
"""

import time

t1 = time.clock()

target = 200
coins = [1,2,5,10,20,50,100,200]
ways = [1]+[0]*target
 
for coin in coins:
  for i in range(coin, target+1):
    ways[i] += ways[i-coin]
 
print ("Answer to PE31 = ", ways[target])
print("Time:", time.clock() - t1, "seconds")
print(ways)
