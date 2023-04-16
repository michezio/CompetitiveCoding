# NO FAREWELL: KEEP GOOGLE COMPETITIONS ALIVE

def run(encoding, strings):
    encoding = encoding.split()
    index = lambda letter: ord(letter) - ord('A')

    encoded_str = ["".join([encoding[index(x)] for x in s]) for s in strings]
    unique_str = set(encoded_str)

    return "YES" if len(encoded_str) != len(unique_str) else "NO"


if __name__ == "__main__":

    TEST = int(input())

    for case_n in range(TEST):
        encoding = input()
        str_n = int(input())
        strings = [input() for _ in range(str_n)]

        result = run(encoding, strings)
        print(f"Case #{case_n+1}: {result}")
