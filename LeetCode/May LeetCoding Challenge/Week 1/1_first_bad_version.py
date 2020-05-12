# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool


def isBadVersion(version):
    pass


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        last_true = 0
        def binarySearch(a, b):
            nonlocal last_true
            if a >= b:
                if isBadVersion(a):
                    last_true = a
                    return
            c = (b+a)//2
            if isBadVersion(c):
                last_true = c
                binarySearch(a, c-1)
            else:
                binarySearch(c+1, b)
        '''
        a = 1
        b = n
        last_true = 0
        while (a <= b):
            c = (a+b)//2
            res = isBadVersion(c)
            if res:
                last_true = c
                b = c-1
            else:
                a = c+1

        return last_true


''' C++ CODE
class Solution {
public:
    int firstBadVersion(int n) {
        long a = 1;
        long answer = 0;
        while (a <= n) {
            long c = (a+n)/2;
            if (isBadVersion(c)) {
                answer = c;
                n = c-1;
            }
            else a = c+1;
        }
        return answer;
    }
};
'''
