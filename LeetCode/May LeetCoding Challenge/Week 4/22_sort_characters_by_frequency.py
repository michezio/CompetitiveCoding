class Solution:
    def frequencySort(self, s: str) -> str:
        ss = set([x for x in s])
        sl = []
        for c in ss:
            sl.append((c, s.count(c)))
        sl.sort(key=lambda x: -x[1])
        res = ""
        for x in sl:
            res += x[0]*x[1]
        return res
