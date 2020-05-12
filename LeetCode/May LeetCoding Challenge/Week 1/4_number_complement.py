class Solution:
    def findComplement(self, num: int) -> int:
        # return num ^ int('0b'+'1'*(len(bin(num))-2),2)
        return num ^ ((1 << (len(bin(num)) - 2)) - 1)


''' C++ CODE
class Solution {
public:
    int findComplement(int num) {
        long len = 0;
        long p = num;
        while(p != 0) {
            p = p >> 1;
            len++;
            }
        return ((1<<len)-1) - num;
    }
};
'''
