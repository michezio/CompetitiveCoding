class Solution:
    def possibleBipartition(self, N: int, dis: list[list[int]]) -> bool:
        while dis:
            dis.sort(key=lambda x: x[0])
            g1 = set()
            g2 = set()
            g1.add(dis[0][0])
            g2.add(dis[0][1])
            rem = []
            # previous = dis[0][0]
            # a1, a2 = True, False
            for el in dis[1:]:
                a = el[0]
                b = el[1]
                # if a != previous:
                a1, a2 = (True, False) if a in g1 else (
                    (False, True) if a in g2 else (False, False))
                b1, b2 = (True, False) if b in g1 else (
                    (False, True) if b in g2 else (False, False))
                if (a1 and b1) or (a2 and b2):
                    return False
                elif (a1 and b2) or (a2 and b1):
                    continue
                else:
                    if a1:
                        g2.add(b)
                    elif a2:
                        g1.add(b)
                    else:
                        if b1:
                            g2.add(a)
                        elif b2:
                            g1.add(a)
                        else:
                            rem.append(el)
                # previous = a
            dis = rem
        return True
