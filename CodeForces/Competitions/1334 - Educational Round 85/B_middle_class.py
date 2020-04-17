CASES = int(input())

answers = []

while (CASES):
    CASES -= 1

    people, thresh = [int(x) for x in input().split(" ")]
    saves = [int(x) for x in input().split(" ")]
    saves.sort()
    total = sum(saves)
    index = 0
    found = None
    while not found and index < len(saves):
        if total / (len(saves) - index) >= thresh:
            found = len(saves) - index
        else:
            total -= saves[index]
            index += 1

    found = 0 if found is None else found

    answers.append(found)

for ans in answers:
    print(ans)
