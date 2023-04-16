# NO FAREWELL: KEEP GOOGLE COMPETITIONS ALIVE

def run(colors):
    current = 0
    color_map = {}

    for c in colors:
        if c not in color_map.keys():
            current += 1
            color_map[c] = current
        else:
            if color_map[c] < current:
                return "IMPOSSIBLE"
            else:
                current = color_map[c]

    sorted_colors = [str(x[0]) for x in sorted(color_map.items(), key=lambda x: x[1])]
    return " ".join(sorted_colors)   
    

if __name__ == "__main__":

    TEST = int(input())

    for case_n in range(TEST):
        n = int(input())
        colors = list(map(int, input().split()))

        result = run(colors)
        print(f"Case #{case_n+1}: {result}")
