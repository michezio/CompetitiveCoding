class Solution:
    def firstUniqChar(self, s: str) -> int:
        index = -1
        appeared = set()
        for i in range(len(s)):
            c = s[i]
            if c in appeared:
                continue
            appeared.add(c)
            if s.count(s[i]) == 1:
                index = i
                break
        return index
