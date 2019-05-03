import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    ac,oc = 0,0
    for apple in apples:
        if apple+a>=s and apple+a<=t:
            ac += 1
    for orange in oranges:
        if orange+b>=s and orange+b<=t:
            oc += 1
    print(ac)
    print(oc)


s,t = 7, 11
a,b = 5, 15
m,n = 3, 2
apples = [-2, 2, 1]
oranges = [5, -6]
countApplesAndOranges(s, t, a, b, apples, oranges)
