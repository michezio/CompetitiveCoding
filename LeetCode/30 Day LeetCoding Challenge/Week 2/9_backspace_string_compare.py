class Solution:
    def backspaceCompare(self, S, T):
        S = list(S)
        T = list(T)
        runnerS = 0
        for c in S:
            if c == "#":
                runnerS = max(0, runnerS - 1)
            else:
                S[runnerS] = c
                runnerS += 1

        runnerT = 0
        for c in T:
            if c == "#":
                runnerT = max(0, runnerT - 1)
            else:
                T[runnerT] = c
                runnerT += 1

        if runnerS != runnerT:
            return False
        else:
            for i in range(runnerS):
                if S[i] != T[i]:
                    return False

        return True


''' C++ CODE
public:
    bool backspaceCompare(string S, string T) {

        int runnerS = 0;
        for (char c : S) {
            if (c == '#')
                runnerS = max(0, runnerS - 1);
            else {
                S[runnerS] = c;
                runnerS++;
            }
        }

        int runnerT = 0;
        for (char c : T) {
            if (c == '#')
                runnerT = max(0, runnerT - 1);
            else {
                T[runnerT] = c;
                runnerT += 1;
            }
        }

        if (runnerS != runnerT)
            return false;
        else
            for (int i=0; i<runnerS; i++)
                if (S[i] != T[i])
                    return false;

        return true;
    }
};
'''
