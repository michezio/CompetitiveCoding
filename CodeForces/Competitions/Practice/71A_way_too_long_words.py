# https://codeforces.com/problemset/problem/71/A
# 71A Way Too Long Words

w = int(input())

while(w):
    w -= 1
    word = input()
    if (len(word) <= 10):
        print(word)
    else:
        word = word[0] + str(len(word[1:-1])) + word[-1]
        print(word)
