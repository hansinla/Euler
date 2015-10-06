"""
A palindromic number reads the same both ways.
The largest palindrome made from the product
of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product
of two 3-digit numbers.
"""

def palin_num(digits):
    palindromes = []
    i = (10 ** digits) - 1
    j = i
    for x in range(i, 10 ** (digits - 1), -1):
        for y in range(j, 10 ** (digits - 1), -1):
            if is_palindrome(x, y):
                palindromes.append(x * y)
    return palindromes

def is_palindrome(x, y):
    s = str(x * y)
    i = 0
    j = len(s)-1

    while i < j and s[i] == s[j]:
        i+=1
        j-=1

    return j <= i
    

print(max(palin_num(3)))    # specify number of digits

