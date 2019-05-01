#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    return f"{sum(sorted(arr)[:len(arr)-1])} {sum(sorted(arr)[1:])}"


arr = [1,3,5,7,9]
print(miniMaxSum(arr))
