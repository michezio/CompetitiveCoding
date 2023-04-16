# NO FAREWELL: KEEP GOOGLE COMPETITIONS ALIVE

def run(meters, radius, lights):
    min_m = lambda p: max(0, p-radius)
    max_m = lambda p: min(meters, p+radius-1)
    covers = lambda m, p: m >= min_m(p) and m <= max_m(p)

    turned_on_lights = []
    position = 0
    light = 0
    covering_lights = 0
    while position < meters:
        if light < len(lights) and (covers(position, lights[light])):
            light += 1
            covering_lights += 1
        else:
            if covering_lights == 0:
                return "IMPOSSIBLE"
            turned_on_lights.append(light-1)
            position = lights[light-1] + radius
            covering_lights = 0

    if position < meters:
        return "IMPOSSIBLE"

    return str(len(turned_on_lights))

if __name__ == "__main__":

    TEST = int(input())

    for case_n in range(TEST):
        m, r, n = list(map(int, input().split()))
        lights = [int(x) for x in input().split()]

        result = run(m, r, lights)
        print(f"Case #{case_n+1}: {result}")
