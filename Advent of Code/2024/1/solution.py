from collections import Counter


def main():

    with open("input.txt", "r") as file:
        lines = map(lambda x: x.strip(), file.readlines())

    list_1, list_2 = map(sorted, zip(*(map(int, x.split()) for x in lines)))

    sol_1 = solve_part_1(list_1, list_2)
    print(f"Answer part 1: {sol_1}")

    sol_2 = solve_part_2(list_1, list_2)
    print(f"Answer part 2: {sol_2}")


def solve_part_1(list_1, list_2):
    cumul = 0
    
    for a, b, in zip(list_1, list_2):
        dist = abs(a - b)
        cumul += dist

    return cumul


def solve_part_2(list_1, list_2):
    cumul = 0

    list_2_counter = Counter(list_2)

    for a in list_1:
        sc = a * list_2_counter[a]
        cumul += sc

    return cumul


if __name__ == "__main__":
    main()