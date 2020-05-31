class Solution:
    def countBits(self, num: int) -> list[int]:
        arr = [0, 1]
        if num < 2:
            return arr[:num+1]
        basin = 2
        for i in range(2, num+1):
            if i == basin << 1:
                basin = basin << 1
            arr.append(arr[i % basin] + 1)
        return arr
