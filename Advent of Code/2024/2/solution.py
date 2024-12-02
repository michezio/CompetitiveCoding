def main():

    with open("input.txt", "r") as file:
        lines = [ a.strip() for a in file.readlines() ]

    lines = [ [ int(b) for b in a.split() ] for a in lines ]

    sol_1 = solve_part_1(lines)
    print(f"Answer part 1: {sol_1}")

    sol_2 = solve_part_2(lines)
    print(f"Answer part 2: {sol_2}")


def check_line(nums):
    sort_nums = sorted(nums)
    if (nums == sort_nums or nums == sort_nums[::-1]):
        fn = lambda x: 0 < (x[1] - x[0]) <= 3
        if all(map(fn, zip(sort_nums, sort_nums[1:]))):
            return True
    return False

def solve_part_1(lines):
    cumul = 0

    for line in lines:
        if (check_line(line)):
            cumul += 1

    return cumul


def solve_part_2(lines):
    cumul = 0
    
    for line in lines:
        if (check_line(line)):
            cumul += 1
        else:
            for i in range(len(line)):
                nl = line[0:i] + line[i+1:]
                if (check_line(nl)):
                    cumul += 1
                    break
    
    return cumul


if __name__ == "__main__":
    main()