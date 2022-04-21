cases = int(input())

for _ in range(cases):
    rating = int(input())

    if rating <= 1399:
        div = 4
    elif rating <= 1599:
        div = 3
    elif rating <= 1899:
        div = 2
    else:
        div = 1

    print(f"Division {div}")