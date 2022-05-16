from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]:
            return -1
        queue = collections.deque([(0,0,1)])
        while queue:
            i, j, count = queue.popleft()
            if i == len(grid)-1 and j == len(grid[0])-1:
                return count
            for x, y in ((0,1), (0,-1), (1,0), (-1,0), (1,-1), (-1,1), (1,1), (-1,-1)):
                row, col = i + y, j + x
                if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and not grid[row][col]:
                    queue.append((row, col, count+1))
                    grid[row][col] = 1
        return -1