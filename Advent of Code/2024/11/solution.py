from collections import defaultdict

def main():

    with open("input.txt", "r") as file:
        stones = [ int(x) for x in file.readlines()[0].strip().split() ]

    sol_1 = solve_part_1(stones)
    print(f"Answer part 1: {sol_1}")

    sol_2 = solve_part_2(stones)
    print(f"Answer part 2: {sol_2}")


def change_stone(s) -> list[int]:
    # 0 -> 1
    if s == 0:
        return 1
    # even digits -> split in half
    if len(ss := str(s)) % 2 == 0:
        a = int(ss[:len(ss)//2])
        b = int(ss[len(ss)//2:])
        return [a, b]
    # other cases: s -> s * 2024    
    return s * 2024


def solve_part_1(stones):

    # very dirty solution, good for part 1 but scales very poorly

    stones = stones.copy()

    def expand_list(stones):
        length = 0
        for i, s in enumerate(stones):
            if isinstance(s, list):
                length += expand_list(s)
            else:
                stones[i] = change_stone(s) 
                length += 2 if isinstance(stones[i], list) else 1
        return length

    length = 0
    for blink in range(25):
        length = expand_list(stones)
        #print(f"Blink {blink + 1}: {length}")

    return length



def solve_part_2(stones):
    
    # fast approach, we actually don't care about the position of the stones
    # but only about their current number and how many of each number there are

    stonesd = defaultdict(lambda: int(0))
    for stone in stones:
        stonesd[stone] += 1
    
    for blink in range(75):

        new_stonesd = defaultdict(lambda: int(0))

        for number, amount in stonesd.items():

            changed = change_stone(number)

            if isinstance(changed, list):
                new_stonesd[changed[0]] += amount
                new_stonesd[changed[1]] += amount
            else:
                new_stonesd[changed] += amount

        stonesd = new_stonesd

        #print(f"Blink {blink + 1}: {sum(expanded_stonesd.values())}")

    return sum(stonesd.values())





if __name__ == "__main__":
    main()