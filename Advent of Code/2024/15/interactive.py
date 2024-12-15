import os
import time
import msvcrt
import sys
import signal

g_total_lines_printed = 0


def main(input_file, params = tuple()):

    print(f"Playing on '{input_file}'...")

    warehouse = []
    movements = []

    with open(input_file, "r") as file:

        parsing_warehouse = True
        for line in (line.strip() for line in file.readlines()):

            if len(line) == 0:
                if len(warehouse) > 0:
                    parsing_warehouse = False
                else:
                    parsing_warehouse = True
                continue
            
            if parsing_warehouse:
                warehouse.append(line)
            else:
                movements.extend([*line])


    level = '0'
    while level not in "123":
        print("Levels: [1] Easy, [2] Medium, [3] Hard")
        level = input("Select level: ")

    level = int(level)

    if level == 1:
        warehouse = transform_easy_warehouse(warehouse)
    if level == 2:
        warehouse = transform_medium_warehouse(warehouse)
    elif level == 3:
        warehouse = transform_hard_warehouse(warehouse)

    autoplay = False
    if len(movements) > 0:
        autoplay = input("Autoplay? [y/N]: ")
        autoplay = True if autoplay != '' and autoplay in "yY" else False
    
    play(warehouse, movements if autoplay else None)



def find_robot(wh) -> tuple[int, int]:
    for y, row in enumerate(wh):
        for x, c in enumerate(row):
            if c == '@':
                return (x, y)
    return None
                


def check_push_split(wh, x, y, dx, dy):
    
    nx, ny = x + dx, y + dy

    c = wh[ny][nx]

    if (c == '█'):
        return False
    
    if (c != " "):
        if (not check_push_split(wh, nx, ny, dx, dy)):
            return False
        if dy != 0: # only in Medium and Hard mode
            if c in "[╚╔":
                if (not check_push_split(wh, nx + 1, ny, 0, dy)): # check push block on the right
                    return False
            elif c in "]╝╗":
                if (not check_push_split(wh, nx - 1, ny, 0, dy)): # check push block on the left
                    return False
        if dx != 0: # only in Hard mode
            if c in "╔╗":
                if (not check_push_split(wh, nx, ny + 1, dx, 0)): # check push block below
                    return False
            elif c in "╚╝":
                if (not check_push_split(wh, nx, ny - 1, dx, 0)): # check push block above
                    return False
                
    return True
                

def push_split(wh, x, y, dx, dy):
    
    nx, ny = x + dx, y + dy

    c = wh[ny][nx]

    if (c == '█'):
        return False
    
    if (c != " "):
        push_split(wh, nx, ny, dx, dy)
        if dy != 0: # only in Medium and Hard mode
            if c in "[╚╔":
                push_split(wh, nx + 1, ny, 0, dy) # check push block on the right
            elif c in "]╝╗":
                push_split(wh, nx - 1, ny, 0, dy) # check push block on the left
        if dx != 0: # only in Hard mode
            if c in "╔╗":
                push_split(wh, nx, ny + 1, dx, 0) # check push block below
            elif c in "╚╝":
                push_split(wh, nx, ny - 1, dx, 0) # check push block above

    wh[ny][nx], wh[y][x] = wh[y][x], wh[ny][nx]

    return True


def print_warehouse(warehouse):
    global g_total_lines_printed
    #print()
    #g_total_lines_printed += 1
    for row in warehouse:
        print(''.join(row))
        g_total_lines_printed += 1
    print()
    g_total_lines_printed += 1



def transform_easy_warehouse(warehouse):

    nwh = []

    for row in warehouse:
        nrow = row.replace(".", " ")
        nrow = nrow.replace("#", "█")
        nrow = nrow.replace("O", "#")
        nwh.append([*nrow])

    return nwh


def transform_medium_warehouse(warehouse):

    nwh = []

    for row in warehouse:
        nwh.append([])
        for c in row:
            if c == '#':
                nwh[-1].extend([*"██"])
            elif c == 'O':
                nwh[-1].extend([*"[]"])
            elif c == '@':
                nwh[-1].extend([*"@ "])
            elif c == '.':
                nwh[-1].extend([*"  "])

    return nwh


def transform_hard_warehouse(warehouse):

    nwh = []

    for row in warehouse:
        nwh.append([])
        nwh.append([])
        for c in row:
            if c == '#':
                nwh[-2].extend([*"██"])
                nwh[-1].extend([*"██"])
            elif c == 'O':
                nwh[-2].extend([*"╔╗"])
                nwh[-1].extend([*"╚╝"])
            elif c == '@':
                nwh[-2].extend([*"@ "])
                nwh[-1].extend([*"  "])
            elif c == '.':
                nwh[-2].extend([*"  "])
                nwh[-1].extend([*"  "])

    return nwh


def play(warehouse, movements):

    global g_total_lines_printed
    
    robot_pos = find_robot(warehouse)

    if robot_pos is None:
        print("Something went wrong!")
        exit(1)

    rx, ry = robot_pos

    def next_move(warehouse, move, rx, ry):
        match move:
            case move if move in 'w^': # up
                if check_push_split(warehouse, rx, ry, 0, -1):
                    push_split(warehouse, rx, ry, 0, -1)
                    ry -= 1
            case move if move in 'sv': # down
                if check_push_split(warehouse, rx, ry, 0, +1):
                    push_split(warehouse, rx, ry, 0, +1)
                    ry += 1
            case move if move in 'a<': # left
                if check_push_split(warehouse, rx, ry, -1, 0):
                    push_split(warehouse, rx, ry, -1, 0)
                    rx -= 1
            case move if move in 'd>': # right
                if check_push_split(warehouse, rx, ry, +1, 0):
                    push_split(warehouse, rx, ry, +1, 0)
                    rx += 1
        return rx, ry


    os.system('cls' if os.name=='nt' else 'clear')

    if movements is not None:
        
        for move in movements:
            print("\033[F" * (g_total_lines_printed + 1))
            g_total_lines_printed = 0
            print_warehouse(warehouse)
            print("Press CTRL+C to exit.")
            g_total_lines_printed += 1
            rx, ry = next_move(warehouse, move, rx, ry)
            #time.sleep(1 / 10)

    else:

        while (True):
        
            print("\033[F" * (g_total_lines_printed + 1))
            g_total_lines_printed = 0

            print_warehouse(warehouse)

            move = '@'

            while (move not in "wasd"):
                print("Use WASD to move. Press q to exit.")
                g_total_lines_printed += 1
                ch = msvcrt.getch()

                if ch != b'\x00':
                    if ch in (b'q', b'Q'):
                        print()
                        exit(0)
                    if ch in (b"w", b"a", b"s", b"d", b"W", b"A", b"S", b"D"):
                        move = ch.decode("utf-8").lower()
                        break

                time.sleep(1 / 30)

            rx, ry = next_move(warehouse, move, rx, ry)

        



if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("\nPlease insert input file as argumemt.\n")
        exit(1)

    def signal_handler(sig, frame):
        os.system('cls' if os.name=='nt' else 'clear')
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    main(sys.argv[1], ())