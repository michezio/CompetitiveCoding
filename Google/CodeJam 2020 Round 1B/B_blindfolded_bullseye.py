'''
WORKS PERFECTLY AND IS INDEED THE SUGGESTED SOLUTION
but unfortunately I made a bunch of errors while coding
and couldn't submit a working solution (had lots of RE)
'''


from random import randint as ri


def avg(p1, p2):
    return [(p1[0]+p2[0])/2, (p1[1]+p2[1])/2]


def dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def binarySearch(a, b):
    c = avg(a, b)
    if dist(a, b) < EPSILON:
        return c
    print("{} {}".format(int(round(c[0])), int(round(c[1]))))
    stat = input()
    global queries
    queries += 1
    if stat == 'HIT':
        return binarySearch(c, b)
    elif stat == 'MISS':
        return binarySearch(a, c)
    elif stat == 'WRONG':
        exit()


def getCenter(b, c, d):
    temp = c[0]**2 + c[1]**2
    bc = (b[0]**2 + b[1]**2 - temp) / 2
    cd = (temp - d[0]**2 - d[1]**2) / 2
    det = (b[0] - c[0]) * (c[1] - d[1]) - (c[0] - d[0]) * (b[1] - c[1])

    if abs(det) < 1.0e-10:
        return None

    # Center of circle
    cx = (bc*(c[1] - d[1]) - cd*(b[1] - c[1])) / det
    cy = ((b[0] - c[0]) * cd - (c[0] - d[0]) * bc) / det

    return [cx, cy]


# had wrong answer with epsilon=2 on test 3, but since I didn't
# round any intermediate result anymore epsilon=1 is more precise
EPSILON = 1
RAND_ATTEMPTS = 100
LIM = 1.0e9
queries = 0

# this was the main problem, i forgot to acquire also A and B
TEST, A, B = [int(x) for x in input().split()]
for _ in range(TEST):
    response = ""
    pcenter = [0, 0]
    queries = 0

    hits = 0
    for i in range(RAND_ATTEMPTS):
        pt = [ri(-LIM, LIM), ri(-LIM, LIM)]
        print("{} {}".format(int(pt[0]), int(pt[1])))
        status = input()
        queries += 1
        if status == 'CENTER':
            response = "CENTER"
            break
        elif status == 'HIT':
            hits += 1
            pcenter[0] += pt[0]
            pcenter[1] += pt[1]
        elif status == 'WRONG':
            exit()
    if response == "CENTER":
        continue
    pcenter = [pcenter[0] / hits, pcenter[1] / hits]
    vertex = [[-LIM, -LIM], [LIM, -LIM], [-LIM, LIM], [LIM, LIM]]
    if pcenter[0] < 0:
        if pcenter[1] < 0:
            vertex.pop(0)
        else:
            vertex.pop(2)
    else:
        if pcenter[1] < 0:
            vertex.pop(1)
        else:
            vertex.pop(3)

    c1 = binarySearch(pcenter, vertex[0])
    c2 = binarySearch(pcenter, vertex[1])
    c3 = binarySearch(pcenter, vertex[2])

    center = list(map(round, getCenter(c1, c2, c3)))

    # a better way was to spiral out from the calculated center
    # but since my solution was already very precise, only the
    # neighbour are necessary to compensate for rouding precision
    offset = [
        [-1, -1], [0, -1], [1, -1],
        [-1, 0], [0, 0], [1, 0],
        [-1, 1], [0, 1], [1, 1]
    ]

    for of in offset:
        pt = [center[0] + of[0], center[1] + of[1]]
        print("{} {}".format(int(pt[0]), int(pt[1])))
        res = input()
        if res == 'CENTER':
            response = "CENTER"
            break
        elif res == 'WRONG':
            exit()
