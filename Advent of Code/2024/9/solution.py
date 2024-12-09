#import numba

def main():

    with open("input.txt", "r") as file:
        line = file.readlines()[0].strip()

    diskmap: list[int] = []

    for i, c in enumerate(line):
        if (i % 2 == 0):
            diskmap += [i//2] * int(c)
        else:
            diskmap += [-1] * int(c)

    sol_1 = solve_part_1(diskmap.copy())
    print(f"Answer part 1: {sol_1}")

    sol_2 = solve_part_2(diskmap.copy())
    print(f"Answer part 2: {sol_2}")


def solve_part_1(diskmap: list[int]):
    cumul = 0

    lpos = 0
    rpos = len(diskmap) - 1

    while (lpos < rpos):
        while (lpos < rpos and diskmap[lpos] != -1):
            lpos += 1

        while (lpos < rpos and diskmap[rpos] == -1):
            rpos -= 1

        if (lpos >= rpos):
            break

        diskmap[lpos], diskmap[rpos] = diskmap[rpos], diskmap[lpos]
    
    for i, c in enumerate(diskmap):
        if (c == -1):
            break
        cumul += i * c

    return cumul

#@numba.jit
def solve_part_2(diskmap: list[int]):
    cumul = 0

    rpos = len(diskmap) - 1

    first_empty = 0

    while (rpos > first_empty):
        
        rsize = 0
        while (rpos > 0 and diskmap[rpos] == -1):
            rpos -= 1
        
        if (rpos <= 0):
            break

        sym = diskmap[rpos]

        while (rpos > 0 and diskmap[rpos] == sym):
            rpos -= 1
            rsize += 1

        if (rpos <= 0):
            break
        
        rpos += 1
        
        lsize = 0
        lpos = first_empty
        new_first_empty = -1
        while (lpos + lsize < rpos and lsize < rsize):
            if (diskmap[lpos] == -1):
                if new_first_empty == -1:
                    new_first_empty = lpos
                lsize += 1
            else:
                lsize = 0
            lpos += 1

        if new_first_empty != -1:
            first_empty = new_first_empty
        
        lpos -= 1

        if (lpos + lsize > rpos or lsize < rsize):
            rpos -= 1
            continue

        for i in range(rsize):
            diskmap[lpos - i] = diskmap[rpos + i]
            diskmap[rpos + i] = -1

        rpos -= 1
    
    for i, c in enumerate(diskmap):
        if (c == -1):
            continue
        cumul += i * c

    return cumul


if __name__ == "__main__":
    main()