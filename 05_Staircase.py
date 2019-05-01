#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for c in range(n):
        print('{:>{fill}}'.replace('{fill}',str(n)).format('#'*(c+1)))
            
n=4
staircase(n)