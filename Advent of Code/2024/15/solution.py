import copy

def main(input_file, params = tuple()):

    warehouse = []
    movements = []

    with open(input_file, "r") as file:

        parsing_warehouse = True

        for line in (line.strip() for line in file.readlines()):

            if len(line) == 0:
                parsing_warehouse = False
                continue

            if parsing_warehouse:
                warehouse.append([*line])
            else:
                movements.extend([*line])

    print(f"Running on '{input_file}'...")
            
    sol_1 = solve_part_1((copy.deepcopy(warehouse), movements))
    print(f"Answer part 1: {sol_1}")

    sol_2 = solve_part_2((copy.deepcopy(warehouse), movements))
    print(f"Answer part 2: {sol_2}")



def find_robot(wh) -> tuple[int, int]:
    for y, row in enumerate(wh):
        for x, c in enumerate(row):
            if c == '@':
                return (x, y)
    return None
                


def push(wh, x, y, dx, dy):

    nx, ny = x + dx, y + dy

    c = wh[ny][nx]

    if (c == '#'):
        return False
    
    if (c != '.'):
        if (not push(wh, nx, ny, dx, dy)):
            return False
        
    wh[ny][nx], wh[y][x] = wh[y][x], wh[ny][nx]
    
    return True



def check_push_vert(wh, x, y, dy):
    
    ny = y + dy

    c = wh[ny][x]

    if (c == '#'):
        return False
    
    if (c in "[]"):
        if (not check_push_vert(wh, x, ny, dy)):
            return False
        if c == "[":
            if (not check_push_vert(wh, x + 1, ny, dy)): # check push the next half as well
                return False
        elif c == "]":
            if (not check_push_vert(wh, x - 1, ny, dy)): # check push the previous half as well
                return False
                   
    return True
                


def push_vert(wh, x, y, dy):
    
    nx, ny = x, y + dy

    c = wh[ny][nx]

    if (c == '#'):
        return False
    
    if (c in "[]"):
        push_vert(wh, nx, ny, dy)
        if c == "[":
            push_vert(wh, nx + 1, ny, dy) # push the next half as well
        elif c == "]":
            push_vert(wh, nx - 1, ny, dy) # push the previous half as well

    wh[ny][nx], wh[y][x] = wh[y][x], wh[ny][nx]

    return True



def solve_part_1(parsed, params = tuple()):

    wh, movs = parsed
    
    robot_pos = find_robot(wh)

    if robot_pos is None:
        print("Something went wrong!")
        exit(1)

    rx, ry = robot_pos

    cumul = 0

    for mov in movs:
        match mov:
            case '^':
                if push(wh, rx, ry, 0, -1):
                    ry -= 1
            case 'v':
                if push(wh, rx, ry, 0, +1):
                    ry += 1
            case '<':
                if push(wh, rx, ry, -1, 0):
                    rx -= 1
            case '>':
                if push(wh, rx, ry, +1, 0):
                    rx += 1

        #print(f"Move {mov}")
        #for row in wh:
        #    print(''.join(row))
        #print("\n")

    for y, row in enumerate(wh):
        for x, c in enumerate(row):
            if c == 'O':
                cumul += (100 * y + x)
    
    return cumul



def solve_part_2(parsed, params = tuple()):
    
    cumul = 0

    init_wh, movs = parsed

    nwh = []

    for row in init_wh:
        nwh.append([])
        for c in row:
            if c == '#':
                nwh[-1].extend([*"##"])
            elif c == 'O':
                nwh[-1].extend([*"[]"])
            elif c == '@':
                nwh[-1].extend([*"@."])
            elif c == '.':
                nwh[-1].extend([*".."])

    #print("Modified warehouse")
    #for row in nwh:
    #    print(''.join(row))
    #print("\n")

    robot_pos = find_robot(nwh)

    if robot_pos is None:
        print("Something went wrong!")
        exit(1)

    rx, ry = robot_pos

    for mov in movs:
        match mov:
            case '^':
                if check_push_vert(nwh, rx, ry, -1):
                    push_vert(nwh, rx, ry, -1)
                    ry -= 1
            case 'v':
                if check_push_vert(nwh, rx, ry, +1):
                    push_vert(nwh, rx, ry, +1)
                    ry += 1
            case '<':
                if push(nwh, rx, ry, -1, 0):
                    rx -= 1
            case '>':
                if push(nwh, rx, ry, +1, 0):
                    rx += 1

        #print(f"Move {mov}")
        #for row in nwh:
        #    print(''.join(row))
        #print("\n")

    for y, row in enumerate(nwh):
        for x, c in enumerate(row):
            if c == '[':
                cumul += (100 * y + x)

    return cumul





if __name__ == "__main__":
    #main("smaller_sample.txt", ())
    #main("sample.txt", ())#
    main("input.txt", ())