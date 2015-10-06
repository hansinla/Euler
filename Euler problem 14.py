"""
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1
It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def get_sequence_length(n):
    seq = [i]

    while seq[-1] > 1:
        if (seq[-1] % 2 == 0):
            seq.append(seq[-1]//2)
        else:
            seq.append(seq[-1] * 3 + 1)
    # print(seq)
    return len(seq)


max_length = 0
starting_num = 0
for i in range(1000000, 1, -1):
    new_max_length = get_sequence_length(i)
    if new_max_length > max_length:
        starting_num = i
        max_length = new_max_length


print("Starting number: ", starting_num, "\nSequence length: ", max_length)
