'''
Maze example:
ZgV(;sMXSw_EOvy/Y9Y

p[{>|#nD>Q1={48#&,.
     ^~~~~~~~~~         go down 1
V[uZiB4D\f%hQBW$"Vk
     ^     #            go right 6
0$qCvf!WGs)"k=^@^i<

fS6}3RtG*(pZ;0)x]}.

Vw(Y`=dB%|G?iCO@L>B

l#4~t2@7B81U:*7'!t9
     ^~~~~~~~~~         go down 4 (check)
BF5%4-DlkRkuKa|#vJm


Map example:
#nD>Q1={48  -> Starting position (line.find(str))
1           -> Vertical dist from start pos
6           -> Horizontal dist from start pos
4           -> Vertical dist from end pos
2@7B81U:*7  -> Ending position


Output example: h
'''

import sys

with open(sys.argv[1], 'r') as maze_file:
    maze = maze_file.read().splitlines()
    #print(maze)
    
with open(sys.argv[2], 'r') as map_file:
    maps = map_file.read().splitlines()
    #print(maps)

class Coordinate:
    def __init__(self, i, maps):
        self.pivot = maps[i]
        self.voff = int(maps[i+1])
        self.hoff = int(maps[i+2])
        self.sep = int(maps[i+3])
        self.bottom = maps[i+4]
    
    def findIn(self, maze):
        for row, line in enumerate(maze):
            val = line.find(self.pivot)
            if val >= 0:
                vindex = row + self.voff
                hindex = val + self.hoff
                result = maze[vindex][hindex]
                vindex += self.sep
                val = maze[vindex].find(self.bottom)
                return result if val >= 0 else None
        return None

coords = [Coordinate(i, maps) for i in range(0, len(maps), 6)]
coords = map(lambda x: x.findIn(maze), coords)

print("".join(c for c in coords if c is not None))