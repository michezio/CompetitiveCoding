import re

html = input()
a = re.findall(r'<[^<]+?>', html)
stack = []
tags = 0
for i in range(len(a)):
    x = a[i]
    if "/" in x:
        b = "<" + x[2:]
        if b == stack[-1]:
            stack.pop(-1)
            tags += 1
        else:
            print("Broken")
            exit()
    else:
        stack.append(x)

if len(stack) > 0:
    print("Broken")
else:
    print(tags)

#print(a)
