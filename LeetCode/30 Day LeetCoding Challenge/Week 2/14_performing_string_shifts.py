class Solution:
    def stringShift(self, s, shift):
        pos = 0
        limit = len(s)
        for sh in shift:
            pos += sh[1] if sh[0] == 0 else -sh[1]
        pos = (pos % limit) if pos > 0 else (limit - abs(pos) % limit)
        newstr = s[pos:] + s[:pos]
        return newstr
