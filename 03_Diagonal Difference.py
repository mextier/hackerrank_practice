
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
    sum1 = sum([d for i,d in enumerate(data) if i==int(i//size)*(size+1)])
    sum2 = sum([d for i,d in enumerate(data) if int((i+1+i/size)%size)==0])
    return abs(sum1-sum2)

    
input_data = [[11,2,4],[4,5,6],[10,8,-12]]
print(diagonalDifference(input_data))
