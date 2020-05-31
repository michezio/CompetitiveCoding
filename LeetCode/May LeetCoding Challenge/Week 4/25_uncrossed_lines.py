class Solution:
    def maxUncrossedLines(self, A: list[int], B: list[int]) -> int:
        dp = [[0 for x in range(len(A)+1)] for y in range(len(B)+1)]
        # grid has one extra row and column to account for index -1
        # exploiting the python ability to wrap around with negative indexes
        # so there's no need to check if index are > 0
        for y in range(len(B)):
            for x in range(len(A)):
                if A[x] == B[y]:
                    dp[y][x] = dp[y-1][x-1] + 1
                else:
                    dp[y][x] = max(dp[y-1][x], dp[y][x-1])

        return dp[-2][-2]  # account for extra row and column
