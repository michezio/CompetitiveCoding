class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.append(0)
        '''
        for i in range(len(nums)//2):
            p = i*2
            if nums[p] != nums[p+1]:
                return nums[p]
        '''
        right = len(nums) // 2 - 1
        left = 0
        found = 1
        while (left <= right):
            c = (left + right) // 2
            p = c * 2
            if nums[p] == nums[p + 1]:
                left = c + 1
            else:
                found = nums[p]
                right = c - 1
        return found
