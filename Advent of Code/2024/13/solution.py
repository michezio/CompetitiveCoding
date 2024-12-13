class Machine:
    def __init__(self, lines):
        self.a = int(lines[0][12:14]), int(lines[0][18:20])
        self.b = int(lines[1][12:14]), int(lines[1][18:20])
        self.prize = tuple( int(x.split("=")[1]) for x in lines[2][7:].split(", ") )

    def __repr__(self):
        return f"Button A: X+{self.a[0]}, Y+{self.a[1]}\n"\
            f"Button B: X+{self.b[0]}, Y+{self.b[1]}\n"\
            f"Prize: X={self.prize[0]}, Y={self.prize[1]}\n"

def main():

    machines = []
    with open("input.txt", "r") as file:
        lines = [ line.strip() for line in file.readlines() ]
        machine_lines = []
        for line in lines:
            if (len(line) > 0):
                machine_lines.append(line)
            else:
                machines.append(Machine(machine_lines))
                #print(machines[-1])
                machine_lines = []
        if (len(machine_lines) == 3):
            machines.append(Machine(machine_lines))
            #print(machines[-1])

    sol_1 = solve_part_1(machines)
    print(f"Answer part 1: {sol_1}")

    sol_2 = solve_part_2(machines)
    print(f"Answer part 2: {sol_2}")



def solve_part_1(machines: list[Machine]):

    cumul = 0

    for machine in machines:
        best = 101, 101, float("inf")
        for a in range(101):
            xa = a * machine.a[0]
            ya = a * machine.a[1]
            if (xa > machine.prize[0] or ya > machine.prize[1]):
                break
            for b in range(101):
                x = xa + b * machine.b[0]
                y = ya + b * machine.b[1]
                if (x > machine.prize[0] or y > machine.prize[1]):
                    break
                if (x == machine.prize[0] and y == machine.prize[1]):
                    if ((c := a * 3 + b) < best[2]):
                        best = a, b, c
        if (best[0] < 101):
            #print(best)
            cumul += best[2]

    return cumul



def solve_part_2(machines: list[Machine]):
    
    cumul = 0

    def intersect(a, b, p):
        from numpy.linalg import solve

        t1, _ = solve([[a[0], -b[0]], [a[1], -b[1]]], [p[0], p[1]])

        x = float(t1 * a[0])
        y = float(t1 * a[1])

        return x, y

    incr = 10000000000000

    for machine in machines:
        best = -1, -1, float("inf")

        sx, sy = intersect(machine.a, machine.b, machine.prize + incr)

        if (sx < machine.prize[0] + incr and sy < machine.prize[1] + incr):
            if (abs(sx - round(sx)) < 0.001):
                sx = int(round(sx))
                na = sx // machine.a[0]
                nb = (machine.prize[0] + incr - sx) // machine.b[0]
                x = na * machine.a[0] + nb * machine.b[0]
                y = na * machine.a[1] + nb * machine.b[1]
                if ((x, y) == machine.prize + incr and (c := na * 3 + nb) < best[2]):
                    best = na, nb, c

        if (best[0] > -1):
            #print(best)
            cumul += best[2]

    return cumul





if __name__ == "__main__":
    main()