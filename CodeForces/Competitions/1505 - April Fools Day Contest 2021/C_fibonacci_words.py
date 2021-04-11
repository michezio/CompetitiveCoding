def getIndex(lett):
	return ord(lett)-65

word = input()

if len(word) < 3:
	print("YES")
	exit()

a = getIndex(word[0])
b = getIndex(word[1])

for c in word[2:]:
	p = getIndex(c)
	if p != (a + b) % 26:
		print("NO")
		exit()
	a = b
	b = p
print("YES")