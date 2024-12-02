import bisect

class MapEntry:
    def __init__(self, value:int, length:int, mapped:int):
        self.value = value
        self.length = length
        self.mapped = mapped

class ValueRange:
    def __init__(self, value:int, length:int):
        self.value = value
        self.length = length

def gen_map(lines: list[str]) -> tuple[list[MapEntry], int]:
    the_map: list[MapEntry] = []
    for i, line in enumerate(lines):
        if len(line) == 0:
            return (the_map, i)
        mapped, value, length = map(int, line.split())
        bisect.insort(the_map, MapEntry(value, length, mapped), key = lambda x: x.value)
    return (the_map, -1)

def map_value(value: int, the_map: list[MapEntry]) -> int:
    i = bisect.bisect_right(the_map, value, key = lambda x: x.value)
    if i:
        distance = value - the_map[i-1].value
        if distance < the_map[i-1].length:
            return the_map[i-1].mapped + distance
        else:
            return value
    else:
        return value
    
#def map_value_ranged(vrange: ValueRange, the_map: list[MapEntry]) -> list[ValueRange]:
#    i = bisect.bisect_right(the_map, vrange.value, key = lambda x: x.value)
#    if i:
#        i -= 1
#        vrange_list = []
#        while (i <= len(the_map) and vrange.length > 0):
#            current_map = the_map[i]
#            distance = vrange.value - current_map.value
#            if distance < current_map.length:
#                vrange_list.append(ValueRange(vrange.value, 1))
#                new_value = current_map.value + current_map.length
#                vrange.length -= new_value - vrange.value
#                vrange.value = new_value
#            else:
#                if i == len(the_map):
#                    vrange_list.append(vrange)
#                else:
#                    i += 1
#                    next_map = the_map[i + 1]
#                    vrange.length = 
#    else:
#        return [vrange]

def main():
    with open("input.txt", "r") as file:
        lines = [ x.strip() for x in file.readlines() ]

    seeds = [int(s) for s in lines[0].split()[1:]]
    pos = 3
    seed_to_soil, i = gen_map(lines[pos:])
    pos += i + 2
    soil_to_fertilizer, i = gen_map(lines[pos:])
    pos += i + 2
    fertilizer_to_water, i = gen_map(lines[pos:])
    pos += i + 2
    water_to_light, i = gen_map(lines[pos:])
    pos += i + 2
    light_to_temperature, i = gen_map(lines[pos:])
    pos += i + 2
    temperature_to_humidity, i = gen_map(lines[pos:])
    pos += i + 2
    humidity_to_location, i = gen_map(lines[pos:])

    assert i == -1 or pos + i == len(lines), "ERROR"

    maps_list = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location]

    sol_1 = solve_part_1(seeds, maps_list)
    print(f"Answer part 1: {sol_1}")

    sol_2 = solve_part_2(seeds, maps_list)
    print(f"Answer part 2: {sol_2}")

def solve_part_1(seeds: list[int], maps: list[list[MapEntry]]) -> int:
    closest_location = 1e100
    for seed in seeds:
        value = seed
        for the_map in maps:
            value = map_value(value, the_map)

        closest_location = min(closest_location, value)
    return closest_location

def solve_part_2(seeds: list[int], maps: list[list[MapEntry]]) -> int:
    closest_location = 1e100
    for seed, length in zip(seeds[::2], seeds[1::2]):
        print(f"solving seed {seed}")
        for i in range(length):
            value = seed + i
            for m, the_map in enumerate(maps):
                value = map_value(value, the_map)

            closest_location = min(closest_location, value)
    return closest_location

if __name__ == "__main__":
    main()
