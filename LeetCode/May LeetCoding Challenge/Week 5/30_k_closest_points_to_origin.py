class Solution:
    def kClosest(self, points: list[list[int]], K: int) -> list[list[int]]:
        points.sort(key=lambda x: x[0]*x[0] + x[1]*x[1])
        return points[:K]
