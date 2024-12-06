class Glob:
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    start_x = 0
    start_y = 0 
    size_x = 0
    size_y = 0


def main():

    with open("input.txt", "r") as file:
        lines = [ [*a.strip()] for a in file.readlines() ]

    Glob.size_y = len(lines)
    Glob.size_x = len(lines[0])

    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "^":
                Glob.start_x, Glob.start_y = j, i
                break
        else:
            continue
        break

    sol_1 = solve_part_1(lines)
    print(f"Answer part 1: {sol_1}")

    sol_2 = solve_part_2(lines)
    print(f"Answer part 2: {sol_2}")



def solve_part_1(lines):

    visited = set()
    angle = 0
    x, y = Glob.start_x, Glob.start_y
    dx, dy = Glob.dirs[angle]

    while True:
        visited.add((x, y))

        nx, ny = x + dx, y + dy

        if not (0 <= nx < Glob.size_x) or not (0 <= ny < Glob.size_y):
            break
        
        if lines[ny][nx] == "#":
            angle = (angle + 1) % len(Glob.dirs)
            dx, dy = Glob.dirs[angle]
        else:
            x, y = nx, ny

    return len(visited)


def solve_part_2(lines):

    def detect_loop() -> int:

        visited = set()
        angle = 0
        x, y = Glob.start_x, Glob.start_y
        dx, dy = Glob.dirs[angle]

        while True:   
            prev_visited_size = len(visited)
            visited.add((x, y, angle))
            if (prev_visited_size == len(visited)):
                return 1 # already visited with same angle, loop detected
            
            nx, ny = x + dx, y + dy

            if not (0 <= nx < Glob.size_x) or not (0 <= ny < Glob.size_y):
                break

            if lines[ny][nx] == "#":
                angle = (angle + 1) % len(Glob.dirs)
                dx, dy = Glob.dirs[angle]
            else:
                x, y = nx, ny

        return 0


    cumul = 0

    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == ".":
                lines[i][j] = "#"
                cumul += detect_loop()
                lines[i][j] = "."

    return cumul


if __name__ == "__main__":
    main()