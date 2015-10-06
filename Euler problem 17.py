"""
If the numbers 1 to 5 are written out in words:
one, two, three, four, five,

then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.

If all the numbers from 1 to 1000 (one thousand)
inclusive were written out in words,
how many letters would be used?

NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two)
contains 23 letters and 115 (one hundred and fifteen)
contains 20 letters.
The use of "and" when writing out numbers
is in compliance with British usage.
"""

singles = ["nul", "one", "two", "three", "four",\
           "five", "six", "seven", "eight", "nine", "ten"]
whole_tens = ["nul","ten", "twenty", "thirty", "forty", "fifty",\
              "sixty", "seventy", "eighty", "ninety"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen",\
         "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]


def count_letters(n):
    word = ""
    single = int(str(n)[-1])
    tens = int(str(n//10)[-1])
    hundreds = int(str(n//100)[-1])
    thousands = int(str(n//1000)[-1])

    if thousands > 0:
        word += singles[thousands]
        word += "thousand"
    if hundreds > 0:
        word += singles[hundreds]
        word += "hundred"
        if tens > 0 or single > 0:
            word += "and"
    if tens >= 2:
        word += whole_tens[tens]
        if single > 0:
            word += singles[single]
    elif tens == 1:
        word += teens[single]
    else:
        if single > 0:
            word += singles[single]

    return word


total_letters = 0    
for i in range(1,1001):
    total_letters += len(count_letters(i))
print(total_letters)
