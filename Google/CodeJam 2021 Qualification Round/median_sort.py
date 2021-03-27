def solve(n, q):
    arr = []
    print("1 2 3")
    ans = int(input())
    if ans == 2:
        arr = [1,2,3]
    if ans == 1:
        arr = [2,1,3]
    if ans == 3:
        arr = [1,3,2]
    for i in range(4, n+1):
        L = 0
        R = len(arr)-1
        while L < R:
            median = (L + R) // 2
            print(f"{arr[median]} {arr[median+1]} {i}")
            ans = int(input())
            if ans == arr[median]:
                R = median
            elif ans == arr[median+1]:
                L = median + 1
            else:
                arr.insert(median+1, i)
                break
        if i != len(arr):
            if (L == 0):
                arr.insert(0, i)
            else:
                arr.append(i)
    print(*arr)
    ans = int(input())
    if ans == -1:
        exit()
        

'''
REC = 0
def solve(n, q):
    arr = list(range(1, n+1))
    medianSort(arr, 0, n-1)
    print(*arr)
    return int(input())


def medianSort(arr, L, R):
    global REC
    REC += 1
    with open("median_log.txt", "a") as log:
        log.write(f"RECURSION #{REC}: {arr}, {L}, {R}\n")
        if R-L > 1:
            median = (L + R) // 2
            print(arr[L], arr[median], arr[R])
            log.write(f"Asking index {L}, {median}, {R} -> {arr[L]} {arr[median]} {arr[R]}\n")
            new_median = int(input())
            if new_median == -1:
                exit()
            log.write(f"Median is: {new_median}\n")
            if new_median == arr[L]:
                arr[L], arr[median] = arr[median], arr[L]
            elif new_median == arr[R]:
                arr[R], arr[median] = arr[median], arr[R]
            log.write("Updated array: "+" ".join([str(x) for x in arr])+"\n")
            medianSort(arr, L, median)
            medianSort(arr, median, R)
'''


TEST, N, Q = [int(x) for x in input().split()]

for _ in range(TEST):
    solve(N, Q)
