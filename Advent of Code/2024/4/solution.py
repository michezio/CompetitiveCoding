def main():

    with open("input.txt", "r") as file:
        lines = [ a.strip() for a in file.readlines() ]

    sol_1 = solve_part_1(lines)
    print(f"Answer part 1: {sol_1}")

    sol_2 = solve_part_2(lines)
    print(f"Answer part 2: {sol_2}")

def search_mas(lines: list[list[str]], x: int, y: int, dx: int, dy: int) -> bool:
    n_lines = len(lines)
    sz_line = len(lines[0])
    n_steps = 2 # len("MAS") - 1
    if not (0 <= x < sz_line) or \
       not (0 <= y < n_lines) or \
       not (0 <= x + dx * n_steps < sz_line) or \
       not (0 <= y + dy * n_steps < n_lines):
        return False
    for c in "MAS":
        if lines[y][x] != c:
            return False
        x += dx
        y += dy
    return True

def count_xmas(lines: list[list[str]], x: int, y: int) -> int:
    if lines[y][x] != "X":
        return 0
    total =  search_mas(lines, x-1, y-1, -1, -1)
    total += search_mas(lines, x-1, y,   -1,  0)
    total += search_mas(lines, x-1, y+1, -1,  1)
    total += search_mas(lines, x,   y-1,  0, -1)
    total += search_mas(lines, x,   y+1,  0,  1)
    total += search_mas(lines, x+1, y-1,  1, -1)
    total += search_mas(lines, x+1, y,    1,  0)
    total += search_mas(lines, x+1, y+1,  1,  1)
    return total

def solve_part_1(lines):
    cumul = 0

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            cumul += count_xmas(lines, x, y)

    return cumul

def find_crossed_mas(lines: list[list[str]], x: int, y: int) -> bool:
    found = search_mas(lines, x-1, y-1, 1, 1) or \
            search_mas(lines, x+1, y+1, -1, -1)
    if not found:
        return 0
    found = search_mas(lines, x+1, y-1, -1, 1) or \
            search_mas(lines, x-1, y+1, 1, -1)
    return found

def solve_part_2(lines):
    cumul = 0

    for y in range(len(lines)):
        line = lines[y]
        for x in range(len(line)):
            if line[x] == "A":
                cumul += find_crossed_mas(lines, x, y)

    return cumul


if __name__ == "__main__":
    main()