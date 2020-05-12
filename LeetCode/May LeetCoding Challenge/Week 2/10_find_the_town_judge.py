class Solution:
    def findJudge(self, N: int, trust: list[list[int]]) -> int:
        '''
        if N == 1:
            return 1
        possible_judges = [0 for _ in range(N)]
        judges = set()
        for a in trust:
            possible_judges[a[0]-1] = -N
            if a[0] in judges:
                judges.remove(a[0])
            possible_judges[a[1]-1] += 1
            if possible_judges[a[1]-1] == N-1:
                judges.add(a[1])
        '''
        people = [0 for _ in range(N)]
        for a in trust:
            people[a[0] - 1] = -N
            people[a[1] - 1] += 1

        try:
            return people.index(N - 1) + 1
        except ValueError:
            return -1
