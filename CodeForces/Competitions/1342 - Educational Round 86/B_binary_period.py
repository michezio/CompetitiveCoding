TESTS = int(input())

answers = []

for _ in range(TESTS):
    s = input()
    res = ''
    if s.find('0') != -1 and s.find('1') != -1:
        res = '10'*len(s) if s[-1] == '0' else '01'*len(s)
    else:
        res = s
    answers.append(res)

for ans in answers:
    print(ans)
