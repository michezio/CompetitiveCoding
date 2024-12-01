class Card:
    def __init__(self, line: str) -> None:
        card_id, line = line.split(": ")
        self.id = int(card_id.split()[1], 10)
        numbers = line.split(" | ")
        winning = set(map(int, numbers[0].split()))
        mine = set(map(int, numbers[1].split()))
        self.matches = len(winning & mine)
        self.copies = 1

def main():
    cards = []
    with open("input.txt", "r") as file:
        lines = [ x.strip() for x in file.readlines() ]
        cards = [ Card(line) for line in lines ]

    sol_1 = solve_part_1(cards)
    print(f"Answer part 1: {sol_1}")

    sol_2 = solve_part_2(cards)
    print(f"Answer part 2: {sol_2}")

def solve_part_1(cards: list[Card]) -> int:
    cum_sum: int = 0

    for card in cards:
        cum_sum += 2 ** (card.matches - 1) if card.matches > 0 else 0

    return cum_sum

def solve_part_2(cards: list[Card]) -> int:
    cum_sum = 0

    for n, card in enumerate(cards):
        cum_sum += card.copies
        for i in range(n + 1, n + 1 + card.matches):
            cards[i].copies += card.copies

    return cum_sum

if __name__ == "__main__":
    main()
