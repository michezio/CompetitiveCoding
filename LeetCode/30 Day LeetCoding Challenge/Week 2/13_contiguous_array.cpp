#include <vector>

using namespace std;

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

/* GOOD SOLUTION PYTHON (STILL SLOWER THAN AVERAGE)
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
*/

/* LESS SLOW SOLUTION (BUT STILL TLE)
def findFirst(nums, n):
    ind = None
    try:
        ind = nums.index(n)
    except ValueError:
        return None
    return ind


def findLast(nums, n):
    ind = None
    try:
        ind = len(nums) - 1 - nums[::-1].index(n)
    except ValueError:
        return None
    return ind


class Solution:
    def findMaxLength(self, nums):
        subsums = []
        for c in nums:
            if len(subsums) == 0:
                subsums.append(1 if c is 1 else -1)
            else:
                last = subsums[-1]
                new = last + (1 if c is 1 else -1)
                subsums.append(new)
        max_length = 0
        elements = set(subsums)
        for e in elements:
            if subsums.count(e) > 1 or e == 0:
                indF = -1
                indL = len(subsums) - 1
                if e == 0:
                    indF = -1
                    indL = findLast(subsums, e)
                else:
                    indF = findFirst(subsums, e)
                    indL = findLast(subsums, e)
                diff = indL - indF
                max_length = max(max_length, diff)
        return max_length
*/

/* SLOW SOLUTION (TLE)
class Solution:
    def findMaxLength(self, nums):
        found = False
        size = len(nums)
        begin = 0
        while(not found):
            while(begin+size <= len(nums)):
                a = nums[begin:begin+size]
                zeros = a.count(0)
                ones = a.count(1)
                if zeros == ones:
                    found = True
                    break
                else:
                    begin += 1
            if found:
                break
            begin = 0
            size -= 1
        return size
*/
