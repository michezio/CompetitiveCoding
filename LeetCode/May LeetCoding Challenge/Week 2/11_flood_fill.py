class Solution:
    def floodFill(self, image: list[list[int]], sr, sc, newColor) \
            -> list[list[int]]:
        H = len(image)
        W = len(image[0])
        oldColor = image[sr][sc]
        isFloodable = lambda x, y: \
            0 <= x < W and 0 <= y < H and image[y][x] == oldColor

        def flood(x, y):
            if isFloodable(x, y):
                image[y][x] = newColor
                flood(x - 1, y)
                flood(x + 1, y)
                flood(x, y - 1)
                flood(x, y + 1)

        if newColor == oldColor:
            return image

        flood(sc, sr)

        return image
