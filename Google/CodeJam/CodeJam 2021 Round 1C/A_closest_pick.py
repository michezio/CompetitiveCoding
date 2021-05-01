def solve(nums, k):
    nums = list(set(nums))
    nums.sort()

    #print(nums)

    ranges = []
    monoranges = [0]
    for i in range(len(nums)-1):
        a = nums[i]
        b = nums[i+1]
        if b-a > 1:
            ranges.append((b-a)//2)
            monoranges.append(b-a-1)

    if nums[0] != 1:
        ranges.insert(0, nums[0]-1)
    if nums[-1] != k:
        ranges.append(k-nums[-1])

    #print(ranges)

    #ranges = list(map(lambda x: (1+x)//2, ranges))
    #print(ranges)

    ranges.sort(reverse=True)
    #print(ranges)
    #print(monoranges)

    res = 0
    if len(ranges) > 0:
        res += ranges[0]
    if len(ranges) > 1:
        res += ranges[1]

    res = max(res, max(monoranges))

    res = res / float(k)
    return res


TEST = int(input())
for i in range(TEST):
    n, k = map(int, input().split())
    nums = map(int, input().split())
    res = solve(nums, k)
    print(f"Case #{i+1}: {res}")