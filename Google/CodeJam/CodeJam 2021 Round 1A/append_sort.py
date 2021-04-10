def solve(nums):
	ops = 0
	prev = int(nums[0])

	for n in nums[1:]:
		while prev >= int(n):
			prv = str(prev)
			if len(prv) == len(n):
				ops += 1
				n = n + "0"
			elif int(prv[:len(n)]) != int(n):
				ops += len(prv)-len(n)
				n = n + "0"*(len(prv)-len(n))
			elif int(prv[:len(n)]) == int(n):
				st = prv[len(n):]
				for i in range(len(st)-1, -1, -1):
					if st[i] != "9":
						st = st[:i] + str(int(st[i])+1)
						n = n + st
						ops += len(st)
						break
				else:
					ops += len(st)+1
					n = n + "0"*(len(st)+1)
			else:
				if int(prv[:-1]) < int(n):
					n = n + "0"
				else:
					dig = prv[len(n)]
					n = n + str((int(dig)+1)%10)
				ops += 1
		prev = int(n)
		#print(n, end=" ")
	return ops


TEST = int(input())
for i in range(TEST):
	n = int(input())
	nums = input().split()
	res = solve(nums)
	print(f"Case #{i+1}: {res}")