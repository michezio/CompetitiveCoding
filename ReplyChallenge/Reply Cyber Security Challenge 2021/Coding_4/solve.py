from rubik.cube import *
from rubik.solve import *

import sys

debug = bool(sys.argv[2]) if len(sys.argv) == 3 else False

with open(sys.argv[1], "r") as f:
    lines = f.read().splitlines()

c = Cube("".join(lines[:9]))

if debug:
    print("Imported Cube")
    print(c, "\n")

sol = Solver(c)
sol.solve()

check = Cube("".join(lines[20:29]))

if debug:
    print("Desired output cube")
    print(check, "\n")

def position(sol, checker):
    if c.flat_str() == checker:
        return
    while(True):
        for _ in range(4):
            sol.move("X")
            if c.flat_str() == checker:
                return
            for _ in range(4):
                sol.move("Y")
                if c.flat_str() == checker:
                    return
                for _ in range(4):
                    sol.move("Z")
                    if c.flat_str() == checker:
                        return


position(sol, check.flat_str())

if debug:
    print("Final state of the cube")
    print(c, "\n")

r = Cube("".join(lines[10:19]))

if debug:
    print("Imported decypher cube")
    print(r, "\n")

nsol = Solver(r)
for m in sol.moves:
    nsol.move(m)

if debug:
    print("Decrypted cube")
    print(r, "\n")
    print("Password:")

print(r.flat_str())