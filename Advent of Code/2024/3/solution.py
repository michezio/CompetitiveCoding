import re

def main():

    with open("input.txt", "r") as file:
        lines = [ a.strip() for a in file.readlines() ]

    sol_1 = solve_part_1(lines)
    print(f"Answer part 1: {sol_1}")

    sol_2 = solve_part_2(lines)
    print(f"Answer part 2: {sol_2}")


def solve_part_1(lines):
    cumul = 0

    for line in lines:
        mults = re.findall("mul\(\d+,\d+\)", line)
        for mult in mults:
            a, b = map(int, mult[4:-1].split(","))
            cumul += a * b

    return cumul


def solve_part_2(lines):
    cumul = 0
        
    enabled = True
    for line in lines:
        ops = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", line)
        for op in ops:
            if op == "do()":
                enabled = True
            elif op == "don't()":
                enabled = False
            elif enabled: 
                a, b = map(int, op[4:-1].split(","))
                cumul += a * b

    return cumul


if __name__ == "__main__":
    main()