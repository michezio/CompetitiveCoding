class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= k:
            return '0'
        ls = [x for x in num]

        i = 0
        while i < (len(ls)-1):
            if ls[i] > ls[i+1]:
                ls.pop(i)
                k -= 1
                i = i-1 if i > 0 else 0
                if k == 0:
                    break
            else:
                i += 1
        if k > 0:
            ls = ls[:-k]

        ans = ''.join(ls).lstrip('0')

        return ans if len(ans) else '0'
