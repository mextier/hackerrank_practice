import os
import sys

def timeConversion(s):
    h,m,sec = s[:len(s)-2].split(':')
    if s[len(s)-2:]=='PM' and int(h)<12:
        h = int(h) + 12
    elif s[len(s)-2:]=='AM':
        if int(h) >= 12:
            h = int(h) - 12
    if int(h) > 23:
        h = 0
    return ':'.join(['{:0>2}'.format(h),m,sec])



s='06:40:03AM'
print(timeConversion(s))
