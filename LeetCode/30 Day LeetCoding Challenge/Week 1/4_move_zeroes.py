class Solution:
    def moveZeroes(self, nums):
        set_position = 0
        for i in range(set_position, len(nums)):
            if nums[i] != 0:
                temp = nums[i]
                nums[i] = nums[set_position]
                nums[set_position] = temp
                set_position += 1
