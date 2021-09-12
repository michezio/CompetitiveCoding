import math


TESTS = int(input())

for t in range(TESTS):
	n, s = map(int, input().split())
	median = math.ceil(n/2)
	nright = n - (median-1)
	m = s // nright
	print(m)
