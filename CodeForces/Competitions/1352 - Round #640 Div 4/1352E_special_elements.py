''' TLE, too slow solution with 1 sec limit '''


def bs(arr, n):
    if len(arr) == 0:
        return False
    c = len(arr)//2
    if arr[c] == n:
        return True
    elif c == 0:
        return False
    elif n > arr[c]:
        return bs(arr[c+1:], n)
    else:
        return bs(arr[:c], n)


def find(arr, n):
    for el in arr:
        if el == n:
            return True
        elif el > n:
            return False


TEST = int(input())
for _ in range(TEST):
    num = int(input())
    arr = [int(x) for x in input().split()]
    pref_sum = [0]
    for a in arr:
        pref_sum.append(pref_sum[-1]+a)

    special = set()
    not_special = set()

    count = 0
    for el in arr:
        if el in special:
            count += 1
            continue
        elif el in not_special:
            continue
        res = False
        for i in range(len(pref_sum)-2):
            c = pref_sum[i]
            res = find(pref_sum[i+2:], c+el)
            if res:
                count += 1
                special.add(el)
                break
        if res is False:
            not_special.add(el)

    print(count)
