class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        cnt = 0
        d = set((x for x in J))
        for s in S:
            if s in d:
                cnt += 1
        return cnt
