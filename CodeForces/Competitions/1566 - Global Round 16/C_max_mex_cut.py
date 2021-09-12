TESTS = int(input())

for t in range(TESTS):
	size = int(input())
	A = [int(x) for x in input()]
	B = [int(x) for x in input()]
	
	mex = 0
	previous = -1
	for i in range(size):
		a, b = A[i], B[i]
		if a != b:
			mex += 2
			previous = -1
			continue
		if a+b == 0:
			mex += 1
			if previous == 1:
				mex += 1
				previous = -1
			else:
				previous = 0
		if a+b == 2:
			if previous == 0:
				mex += 1
				previous = -1
			else:
				previous = 1
	print(mex)
