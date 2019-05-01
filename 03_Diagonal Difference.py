
import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    data =  []
    size = len(arr[0])
    for _ in arr:
        data.extend(_)
    sum1 = sum([d for d,i in enumerate(data) if i//size==0])
    sum2 = 0
    return abs(sum1+sum2)


input_data = [[11,2,4],[4,5,6],[10,8,-12]]
print(diagonalDifference(input_data))

""" n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
print(arr)
 """