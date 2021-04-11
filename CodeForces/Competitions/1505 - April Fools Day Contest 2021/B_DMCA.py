a = input()
while len(a) > 1:
	a = str(sum((int(x) for x in a)))
print(a)