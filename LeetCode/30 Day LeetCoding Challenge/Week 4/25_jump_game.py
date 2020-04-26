class Solution:
    def canJump(self, nums):
        index = len(nums)-1
        if index == 0:
            return True
        if nums[0] == 0:
            return False
        while(index >= 0):
            if nums[index] == 0:
                jump = 1 if index == len(nums)-1 else 2
                index -= 1
                while(nums[index] < jump):
                    index -= 1
                    jump += 1
                    if index == -1:
                        return False
            else:
                index -= 1
        return True
