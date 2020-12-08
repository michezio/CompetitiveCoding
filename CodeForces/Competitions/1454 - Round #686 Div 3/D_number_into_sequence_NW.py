import math

def isPrime(num):
	if num == 2:
		return True
	for i in range(2, math.ceil(math.sqrt(num))+1):
		if (num%i == 0):
			return False
	return True

TESTS = int(input())

answers = []

for _ in range(TESTS):
	num = int(input())

	if isPrime(num):
		answers.append([1, [num]])
		continue

	res = []
	val = 2
	last = None
	n = num

	while val <= math.ceil(math.sqrt(num))+1:
		if n % val == 0 and (len(res) == 0 or val % res[-1] == 0):
			res.append(val)
			last = n
			n //= val
		else:
			val += 1

	res[-1] = last

	answers.append([len(res), res])

for ans in answers:
	print(ans[0])
	print(*ans[1])
