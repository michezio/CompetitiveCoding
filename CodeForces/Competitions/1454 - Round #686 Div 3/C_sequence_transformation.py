TESTS = int(input())

answers = []

for _ in range(TESTS):
	n = int(input())
	lis = [int(x)-1 for x in input().split()]

	cnt = [None for _ in range(n)]
	equals = True
	for i, el in enumerate(lis):
		if i > 0 and lis[i] == lis[i-1]:
			continue
		cnt[el] = cnt[el]+1 if cnt[el] is not None else 1
		equals = False

	
	if equals:
		answers.append(0)
		continue

	cnt[lis[0]] -= 1
	cnt[lis[-1]] -= 1

	ops = min([x for x in cnt if x is not None]) + 1

	answers.append(ops)

for ans in answers:
	print(ans)