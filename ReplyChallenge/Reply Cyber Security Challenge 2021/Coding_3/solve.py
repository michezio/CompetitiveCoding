import math
import itertools
import time as tm
from collections import namedtuple
import threading
import sys


Edge = namedtuple('Edge', 'time, energy')

cities = ['Atlantide', 'Biancavilla', 'Camelot', 'Diagon Alley', 'Eldorado',
          'Gotham', 'Hill Valley', 'Hobbiville', 'Hogsmeade', 'Metropolis',
          'Mos Eisley', 'Paperopoli', 'Roma', 'Smallville']

grid = [[None for _ in range(14)] for _ in range(14)]

best_time = float('inf')
best_energy = float('inf')
best_path = None
iterations = 0

fact_iterations = math.factorial(13)

def checkStatus():
    while (True):
        print(f"Executed {iterations} iterations, best time: {best_time}, best energy: {best_energy}.")
        
        perc = 100 * iterations / fact_iterations
        print(f"Progress: {perc:.2f}%")
        if perc == 100:
            break
        else:
            tm.sleep(5)


def computeIterations(first, path_permutator):
    global iterations, best_time, best_energy, best_path
    for path in path_permutator:
        path = [first] + list(path) + [first]
        time = 0
        energy = 0
        prev = first
        for place in path[1:]:
            edge = grid[prev][place]
            time += edge.time
            energy += edge.energy
            if energy > 58000 or (place == 4 and 135 <= time <= 650):
                break
            prev = place
        else:
            if time <= best_time:
                best_path = path
                best_time = time
                best_energy = energy
        iterations += 1



if __name__ == "__main__":
    start = tm.time()

    with open("file.txt", "r") as f:
        lines = f.read().splitlines()
        for lin in lines:
            path, costs = lin.split("=")
            c_start, c_stop = path.split("-")
            time, energy = map(int, costs.split(","))
            start = cities.index(c_start)
            stop = cities.index(c_stop)
            grid[start][stop] = Edge(time, energy)

    first = int(sys.argv[1])
    others = list(range(14))
    others.remove(first)
    worker = threading.Thread(target=computeIterations, args=(first, itertools.permutations(others)))
    worker.start()

    checkStatus()

    worker.join()

    yyy = f"{best_time}-"
    for i in best_path:
        yyy += cities[i][:2]
    yyy += f"-{best_energy}"

    print(f"*** PASSWORD: {yyy}")
    stop = tm.time() - start
    print(f"Completed {iterations} iterations in {stop:.2}s")

    with open(f"pass-{first}.txt", "w") as f:
        f.write(yyy + "\n")