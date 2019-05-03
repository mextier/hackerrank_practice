import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    for n in range(10000):
        if x1+v1*n==x2+v2*n:
            return 'YES'
    return 'NO'

def kangaroo2(x1, v1, x2, v2):
    if v1==v2 and x1!=x2:
        return 'NO'
    n = (x2-x1)/(v1-v2) # (4-2)/(2-3)
    if int(n)==n and n>=0:
        return 'YES'
    else:
        return 'NO'

#x1,v1,x2,v2 = 0,3,4,2
#x1,v1,x2,v2 = 0,2,5,3
#x1,v1,x2,v2 = 4523,8092,9419,8076
x1,v1,x2,v2 = 2081,8403,9107,8400
print(kangaroo(x1, v1, x2, v2))
print(kangaroo2(x1, v1, x2, v2))


# x1+v1*n=x2+v2*n
# (v1-v2)*n=x2-x1
# n = (x2-x1)/(v1-v2)   #v1!=v2