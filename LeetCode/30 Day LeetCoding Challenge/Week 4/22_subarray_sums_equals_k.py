class Solution:
    def subarraySum(self, nums, k):
        pref = [0]
        dp = {0: 1}
        count = 0
        for i in range(len(nums)):
            pref.append(pref[-1] + nums[i])
            e = pref[-1]
            if e-k in dp:
                count += dp[e-k]
            if e in dp:
                dp[e] += 1
            else:
                dp[e] = 1
        return count
