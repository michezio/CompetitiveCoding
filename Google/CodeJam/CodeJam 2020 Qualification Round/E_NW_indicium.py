'''
I know it's stupid and trying to randomly find a solution is too slow but...
In theory given the right amount of attempts possible it should work at last.
But why it doesn't? Even for a 4x4 square it can't find one with trace 6.
Why tf is that???
'''

import random
import copy

w = int(input())

MAX_ATTEMPTS = 10000


def generateLatinSquareClasses(N):
    matrix_c = []

    matrix_c.append([[a+1 for a in range(N)]])
    for x in range(N-1):
        matrix_c[0].append(list(matrix_c[0][x]))
        matrix_c[0][x+1].insert(0, matrix_c[0][x+1].pop(-1))

    for i in range(5):
        matrix_c.append(copy.deepcopy(matrix_c[0]))
    for r in range(N):
        for c in range(N):
            s = matrix_c[0][r][c]-1
            matrix_c[1][c][r] = s+1
            matrix_c[2][r][s] = c+1
            matrix_c[3][s][r] = c+1
            matrix_c[4][s][c] = r+1
            matrix_c[5][c][s] = r+1

    return matrix_c


def get_trace(matrix_c, n):
    trace = []
    for matrix in matrix_c:
        sum = 0
        for x in range(n):
            sum += matrix[x][x]
        trace.append(sum)
    return trace


def shuffle(matrix_c, N):
    for matrix in matrix_c:
        sw = random.randint(0, 2)
        a = 0
        b = 0
        while (a == b):
            a = random.randint(0, N-1)
            b = random.randint(0, N-1)
        if (sw == 0):  # SWAP ROWS
            temp = matrix[a]
            matrix[a] = matrix[b]
            matrix[b] = temp
        elif (sw == 1):  # SWAP COLUMNS
            for x in range(N):
                temp = matrix[x][a]
                matrix[x][a] = matrix[x][b]
                matrix[x][b] = temp
        elif (sw == 2):  # SWAP NUMBERS
            for r in matrix:
                a += 1
                b += 1
                r = list(
                    map(lambda x: a if x == b else (b if x == a else x), r)
                )


answer = []
while (w):
    w -= 1

    N, K = [int(x) for x in input().split(" ")]

    if K in [N+1, N**2-1]:
        answer.append(None)
        continue

    matrix_c = generateLatinSquareClasses(N)

    attempts = 0

    trace = get_trace(matrix_c, N)
    while (K not in trace and attempts < MAX_ATTEMPTS):
        attempts += 1
        shuffle(matrix_c, N)
        trace = get_trace(matrix_c, N)

    if K in trace:
        answer.append(matrix_c[trace.index(K)])
    else:
        answer.append(None)

for x in range(len(answer)):
    if answer[x] is None:
        print("Case #{}: IMPOSSIBLE".format(x+1))
    else:
        print("Case #{}: POSSIBLE".format(x+1))
        for i in answer[x]:
            print(" ".join([str(s) for s in i]))
