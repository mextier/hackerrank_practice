#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    mins, maxs = 0, 0
    for i,score in enumerate(scores):
        if i==0:
            min_ = max_ = score
        elif score < min_:
            min_ = score
            mins += 1
        elif score > max_:
            max_ = score
            maxs += 1
    return f"{maxs} {mins}"


#scores = [10, 5, 20, 20, 4, 5 , 2, 25, 1]
scores = [3, 4, 21 ,36, 10, 28, 35, 5, 24, 42]
print(breakingRecords(scores))

