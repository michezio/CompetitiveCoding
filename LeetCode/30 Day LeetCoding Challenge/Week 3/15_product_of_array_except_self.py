class Solution:
    def productExceptSelf(self, nums):
        pre = [1]
        post = [1]
        for i in range(1, len(nums)):
            pre.append(pre[-1] * nums[i-1])
            post.append(post[-1] * nums[-i])
        return [pre[i] * post[-i-1] for i in range(len(nums))]
