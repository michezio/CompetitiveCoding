class Solution:
    def intervalIntersection(
            self, A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
        AA = []
        for a in A:
            AA.extend(a)
        BB = []
        for b in B:
            BB.extend(b)
        RES = []
        sA = False
        sB = False
        sI = False
        ia, ib = 0, 0
        while ia < len(AA) and ib < len(BB):
            selected = min(AA[ia], BB[ib])
            if(AA[ia] == BB[ib] and sA != sB):
                RES.extend([selected, selected])
            if selected == AA[ia]:
                sA = not sA
                ia += 1
            if selected == BB[ib]:
                sB = not sB
                ib += 1
            bk = sI
            sI = sA and sB
            if sI != bk:
                RES.append(selected)
        E = []
        for i in range(len(RES)//2):
            E.append([RES[i*2], RES[i*2+1]])

        return E
