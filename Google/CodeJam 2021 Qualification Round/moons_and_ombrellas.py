def compress(string):
    res=""
    prv = string[0]
    if prv != "?":
        res += prv
    count = 1 if prv == "?" else 0
    for i in range(1, len(string)):
        act = string[i]
        if act == "?":
            count += 1
        else:
            if count > 0:
                res += " " + str(count) + " "
                count = 0
            if act != prv:
                res += act
        prv = act
    if count > 0:
        res += " " + str(count)
    return res.strip()

def score(A, B, num, cj, jc):
    score = 10e10
    if num % 2 == 0:
        # pari interrogativi init CJ
        nCJ = num//2
        nJC = num//2 - 1
        if A == "J":
            nJC += 1
        if B == "C":
            nJC += 1
        score = min(score, nCJ*cj + nJC*jc)
        # pari interrogativi init JC
        nCJ = num//2 - 1
        nJC = num//2
        if A == "C":
            nCJ += 1
        if B == "J":
            nCJ += 1
        score = min(score, nCJ*cj + nJC*jc)
    if num % 2 != 0:
        # dispari interrogativi init CJ
        nCJ = num//2
        nJC = num//2
        if A == "J":
            nJC += 1
        if B == "J":
            nCJ += 1
        score = min(score, nCJ*cj + nJC*jc)
        # dispari interrogativi init JC
        nCJ = num//2
        nJC = num//2
        if A == "C":
            nCJ += 1
        if B == "C":
            nJC += 1
        score = min(score, nCJ*cj + nJC*jc)
    if A == "C" and B == "J":
        score = min(score, cj)
    if A == "J" and B == "C":
        score = min(score, jc)
    if A == B or A == None or B == None:
        score = min(score, 0)

    return score



def solve(line, cj, jc):
    #line = "".join(line.split("?"))
    if len(line) < 1:
        return 0
    line = compress(line).split(" ")
    total = 0
    for index, sub in enumerate(line):
        if sub[0].isdigit():
            total += score( None if index == 0 else line[index-1][-1],
                            None if index == len(line)-1 else line[index+1][0],
                            int(sub), cj, jc)
        else:
            prev = sub[0]
            for i in range(1, len(sub)):
                el = sub[i]
                if prev == "C" and el == "J":
                    total += cj
                if prev == "J" and el == "C":
                    total += jc
                prev = el
    return total

TEST = int(input())
for case in range(TEST):
    cj, jc, line = [x for x in input().split()]
    cj = int(cj)
    jc = int(jc)
    res = solve(line, cj, jc)
    print(f"Case #{case+1}: {res}")
