"""
If p is the perimeter of a right angle triangle
with integral length sides, {a,b,c},
there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p < 1000,
is the number of solutions maximised?

No matter which integral values we choose for a, b and c such that a2 + b2 = c2 the perimeter will be even.

By iterating perimeters we need a method to check for integral (integer) right triangles.
We can interpret the Pythagorean theorem as a2 + b2 = (p-a-b)2 since c = p-a-b. After expanding and simplifying we have:
b = p(p – 2a) / 2(p-a) and when this equation evaluates to an integer (MOD(p(p – 2a), 2(p-a)) = 0) we have our triangle.

One last optimization. By using a+b>c and symmetry we only need to investigate values of a to p/4.
"""
import time


def pythagoras(perimeter):
    """ Integer -> list of list of integers
    computes the possible sides
    of a right triangle with perimeter n"""

    triangle_list = []
    for c in range(perimeter-1, 1, -1 ):
        for a in range(1, perimeter - c - 1):
            b = perimeter - c - a
            if  (b > 0) and ((a ** 2 + b ** 2) == (c ** 2)):
                temp_list = [a, b, c]
                triangle_list.append(temp_list)
    return triangle_list

t1 = time.clock()

t_max = 0
p_limit = 1000
 
for p in range(p_limit//2, p_limit+1, 2):
  t = 0;
  for a in range(2, p//4+1):
    if  p*(p - 2*a) % (2*(p-a)) == 0: t += 1
    if t > t_max: (t_max, p_max) = (t, p)
 
print("Answer = ", p_max)
print(len(pythagoras(p_max)))
