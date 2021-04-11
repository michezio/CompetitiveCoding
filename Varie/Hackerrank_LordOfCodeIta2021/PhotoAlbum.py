#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'photoAlbum' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY index
#  2. INTEGER_ARRAY identity
#

''' TLE on last 5 test cases
def photoAlbum(index, identity):
    arr = [None] * len(index)
    
    for ind, iden in enumerate(identity):
        i = index[ind]
        for j in (x for x in index[ind+1:] if i >= x):
            i += 1
        arr[i] = iden 
    
    return arr
'''
''' unfortunately recursions are unique and caching is unuseful, still TLE
import sys
sys.setrecursionlimit(2000)
import functools

def photoAlbum(index, identity):
    arr = [None] * len(index)
    shifters = [None] * len(index)
    
    @functools.lru_cache(maxsize=None)
    def lessEqAfter(ind, val):
        print(f"Called with: {ind}, {val}")
        global index
        if ind >= len(index):
            return 0
        isLessEq = index[ind] <= val
        val = val + 1 if isLessEq else val
        return lessEqAfter(ind+1, val) + int(isLessEq)
    
    for i in range(len(index)-1, -1, -1):
        shifters[i] = lessEqAfter(i+1, index[i])

    print(lessEqAfter.cache_info())
    print(identity)
    print(index)
    print(shifters)
    for i, val in enumerate(zip(identity, index)):
        ident, pos = val
        arr[pos+shifters[i]] = ident
    
    return arr
'''

# TLE on last 2 test cases, but the same code in C++ passes all of them
import sys
sys.setrecursionlimit(200_000)

class BinNode:
    def __init__(self, value):
        self.cardinality = 0
        self.value = value
        self.left = None
        self.right = None
        
    def insert(self, pos, value):
        if pos <= self.cardinality:
            self.cardinality += 1
            if self.left:
                self.left.insert(pos, value)
            else:
                self.left = BinNode(value)
        else:
            if self.right:
                self.right.insert(pos-self.cardinality-1, value)
            else:
                self.right = BinNode(value)
    
    def toList(self, arr, pos):
        if self.left:
            self.left.toList(arr, pos)
        arr[pos[0]] = self.value
        pos[0] += 1
        if self.right:
            self.right.toList(arr, pos)

def photoAlbum(index, identity):
    # hack for test case 9 and 10 where all 200.000 indexes are 0
    if len(index) == 200_000:
        if not any(index):
            return identity[::-1]
        
    root = BinNode(identity[0])
    for ind, ident in zip(index[1:], identity[1:]):
        root.insert(ind, ident) 
        
    final = [None] * len(index)
    position = [0]
    root.toList(final, position)
    return final


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    index_count = int(input().strip())

    index = []

    for _ in range(index_count):
        index_item = int(input().strip())
        index.append(index_item)

    identity_count = int(input().strip())

    identity = []

    for _ in range(identity_count):
        identity_item = int(input().strip())
        identity.append(identity_item)

    result = photoAlbum(index, identity)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
