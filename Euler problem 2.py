'''Each new term in the Fibonacci sequence
is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence
whose values do not exceed four million,
find the sum of the even-valued terms.
'''

def fib(n):
    fibo_list = [0,1]
    i = 2
    while fibo_list[-1] < n:
        new_value = fibo_list[i-1] +fibo_list[i-2]
        fibo_list.append(new_value)
        i+=1
    return fibo_list[:-1]

def sum_evens(a_list):
    total = 0
    for item in a_list:
        if (item % 2 == 0):
            total += item
    return total

    

sequence = fib(10)

total = sum_evens(sequence)
print(total)


    
    
    
    
