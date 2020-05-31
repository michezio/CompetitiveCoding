class Solution:
    def countSquares(self, m: list[list[int]]) -> int:
        height = len(m)
        width = len(m[0])
        total = 0
        for y in range(height):
            for x in range(width):
                if m[y][x]:
                    if y > 0 and x > 0:
                        m[y][x] = 1 + min(m[y-1][x-1], m[y-1][x], m[y][x-1])
                    total += m[y][x]
        return total
