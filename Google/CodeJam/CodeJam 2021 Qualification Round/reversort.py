def solve(arr):
    total = 0
    for i in range(len(arr)):
        minVal = min(arr[i:])
        x = arr[i:].index(minVal)
        reverse(arr, i, x+i)
        total += x+1
        #print(f"DEBUG #{i}: {arr[i:]}, min: {minVal}, cost: {x+1}")
    return total-1

def reverse(arr, i, j):
    for x in range((j-i+1)//2):
        arr[i+x], arr[j-x] = arr[j-x], arr[i+x]

TEST = int(input())

for case in range(TEST):
    num = int(input())
    arr = [int(x) for x in input().split()]
    res = solve(arr)
    print(f"Case #{case+1}: {res}")