class Solution:
    def numIslands(self, grid):
        if len(grid) == 0:
            return 0
        
        n = len(grid)
        m = len(grid[0])
        
        def flood(i, j):
            if grid[i][j] == '1':
                grid[i][j] = 1
                if i > 0:
                    flood(i-1, j)
                if j > 0:
                    flood(i, j-1)
                if i < n-1:
                    flood(i+1, j)
                if j < m-1:
                    flood(i, j+1)
                return True
            else:
                return False
            
        islands = 0
        for i in range(n):
            for j in range(m):
                if flood(i, j):
                    islands += 1

        return islands
