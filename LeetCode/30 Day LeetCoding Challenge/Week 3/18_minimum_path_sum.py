class Solution:
    def minPathSum(self, grid):
        n = len(grid)
        m = len(grid[0])
        
        inf = 10e9
        
       	length = []

       	for y in range(n):
            length.append([])
            for x in range(m):
                left = length[y][x-1] if x > 0 else inf
                up = length[y-1][x] if y > 0 else inf
                prev = min(left, up) if x + y > 0 else 0
                length[y].append(prev + grid[y][x])
       	
        return length[-1][-1]