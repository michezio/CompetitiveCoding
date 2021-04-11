#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumGroups' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY predators as parameter.
#

class Node:
    def __init__(self, value):
        self.depth = 1
        self.value = value
        self.preys = []
        
    def addPrey(self, prey):
        self.preys.append(prey)
        prey.updateDepth(self.depth)
        
    def updateDepth(self, depth):
        self.depth = depth + 1
        for prey in self.preys:
            prey.updateDepth(self.depth)
        

def minimumGroups(predators):
    preArr = [Node(i) for i in range(len(predators))]
    for val, pred in enumerate(predators):
        if pred != -1:
            preArr[pred].addPrey(preArr[val])
    
    return max(x.depth for x in preArr)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    predators_count = int(input().strip())

    predators = []

    for _ in range(predators_count):
        predators_item = int(input().strip())
        predators.append(predators_item)

    result = minimumGroups(predators)

    fptr.write(str(result) + '\n')

    fptr.close()
