'''
The previous solution for problem 17 works too
but is extremely slow in this case
'''


class Solution:
    def checkInclusion(self, match: str, string: str) -> bool:
        if len(match) > len(string):
            return False

        p = [0 for x in range(26)]
        asc = lambda x: ord(x)-97

        for x in match:
            p[asc(x)] += 1

        left = 0
        right = len(match)

        for c in range(right):
            p[asc(string[c])] -= 1

        if all(x == 0 for x in p):
            return True

        while (right < len(string)):
            p[asc(string[left])] += 1
            left += 1
            p[asc(string[right])] -= 1
            right += 1
            if all(x == 0 for x in p):
                return True

        return False
