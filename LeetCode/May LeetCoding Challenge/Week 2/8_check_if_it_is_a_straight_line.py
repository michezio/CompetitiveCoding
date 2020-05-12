class Solution:
    def checkStraightLine(self, coo: list[list[int]]) -> bool:
        if len(coo) == 2:
            return True
        vertical = coo[0][0] == coo[1][0]
        slope = lambda a, b: (b[1] - a[1]) / (b[0] - a[0])
        coeff = slope(coo[0], coo[1]) if not vertical else 0
        for i in range(1, len(coo) - 1):
            if vertical and coo[i][0] == coo[0][0]:
                continue
            elif coo[i][0] == coo[i + 1][0] \
                    or slope(coo[i], coo[i + 1]) != coeff:
                return False
        return True
