"""
A unit fraction contains 1 in the numerator.
The decimal representation of the unit fractions
with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1

Where 0.1(6) means 0.166666...,
and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the
longest recurring cycle in its decimal fraction part.
"""

limit = 1000
max_cycle = []
d_max = 0

for i in range(2, 20):
    number_string  = str(1/i)
    repeat_str = ""
    for n in range(3, len(num_string)):
        




    
    match_index =  number_string .find(number_string[index], index + 1)
    if match_index == index +1:
        print("1/" + str(i), "\t=", number_string[0:2] + "(" + number_string[index] + ")")
    else:
        if (i % 2 == 0) or (i % 5 == 0):
            print("1/" + str(i), "\t=", number_string)
    
        

        
