"""
You are given the following information,
but you may prefer to do some research for yourself.

January 1, 1901 fell on a Tuesday. Jan 6 -> Sunday.

A leap year occurs on any year evenly divisible by 4,
but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month
during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
import time

t1 = time.clock()
sundays = 0


def is_sunday(date, month, year):
    f = (14 - month) // 12
    y = year - f
    m = month + 12 * f - 2
    return ((date + y + ((31 * m)//12) + (y//4) - (y//100) + (y//400)) % 7) == 0

for year in range(1901, 2001):
    for month in range(1, 13):
        if is_sunday(1, month, year): sundays += 1
        
print(sundays)
print(time.clock() - t1, "seconds")
