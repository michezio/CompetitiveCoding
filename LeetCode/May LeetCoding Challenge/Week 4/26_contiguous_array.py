class Solution:
    def findMaxLength(self, nums):
        for i in range(len(nums)):
            nums[i] = 2*nums[i]-1 + (nums[i-1] if i-1 >= 0 else 0)
        hsm = {}
        max_length = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                max_length = max(max_length, i+1)
            elif nums[i] in hsm.keys():
                max_length = max(max_length, i - hsm[nums[i]])
            else:
                hsm[nums[i]] = i
        return max_length


''' C++ SOLUTION
class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        int minV = 100000;
        int maxV = -100000;
        if (nums.size() == 0)
            return 0;
        for (int i=0; i<nums.size(); ++i) {
            nums[i] = 2*nums[i]-1 + (i-1 >= 0 ? nums[i-1] : 0);
            minV = min(minV, nums[i]);
            maxV = max(maxV, nums[i]);
        }
        int hsm[maxV-minV+1];
        for (int i=0; i<maxV-minV+1; ++i) {
            hsm[i] = -1;
        }
        int max_length = 0;
        for (int i=0; i<nums.size(); ++i) {
            if (nums[i] == 0)
                max_length = max(max_length, i+1);
            else if (hsm[nums[i] - minV] != -1)
                max_length = max(max_length, i - hsm[nums[i] - minV]);
            else
                hsm[nums[i] - minV] = i;
        }
        return max_length;
    }
};
'''
