TESTS = int(input())

for t in range(TESTS):
	s = [int(x) for x in input()]
	#print("DEBUG", s)
	prev = -1
	elements = []
	for x in s:
		if x != prev:
			elements.append(x)
			prev = x
	mex = min(2, elements.count(0))
	print(mex)
	
