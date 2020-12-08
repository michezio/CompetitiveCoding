class Solution:
    def isHappy(self, n):
        nums = set()
        while (n not in nums):
            nums.add(n)
            strn = str(n)
            s = 0
            for d in [int(x) for x in strn if x != 0]:
                s += d**2
            if (s == 1):
                return True
            else:
                n = s
        return False
