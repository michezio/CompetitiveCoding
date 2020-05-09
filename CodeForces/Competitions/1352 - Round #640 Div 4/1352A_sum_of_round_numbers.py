TEST = int(input())

answers = []
for _ in range(TEST):
    num = int(input())
    st_num = str(num)
    init = 1
    ans = []
    for c in st_num[::-1]:
        if c != '0':
            ans.append(int(c)*init)
        init *= 10

    answers.append(ans)

for ans in answers:
    print(len(ans))
    print(*ans)
