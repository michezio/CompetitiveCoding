#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'slowestKey' function below.
#
# The function is expected to return a CHARACTER.
# The function accepts 2D_INTEGER_ARRAY keyTimes as parameter.
#

def slowestKey(keyTimes):
    delay = [keyTimes[x][1]-keyTimes[x-1][1] for x in range(1, len(keyTimes))]
    delay.insert(0, keyTimes[0][1])
    index = delay.index(max(delay))
    return chr(97+keyTimes[index][0]) 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    keyTimes_rows = int(input().strip())
    keyTimes_columns = int(input().strip())

    keyTimes = []

    for _ in range(keyTimes_rows):
        keyTimes.append(list(map(int, input().rstrip().split())))

    result = slowestKey(keyTimes)

    fptr.write(str(result) + '\n')

    fptr.close()
