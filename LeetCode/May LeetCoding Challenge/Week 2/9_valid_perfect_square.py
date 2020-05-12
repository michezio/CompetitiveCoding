class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        r = num**0.5
        return r == int(r)
