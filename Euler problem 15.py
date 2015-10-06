"""
Starting in the top left corner of a 2x2 grid,
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?

Solve with binomial coefficient.
"""
from math import factorial
import time

start_time = time.clock()

gridsize = 20

numberOfSteps = int(factorial(gridsize*2) / (factorial(gridsize)**2))

end_time = time.clock()
print("Time elapsed: ", end_time - start_time, " seconds")


print("gridsize:", gridsize, "number of steps", numberOfSteps)
