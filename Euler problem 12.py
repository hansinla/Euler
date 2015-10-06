"""
The sequence of triangle numbers is generated
by adding the natural numbers.
So the 7th triangle number would be
1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.

The first ten terms would be:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

import time
import math

def number_of_divisors(n):
    if n == 1:
        return 1
    num_div = 0
    square_root = int(math.sqrt(n))
    for divisor in range(1, square_root):
        if (n % divisor == 0):
            num_div += 2
        # Correction if the number is a perfect square
        if (square_root * square_root == n):
                      num_div -= 1
    return num_div


    
start_time = time.clock()
triangle_list = [1]
counter = 2
while number_of_divisors(triangle_list[-1]) < 500:
    new_element = triangle_list[-1] + counter
    triangle_list.append(new_element)
    counter += 1

print(triangle_list[-1], " : number of divisors: ", number_of_divisors(triangle_list[-1]))

end_time = time.clock()
print("Elapsed time: ", end_time - start_time, " seconds")

