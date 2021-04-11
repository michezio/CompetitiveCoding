a, b = map(int, input().split())

cake = []

for _ in range(a):
	cake.append([x for x in input()])

count = 0
x, y = 0, 0

while x < b and y < a:
	if cake[y][x] == "*":
		count += 1
	if x < b-1 and cake[y][x+1] == "*":
		x += 1
	elif y < a-1 and cake[y+1][x] == "*":
		y += 1
	else:
		x += 1
		if x == b:
			x -= 1
			y += 1

print(count)