import numpy as np
import sys

dungeon = []

with open(sys.argv[1]) as file:
    dungeon = [list(line.strip()) for line in file.readlines()]


def find_letter(letter, dungeon):
    indices = []
    
    for row, line in enumerate(dungeon):
        for col, cell in enumerate(line):
            if cell == letter:
                indices.append((row, col))

    return indices


portals = {}

for letter in "abcdefghijklmnopqrstuvwxyz":
    indices = find_letter(letter, dungeon)
    if len(indices) == 2:
        portals[indices[0]] = indices[1]
        portals[indices[1]] = indices[0]

def count_neighbors(row, col, dungeon, char='&'):
    min_row = max(0, row-1)
    max_row = min(len(dungeon)-1, row+1)
    min_col = max(0, col-1)
    max_col = min(len(dungeon[0])-1, col+1)
    neighs = np.array(dungeon)[min_row:max_row+1, min_col:max_col+1]
    return np.count_nonzero(neighs == char) - int(dungeon[row][col] == char)

def update_scenario(dungeon, portals):
    import copy
    evolved_dungeon = copy.deepcopy(dungeon)
    evolved_portals = copy.deepcopy(portals)

    for row, line in enumerate(dungeon):
        for col, cell in enumerate(line):
            if cell in 'AB':
                continue
            surrounding_blackholes = count_neighbors(row, col, dungeon, char='&')
            if cell == '&':
                if surrounding_blackholes not in (2, 3):
                    evolved_dungeon[row][col] = '.'
            else:
                if surrounding_blackholes >= 3:
                    evolved_dungeon[row][col] = '&'
                    if (row, col) in evolved_portals.keys():
                        other_portal = evolved_portals[(row, col)]
                        evolved_dungeon[other_portal[0]][other_portal[1]] = '&'
                        del evolved_portals[(row, col)]
                        del evolved_portals[other_portal]
    
    return evolved_dungeon, evolved_portals

def print_dungeon(dungeon):
    print('\n')
    for line in dungeon:
        print("".join(line))
    print('\n')

print_dungeon(dungeon)

for i in range(40):
    dungeon, portals = update_scenario(dungeon, portals)
    print_dungeon(dungeon)

