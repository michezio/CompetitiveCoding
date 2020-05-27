import random

tests = int(input("INSERT NUMBER OF TEST CASES: "))
rows, cols = [int(x) for x in input("INSERT ROWS AND COLS NUMBER: ").split()]
lrange, rrange = [int(x) for x in input("INSERT LEFT AND RIGHT RANGES: ").split()]


print(tests)
for _ in range(tests):
    print("{} {}".format(rows, cols))
    for y in range(rows):
        text = ""
        for x in range(cols):
            num = random.randint(lrange, rrange)
            text += "{} ".format(num)
        print(text)