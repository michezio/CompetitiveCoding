class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        while len(word1) > 0 and len(word2) > 0 and word1[-1] == word2[-1]:
            word1 = word1[:-1]
            word2 = word2[:-1]

        while len(word1) > 0 and len(word2) > 0 and word1[0] == word2[0]:
            word1 = word1[1:]
            word2 = word2[1:]

        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))
        if word1 == word2:
            return 0

        dp = [[0 for i in range(len(word1)+1)] for j in range(len(word2)+1)]

        for x in range(len(word1)+1):
            dp[0][x] = x
        for y in range(len(word2)+1):
            dp[y][0] = y

        for y in range(len(word2)):
            for x in range(len(word1)):
                if word1[x] == word2[y]:
                    dp[y+1][x+1] = dp[y][x]
                else:
                    dp[y+1][x+1] = min(dp[y][x+1], dp[y+1][x], dp[y][x]) + 1

        return dp[-1][-1]
