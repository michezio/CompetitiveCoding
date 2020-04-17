import bisect


class Solution:
    def lastStoneWeight(self, stones):
        stones.sort()
        while(len(stones) > 1):
            m = stones.pop()
            s = stones.pop()
            m -= s
            if m != 0:
                bisect.insort(stones, m)
        if len(stones) > 0:
            return stones[0]
        else:
            return 0
