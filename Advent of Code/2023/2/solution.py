class Game:
    class Extraction:
        def __init__(self, line: str):
            cubes = line.split(",")
            self.red = 0
            self.green = 0
            self.blue = 0
            for cube in cubes:
                num, color = cube.strip().split(" ")
                match(color):
                    case "red": self.red = int(num, 10)
                    case "green": self.green = int(num, 10)
                    case "blue": self.blue = int(num, 10)
                    case _: print(f"Invalid extraction! {color} {num}")

        def __repr__(self) -> str:
            extr = []
            if (self.red): extr.append(f"{self.red} red")
            if (self.green): extr.append(f"{self.green} green")
            if (self.blue): extr.append(f"{self.blue} blue")
            return ", ".join(extr)

    def __init__(self, line: str) -> None:
        game_id, line = line.split(": ")
        self.id = int(game_id.split(" ")[1], 10)
        self.extractions = [ Game.Extraction(x.strip()) for x in line.split(";") ]

    def __repr__(self) -> str:
        return f"Game {self.id}: {'; '.join(str(x) for x in self.extractions)}"

def main():
    games = []
    with open("input.txt", "r") as file:
        lines = [ x.strip() for x in file.readlines() ]
        games = [ Game(line) for line in lines ]

    sol_1 = solve_part_1(games)
    print(f"Answer part 1: {sol_1}")

    sol_2 = solve_part_2(games)
    print(f"Answer part 2: {sol_2}")

def solve_part_1(games: list[Game]) -> int:
    cum_sum: int = 0

    max_reds = 12
    max_greens = 13
    max_blues = 14

    for game in games:
        valid_game = True
        for extr in game.extractions:
            if (extr.red > max_reds or extr.green > max_greens or extr.blue > max_blues):
                break
        else:
            cum_sum += game.id

    return cum_sum

def solve_part_2(games: list[Game]) -> int:
    cum_sum = 0

    for game in games:
        min_red = 0
        min_green = 0
        min_blue = 0
        for ext in game.extractions:
            min_red = max(min_red, ext.red)
            min_green = max(min_green, ext.green)
            min_blue = max(min_blue, ext.blue)
        power = min_red * min_green * min_blue
        cum_sum += power

    return cum_sum

if __name__ == "__main__":
    main()
