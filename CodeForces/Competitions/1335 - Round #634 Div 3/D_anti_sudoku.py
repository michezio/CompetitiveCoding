# D

cases = int(input())

pos = [
    [0, 0], [1, 3], [2, 6],
    [3, 1], [4, 4], [5, 7],
    [6, 2], [7, 5], [8, 8]
]

ans = []

while(cases):
    cases -= 1

    sudoku = []
    for i in range(9):
        sudoku.append([int(x) for x in input()])

    for p in pos:
        sudoku[p[0]][p[1]] = (sudoku[p[0]][p[1]] % 9) + 1

    ans.append(sudoku)

for a in ans:
    for r in a:
        print("".join([str(x) for x in r]))
