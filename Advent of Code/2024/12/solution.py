from copy import deepcopy

def main():

    with open("input.txt", "r") as file:
        lines = [ [*x.strip()] for x in file.readlines() ]

    sol_1 = solve_part_1(deepcopy(lines))
    print(f"Answer part 1: {sol_1}")

    sol_2 = solve_part_2(deepcopy(lines))
    print(f"Answer part 2: {sol_2}")


def flood_rec(lines, x, y, syms):
    perimeter = 0
    corners = 0
    area = 1
    lines[y][x] = syms[1]

    if (c := -1 and x == 0) or (c := lines[y][x - 1]) != syms[0]:
        if (c != syms[1]): 
            perimeter += 1
    else:
        a, p, c = flood_rec(lines, x - 1, y, syms)
        area += a
        perimeter += p
        corners += c

    if (c := -1 and x == len(lines[y]) - 1) or (c := lines[y][x + 1]) != syms[0]:
        if (c != syms[1]): 
            perimeter += 1
    else:
        a, p, c = flood_rec(lines, x + 1, y, syms)
        area += a
        perimeter += p
        corners += c

    if (c := -1 and y == 0) or (c := lines[y - 1][x]) != syms[0]:
        if (c != syms[1]): 
            perimeter += 1
    else:
        a, p, c = flood_rec(lines, x, y - 1, syms)
        area += a
        perimeter += p
        corners += c

    if (c := -1 and y == len(lines) - 1) or (c := lines[y + 1][x]) != syms[0]:
        if (c != syms[1]): 
            perimeter += 1
    else:
        a, p, c = flood_rec(lines, x, y + 1, syms)
        area += a
        perimeter += p
        corners += c

    L = x > 0 and lines[y][x-1] in syms
    R = x < len(lines[y]) - 1 and lines[y][x+1] in syms
    U = y > 0 and lines[y-1][x] in syms
    D = y < len(lines) - 1 and lines[y+1][x] in syms

    if (not(L or U) or (L and U and lines[y-1][x-1] not in syms)):
        corners += 1  
    if (not(R or U) or (R and U and lines[y-1][x+1] not in syms)):
        corners += 1
    if (not(L or D) or (L and D and lines[y+1][x-1] not in syms)):
        corners += 1
    if (not(R or D) or (R and D and lines[y+1][x+1] not in syms)):
        corners += 1

    return area, perimeter, corners


def flood(lines, x, y):
    sym = lines[y][x]
    syms = (sym, sym.lower())
    return flood_rec(lines, x, y, syms)






def solve_part_1(lines):

    cumul = 0

    #for line in lines:
    #    print("".join(line))
    
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] != lines[y][x].lower():
                area, perimeter, _ = flood(lines, x, y)
                print(f"Symbol {lines[y][x].upper()}: area {area}, perimeter {perimeter}")
                cumul += area * perimeter
                #for line in lines:
                #    print("".join(line))
                

    return cumul






def solve_part_2(lines):

    cumul = 0

    #for line in lines:
    #    print("".join(line))
    
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] != lines[y][x].lower():
                area, _, corners = flood(lines, x, y)
                print(f"Symbol {lines[y][x].upper()}: area {area}, corners {corners}")
                cumul += area * corners
                #for line in lines:
                #    print("".join(line))
                

    return cumul







if __name__ == "__main__":
    main()