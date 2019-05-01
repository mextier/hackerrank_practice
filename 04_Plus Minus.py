import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos = sum([1 for i in arr if i>0])
    neg = sum([1 for i in arr if i<0])
    zer = sum([1 for i in arr if i==0])
    print(pos/len(arr))
    print(neg/len(arr))
    print(zer/len(arr))

arr = [1,1,0,-1,-1]
plusMinus(arr)
