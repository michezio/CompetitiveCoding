class Solution:
    def longestCommonSubsequence(self, a, b):
        dp = [[0 for x in range(len(a)+1)] for y in range(len(b)+1)]
        for y in range(1, len(b)+1):
            for x in range(1, len(a)+1):
                dp[y][x] = dp[y-1][x-1] + 1 if a[x-1] == b[y-1] \
                    else max(dp[y-1][x], dp[y][x-1])
        return dp[-1][-1]

    ''' LONG VERSION
    def longestCommonSubsequence(self, a, b):
        if a == b:
            return len(a)
        itr, st = (a, b) if len(a) <= len(b) else (b, a)
        dp = [[0 for x in range(len(a))] for y in range(len(b))]
        for y in range(len(b)):
            for x in range(len(a)):
                if y == 0:
                    if x == 0:
                        dp[0][0] = int(a[0] == b[0])
                    else:
                        dp[0][x] = max(dp[0][x-1], int(a[x] == b[0]))
                else:
                    if x == 0:
                        dp[y][0] = max(dp[y-1][0], int(a[0] == b[y]))
                    else:
                        if a[x] == b[y]:
                            dp[y][x] = dp[y-1][x-1] + 1
                        else:
                            dp[y][x] = max(dp[y-1][x], dp[y][x-1])
        return dp[-1][-1]
    '''

    ''' C++ CODE
    int longestCommonSubsequence(string text1, string text2) {
        int s1 = text1.size();
        int s2 = text2.size();
        int dp[s1+1][s2+1];
        for (int i=0; i<=s1; i++) dp[i][0] = 0;
        for (int i=0; i<=s2; i++) dp[0][i] = 0;
        for (int y=1; y<=s1; y++)
            for (int x=1; x<=s2; x++)
                dp[y][x] = text1[y-1] == text2[x-1] ?
                    dp[y-1][x-1] + 1 : max(dp[y][x-1], dp[y-1][x]);
        return dp[s1][s2];
    }
    '''

    '''
    NW SOLUTION
    def longestCommonSubsequence(self, a, b):
        if a == b:
            return len(a)
        itr, st = (a, b) if len(a) <= len(b) else (b, a)
        max_len = 0
        for i in range(len(itr)):
            if len(itr[i:]) <= max_len:
                return max_len
            ptr = -1
            new_len = 0
            for k in itr[i:]:
                fnd = st.find(k, ptr+1)
                if fnd != -1:
                    ptr = fnd
                    new_len += 1
            max_len = max(max_len, new_len)
        return max_len
    '''
