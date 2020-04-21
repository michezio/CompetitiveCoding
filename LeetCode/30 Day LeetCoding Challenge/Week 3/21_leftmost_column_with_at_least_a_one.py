# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#     def get(self, x: int, y: int) -> int:
#     def dimensions(self) -> list[]:


class Solution:
    def leftMostColumnWithOne(self, bm):
        r, c = bm.dimensions()
        x = c-1
        y = 0
        # debug
        while(x >= 0 and y < r):
            val = bm.get(y, x)
            if val == 1:
                x -= 1
            else:
                y += 1

        if (y == r and x >= 0) or (x < 0 and y < r):
            x += 1
        if x == c:
            return -1
        return x
