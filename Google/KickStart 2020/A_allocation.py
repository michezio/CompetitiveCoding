def compute(budget, costs):
    costs.sort()
    houses = []
    total = 0
    while(costs):
        total += costs[0]
        if (total > budget):
            break
        else:
            houses.append(costs.pop(0))
    return len(houses)

results = []

cases_num = int(input())

for i in range(cases_num):
    num_houses, budget = [int(s) for s in input().split(" ")]
    costs = [int(c) for c in input().split(" ")]
    results.append(compute(budget, costs))

case = 1
for num in results:
    print("Case #{}: {}".format(case, num))
    case += 1
