def shuffle(dec):
    b = bin(dec)
    b = b[2:]
    while(len(b) < 6):
        b = '0' + b
    b = b[::-1]

    new = [b[5], b[0], b[2], b[3], b[1], b[4]]

    n = ""
    for el in new:
        n += el

    res = int("0b" + n, 2)
    return res


w = int(input())

print(shuffle(w))
