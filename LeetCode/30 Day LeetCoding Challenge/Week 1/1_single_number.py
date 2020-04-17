class Solution:
    def singleNumber(self, nums):
        return 2*sum(set(nums)) - sum(nums)

    ''' BEST SOLUTION
    def singleNumber(self, nums):
        a = 0
        for n in nums:
            a = a ^ n   # XOR
        return a
    '''
