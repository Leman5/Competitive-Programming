class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts = horizontalCuts + [0] + [h]
        verticalCuts = verticalCuts + [0] + [w]

        horizontalCuts.sort()
        verticalCuts.sort()

        maxH = 0
        maxW = 0
        for i in range(1, len(horizontalCuts)):
            maxH = max(maxH, horizontalCuts[i] - horizontalCuts[i - 1])

        for i in range(1, len(verticalCuts)):
            maxW = max(maxW, verticalCuts[i] - verticalCuts[i - 1])

        return (maxH * maxW) % (pow(10, 9) + 7)
        