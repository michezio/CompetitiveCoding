class Solution:
    def rangeBitwiseAnd(self, m, n):
        if n == m:
            return m & n
        diff = len(bin(n - m))-2
        res = ""
        bitM = bin(m)[2:-diff]
        bitN = bin(n)[2:-diff]
        if len(bitM) == 0:
            return 0
        for i in range(len(bitM)):
            res += '1' if (bitN[-i-1] == bitM[-i-1] == '1') else '0'
        return int(res[::-1], 2) << diff
