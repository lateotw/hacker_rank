"""
https://www.hackerrank.com/challenges/calendar-module
"""

import calendar

# 08 05 2015

m, d, y = list(map(int, input().split()))
n = calendar.weekday(y, m, d)

def con_weekday(n):
    if n == 0:
        return 'MONDAY'
    elif n == 1:
        return 'TUESDAY'
    elif n == 2:
        return 'WEDNESDAY'
    elif n == 3:
        return 'THURSDAY'
    elif n == 4:
        return 'FRIDAY'
    elif n == 5:
        return 'SATURDAY'
    else:
        return 'SUNDAY'

print(con_weekday(n))
