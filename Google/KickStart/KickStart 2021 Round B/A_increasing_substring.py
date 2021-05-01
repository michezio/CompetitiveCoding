def solve(line):
	res = [1]
	for i, c in enumerate(line[1:]):
		if c > line[i]:
			res.append(res[-1]+1)
		else:
			res.append(1)

	return " ".join(map(str, res))



TEST = int(input())

for i in range(TEST):
	n = int(input())
	line = input()
	res = solve(line)
	print(f"Case #{i+1}: {res}")