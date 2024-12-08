from collections import defaultdict
from itertools import combinations 

def main():

    with open("input.txt", "r") as file:
        lines = [ [*a.strip()] for a in file.readlines() ]

    frequencies = defaultdict(lambda: list())

    map_size = (len(lines[0]), len(lines))

    check_boundaries = lambda p: 0 <= p[0] < map_size[0] and 0 <= p[1] < map_size[1]

    for y, row in enumerate(lines):
        for x, p in enumerate(row):
            if p != '.':
                frequencies[p].append((x, y))

    sol_1 = solve_part_1(frequencies, check_boundaries)
    print(f"Answer part 1: {sol_1}")

    sol_2 = solve_part_2(lines, frequencies, check_boundaries)
    print(f"Answer part 2: {sol_2}")


def solve_part_1(frequencies: defaultdict, check_boundaries):

    antinodes = set()

    for positions in frequencies.values():
        for p1, p2 in combinations(positions, 2):
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            antinodes.add((p1[0] - dx, p1[1] - dy))
            antinodes.add((p2[0] + dx, p2[1] + dy))

    return len(list(filter(check_boundaries, antinodes)))


def solve_part_2(lines, frequencies: defaultdict, check_boundaries):
    
    antinodes = set()

    for positions in frequencies.values():
        for p1, p2 in combinations(positions, 2):
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            
            mult = 1
            while (True):
                an = (p1[0] + (mult * dx), p1[1] + (mult * dy))
                if (check_boundaries(an)):
                    antinodes.add(an)
                    mult += 1
                else:
                    break

            mult = 1
            while (True):
                an = (p2[0] - (mult * dx), p2[1] - (mult * dy))
                if (check_boundaries(an)):
                    antinodes.add(an)
                    mult += 1
                else:
                    break
    
    return len(antinodes)



if __name__ == "__main__":
    main()