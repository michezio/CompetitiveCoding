TESTS = int(input())

for _ in range(TESTS):

    l = int(input())

    lis = [int(x) for x in input().split()]

    evens = lis[::2]
    odds = lis[1::2]

    evens_p = evens[0] % 2
    odds_p = odds[0] % 2

    if all((evens_p == e % 2 for e in evens)) and all((odds_p == o % 2 for o in odds)):
        print("YES")
    else:
        print("NO")


    