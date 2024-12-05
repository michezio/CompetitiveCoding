from functools import cmp_to_key

def main():

    with open("input.txt", "r") as file:
        lines = [ a.strip() for a in file.readlines() ]

    rules = set( tuple( int(b) for b in a.split("|") ) for a in lines if len(a) == 5 )
    updates = [ [ int(b) for b in a.split(",") ] for a in lines if len(a) > 5 ]

    rule_comparator = cmp_to_key(lambda a, b: -1 if (a, b) in rules else +1)

    sol_1 = 0
    sol_2 = 0

    for update in updates:
        sorted_update = sorted(update, key=rule_comparator)
        mid = sorted_update[len(sorted_update) // 2]
        if update == sorted_update:
            sol_1 += mid
        else:
            sol_2 += mid

    print(f"Answer part 1: {sol_1}")
    print(f"Answer part 2: {sol_2}")


if __name__ == "__main__":
    main()