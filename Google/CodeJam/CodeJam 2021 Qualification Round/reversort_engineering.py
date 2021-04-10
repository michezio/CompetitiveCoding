def solve(size, cost):
    if cost < size-1 or cost > size*(size+1)//2-1:
        return ["IMPOSSIBLE"]
    
    arr = list(range(1, size+1))
    if cost == size-1:
        return arr
    # caso in cui cost > size-1 and cost < size*(size-1)//2
    rimanente = size-1
    pos = 0
    operations = []
    cost = cost - rimanente
    while cost > 0:
        cost += rimanente
        rimanente -= 1
        cost -= rimanente
        op = min(cost, len(arr)-pos)
        #reverse(arr, pos, pos+op-1)
        operations.append([pos, pos+op-1])
        cost -= op
        pos += 1
        #print(f">> Rim: {rimanente}, Op: {op}, Cost: {cost}")
        #print(arr)
    for op in operations[::-1]:
        reverse(arr, op[0], op[1])
    return arr

    
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
    size, cost = [int(x) for x in input().split()]
    res = solve(size, cost)
    print(f"Case #{case+1}: ", end="")
    print(*res)
1

