import re
import copy
import functools


class Robot:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def update_position(self, w, h, seconds):
        self.x = (self.x + (self.vx * seconds)) % w
        self.y = (self.y + (self.vy * seconds)) % h

    def __repr__(self):
        return f"p={self.x},{self.y} v={self.vx},{self.vy}"


def main(file, w, h):

    regex = re.compile("p=(\d+),(\d+) v=(-?\d+),(-?\d+)")

    robots = []

    with open(file, "r") as file:
        lines = [ line.strip() for line in file.readlines() ]
        for line in lines:
            m = regex.match(line)
            if not m:
                print("Something went wrong!")
                exit(1)
            robots.append(Robot(*map(int, m.groups())))
            #print(robots[-1])

    sol_1 = solve_part_1(copy.deepcopy(robots), w, h)
    print(f"Answer part 1: {sol_1}")

    sol_2 = solve_part_2(copy.deepcopy(robots), w, h)
    print(f"Answer part 2: {sol_2}")



def solve_part_1(robots: list[Robot], width, height):

    # sectors indices
    # 00 | 01
    # ---+---
    # 10 | 11
    sectors = [0] * 4

    for robot in robots:

        robot.update_position(width, height, 100)

        sector = 0

        if robot.x == (width // 2) or robot.y == (height // 2):
            continue

        if robot.x > width // 2:
            sector |= 0b01

        if robot.y > height // 2:
            sector |= 0b10

        sectors[sector] += 1
    
    return functools.reduce(lambda a,b: a*b, sectors)



def solve_part_2(robots: list[Robot], width, height):

    possible_answers = []

    def progress_bar(i, max_n):
        import sys
        p = round(20 * i / max_n)
        sys.stdout.write('\r')
        sys.stdout.write("[%-20s] %d%%" % ('=' * p, int(100 * i / max_n)))
        sys.stdout.flush()
    
    # periodicicy of width * height, after that patterns would repeat
    max_seconds = width * height

    for s in range(max_seconds):

        if (s % 256 == 0):
            progress_bar(s, max_seconds)

        # clean image
        image = [ [0] * width for _ in range(height) ]

        # update each robot and place a 1 where they are
        # using 0 and 1 for ease of computation but will print
        # using . and # for better visuals
        for robot in robots:
            robot.update_position(width, height, 1)
            image[robot.y][robot.x] = 1

        # is the christmas tree triangular like the one from AOC 2015?
        # ...........
        # .....#.....
        # ....###....
        # ...#####...
        # ..#######..
        # .#########.
        # ....###....
        # ...........
        # or is it something like this? (spoiler: it is)
        # .................
        # ........#........
        # .......###.......
        # ......#####......
        # .....#######.....
        # ......#####......
        # .....#######.....
        # ....#########....
        # ...###########...
        # ....#########....
        # ...###########...
        # ..#############..
        # .###############.
        # .......###.......
        # .......###.......
        # .................
        # maybe larger or smaller, anyways, having a shape like these we expect some 
        # amount of robots positioned contiguously on the same line, so let's find if
        # the image generated contains at least 9 (?) contiguous robots in at least 
        # one line. 9 can be changed if too many or none suitable patterns are found
        # but let's start with a value that seems reasonable, not too high not too low.
        
        for line in image:
            conts = 0

            # accumulate contiguous robots and store the max reached in conts
            def cumulate(a, b):
                nonlocal conts
                n = 0 if b == 0 else a + 1
                conts = max(conts, n)
                return n

            _ = functools.reduce(cumulate, line)

            if conts >= 9:
                possible_answers.append(s + 1)
                print(f"\nImage at second {s + 1}:")
                for line in image:
                    print(''.join(map(lambda c: ".#"[c], line)))
                print("\n")
                break

    progress_bar(max_seconds, max_seconds)
    print('\n')

    return min(possible_answers)


if __name__ == "__main__":
    main("input.txt", 101, 103)