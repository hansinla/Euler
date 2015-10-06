"""
The decimal number, 585 = 1001001001 (binary),
is palindromic in both bases.

Find the sum of all numbers, less than one million,
which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base,
may not include leading zeros.)
"""
def is_palindrome(s):
    """(str)->bool

    This fundction should return True if
    and only if the string s is a palindrome.

    >>> is_palindromeV3('noon')
    True
    >>> is_palindromeV3('racecar')
    True
    >>> is_palindromeV3('dented')
    False

    """
    i = 0
    j = len(s)-1

    while i < j and s[i] == s[j]:
        i+=1
        j-=1

    return j <= i

palin_sum = 0
for i in range(1, 10**6):
    if is_palindrome(str(i)) and is_palindrome(bin(i)[2:]):
        #print(i, "\t", bin(i)[2:])
        palin_sum += i
print(palin_sum)
    
