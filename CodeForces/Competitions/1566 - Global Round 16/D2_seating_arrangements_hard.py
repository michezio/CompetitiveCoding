
TESTS = int(input())

for t in range(TESTS):
	n, m = map(int, input().split())
	people = list(map(int, input().split()))
	
	seats = people.copy()
	seats.sort()
	
	lookup = {}
	for i, s in enumerate(seats):
		if s not in lookup.keys():
			lookup[s] = [i]
		else:
			lookup[s].append(i)
	
	inconvenience = 0
	grid = [[0]*m for i in range(n)]
	
	for key in lookup.keys():
		lookup[key].sort(key=lambda x: -100000*(x//m) + (x%m))
	
	for p in people:
		index = lookup[p].pop(-1)
		nn = index//m
		mm = index%m
		
		grid[nn][mm] = 1
		inconvenience += grid[nn][:mm].count(1)
	
	print(inconvenience)
		
	
