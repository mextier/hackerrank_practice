import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    m = max(ar)
    return sum([1 for i in ar if i==m])

ar = [4,4,1,3,1,1,1,1,1]
print(birthdayCakeCandles(ar))