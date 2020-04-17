class Solution:
    def maxSubArray(self, nums):
        best = float("-inf")
        sub = 0
        for n in nums:
            sub += n
            if (sub < n):
                sub = n
            if (sub > best):
                best = sub
        return best

    '''
    Kadane's algorithm
    '''
