'''
Apparently doesn't work, don't know why it seems correct to me 
¯\\_(ツ)_/¯
'''

def solve(line, rev):
	arr = list(map(int, line.split()))
	if rev == True:
		arr = arr[::-1]
	diff = [arr[i]-arr[i+1] for i in range(len(arr)-1)]
	diff.insert(0, None)
	subfwd = [1, 2]
	subbwd = [1, 2]
	maxfwd = []
	for i in range(2, len(arr)):
		if diff[i] == diff[i-1]:
			subfwd.append(subfwd[-1]+1)
		else:
			if subfwd[-1] > 1:
				maxfwd.append(i-1)
			if subfwd[-1] == 1:
				subfwd.append(2)
			else:
				subfwd.append(1)
	if subfwd[-1] > 1:
		maxfwd.append(len(arr)-1)

	for i in range(len(arr)-3, -1, -1):
		if diff[i] == diff[i+1]:
			subbwd.append(subbwd[-1]+1)
		else:
			#if subbwd[-1] > 1:
				#maxbwd.append(i+1)
			if subbwd[-1] == 1:
				subbwd.append(2)
			else:
				subbwd.append(1)

	#if subbwd[-1] > 1:
	#	maxbwd.append(0)
	subbwd = subbwd[::-1]

	maxres = 2

	for index in maxfwd:
		res = subfwd[index]
		if index < len(arr)-1:
			res += 1
		else:
			maxres = max(res, maxres)
			continue
		val = arr[index]-diff[index]
		if index+2 < len(arr) and val-arr[index+2] == diff[index]:
			res += 1
		if index+3 < len(arr) and diff[index+3] == diff[index]:
			res += subbwd[index+2]-1
		maxres = max(res, maxres)

	#print(diff)
	#print(subfwd)
	#print(subbwd)
	#print(maxres)
	return maxres
'''
	for index in maxbwd:
		res = subbwd[index]
		if index > 0:
			res += 1
		else:
			maxres = max(res, maxres)
			continue
		val = arr[index]-diff[index]
		if index-2 > 0 and arr[index-2]+val == diff[index]:
			res += 1
		if index-3 > 0 and diff[index-3] == diff[index]:
			res += subfwd[index-2]
		maxres = max(res, maxres)
'''


TEST = int(input())

for i in range(TEST):
	n = int(input())
	line = input()
	res1 = solve(line, rev=False)
	res2 = solve(line, rev=True)
	print(f"Case #{i+1}: {max(res1, res2)}")