class Solution:
    def canFinish(self, num: int, pre: list[list[int]]) -> bool:
        graph = [[False] for _ in range(num)]

        for a in pre:
            graph[a[0]].append(a[1])

        stack = []

        def dfs(node):
            if node in stack:
                return False
            if graph[node][0] is True:
                return True
            stack.append(node)
            graph[node][0] = True
            for el in graph[node][1:]:
                good = dfs(el)
                if not good:
                    return False
            stack.pop()
            return True

        good = True
        for i in range(len(graph)):
            if graph[i][0] is False:
                good = dfs(i)
                if not good:
                    return False
        return good
