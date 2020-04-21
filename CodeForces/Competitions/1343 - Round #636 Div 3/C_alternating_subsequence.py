TEST = int(input())

answers = []
for _ in range(TEST):
    n = int(input())
    arr = [int(x) for x in input().split()]

    max_sum = 0
    # find max length or alternating subs
    length = 1
    prov_max = arr[0]
    for i in range(1, len(arr)):
        if (arr[i] * arr[i-1] < 0):
            length += 1
            max_sum += prov_max
            prov_max = arr[i]
        else:
            prov_max = max(prov_max, arr[i])
    max_sum += prov_max

    answers.append(max_sum)

for ans in answers:
    print(ans)
