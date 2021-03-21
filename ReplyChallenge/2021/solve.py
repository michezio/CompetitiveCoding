import random

INITIAL_SIZE = 100
SELECTED_PARENTS = 3
RANDOM_PARENTS = 6
NEW_PARENTS = 10
CHILDREN_GENERATED = 10
GENERATIONS = 20
MUTATION_PROBABILITY = 0.30

class Building:
    def __init__(self, x, y, latency, speed):
        self.latency = latency
        self.speed = speed
        self.x = x
        self.y = y

    def __str__(self):
        return 'X={}, Y={}, Latency={}, Speed={}'.format(self.x, self.y, self.latency, self.speed)


class Antenna:
    def __init__(self, ran, speed):
        self.range = ran
        self.speed = speed

    def __str__(self):
        return 'speed={} capacity={}'.format(self.range, self.speed)


def randomPosition():
    return [(random.randint(0, width-1), random.randint(0, height-1)) for _ in range(antennas_n)]


def generateRandomPositions(size):
    return [[randomPosition(), None] for _ in range(size)]


def mutatePosition(pos):
    x = max(0, min(width-1, pos[0] + random.randint(-1, 1)))
    y = max(0, min(height-1, pos[1] + random.randint(-1, 1)))
    return x, y


def evolvePosition(randomPosition):
    newList = []
    for pos in randomPosition:
        if random.random() < MUTATION_PROBABILITY:
            newPos = mutatePosition(pos)
            while newPos in newList:
                newPos = mutatePosition(newPos)
            newList.append(newPos)
        else:
            newList.append(pos)
    return newList


def generateNewPositions(randomPosition, size):
    return [[evolvePosition(randomPosition), None] for _ in range(size)]


def getBestRandomPosition(randomAntennaPosList: list):
    bestIndex = 0
    bestScore = 0
    for index, randomPos in enumerate(randomAntennaPosList):
        print(f"    Evaluating position {index}... ", end="")
        allbuildings = True
        totScore = 0
        for building in buildings:
            score = getScore(building, randomPos)
            if score is None:
                allbuildings = False
            else:
                totScore += score
        if allbuildings:
            totScore += reward
        if totScore > bestScore:
            bestScore = totScore
            bestIndex = index
        print(f"Score: {totScore}")
    return bestIndex, bestScore


def evaluatePositions(randomAntennaPosList: list):
    for randomPos in [x for x in randomAntennaPosList if x[1] is None]:
        allbuildings = True
        totScore = 0
        for building in buildings:
            score = getScore(building, randomPos[0])
            if score is None:
                allbuildings = False
            else:
                totScore += score
        if allbuildings:
            totScore += reward
        randomPos[1] = totScore
    randomAntennaPosList.sort(key=lambda x: -x[1])
    return randomAntennaPosList


def getScore(building: Building, randomPositions: list):
    bestScore = None
    for index, pos in enumerate(randomPositions):
        dist = abs(building.x - pos[0]) + abs(building.y - pos[1]) # Manhattan distance
        if dist <= antennas[index].range:
            score = calcScore(building, antennas[index], dist)
            bestScore = score if bestScore is None else max(bestScore, score)
    return bestScore


def calcScore(building, antenna, dist):
    return building.speed * antenna.speed - building.latency * dist


def readInput(input_lines):
    global allbuildings
    global width
    global height
    global antennas_n
    global antennas
    global buildings_n
    global buildings
    global reward

    width, height = map(int, input_lines.pop(0).split())
    buildings_n, antennas_n, reward = map(int, input_lines.pop(0).split())
    buildings = []
    for line in input_lines[:buildings_n]:
        tokens = list(map(int, line.split()))
        buildings.append(Building(*tokens))

    antennas = []
    for line in input_lines[buildings_n:]:
        tokens = list(map(int, line.split()))
        antennas.append(Antenna(*tokens))


def compute(input_lines):
    """
    Compute function, takes input_lines and elaborates a solution
    producing output_lines to return to the main function which
    dumps them in the output file. Here the algorithm takes place.
    """

    readInput(input_lines)

    print("  Generating initial random positions...")
    pool = generateRandomPositions(INITIAL_SIZE)
    # index, score = getBestRandomPosition(pool)
    print("    Evaluating positions in pool... ")
    sortedPool = evaluatePositions(pool)
    topBest = sortedPool[0]

    for i in range(GENERATIONS):
        print(f"Generation {i}")
        selectedPool = random.sample(sortedPool[SELECTED_PARENTS:len(sortedPool)//2], RANDOM_PARENTS//2)
        selectedPool.extend(random.sample(sortedPool[SELECTED_PARENTS:], RANDOM_PARENTS-(RANDOM_PARENTS//2)))
        selectedPool.extend(sortedPool[:SELECTED_PARENTS])
        pool = generateRandomPositions(NEW_PARENTS)
        pool.extend(selectedPool)
        print("  Evolving positions...")
        for origin in selectedPool:
            pool.extend(generateNewPositions(origin[0], CHILDREN_GENERATED))
        #index, score = getBestRandomPosition(pool)
        print("    Evaluating positions in pool... ")
        sortedPool = evaluatePositions(pool)
        print(" Best scores found:", *[x[1] for x in sortedPool[:3]])
        topBest = sortedPool[0]

    print(f"BEST SOLUTION FOUND WITH SCORE: {topBest[1]}")
    output_lines = []
    output_lines.append(str(len(topBest[0])))
    for index, pos in enumerate(topBest[0]):
        output_lines.append(f"{index} {pos[0]} {pos[1]}")
    return output_lines, topBest[1]




##############################################################################

def main():
    """
    Main function called when launching the script.
    It takes the input file path as command line argument,
    converts this file into a list of strings (one for each line)
    and passes this list to the compute() function,
    which generates another list of strings.
    Then it dumps those strings into the output file.
    The output file will have '-out' after the name and placed in
    the same path as the input file.
    """
    import os
    import sys
    import time

    assert len(sys.argv) > 1, "Input file path is required"

    input_path = sys.argv[1]
    assert os.path.exists(input_path), "File not found"


    print("RUNNING...")
    start_time = time.perf_counter()

    with open(input_path, "r") as input_file:
        input_lines = [x.strip() for x in input_file.readlines()]

    output_lines, score = compute(input_lines)

    output_path = f"{input_path[:-4]}-out-{score}.txt"
    
    with open(output_path, "w") as output_file:
        output_file.write("\n".join(output_lines))

    elapsed_time = time.perf_counter() - start_time
    print(f"COMPLETED IN {elapsed_time:0.4f}s")


if __name__ == "__main__":
    main()
