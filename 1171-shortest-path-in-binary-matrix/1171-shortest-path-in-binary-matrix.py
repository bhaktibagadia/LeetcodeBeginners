from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        if n == 1:
            return 1 if grid[0][0] == 0 else -1

        # Directions for moving in 8 possible ways
        directions = [
            (1, 0), (1, 1), (0, 1), (-1, 1),
            (-1, 0), (-1, -1), (0, -1), (1, -1)
        ]

        # BFS setup
        queue = deque([(0, 0, 1)])  # (i, j, path_length)
        grid[0][0] = 1  # mark as visited

        while queue:
            i, j, path_length = queue.popleft()

            if i == n - 1 and j == n - 1:
                return path_length

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 0:
                    queue.append((ni, nj, path_length + 1))
                    grid[ni][nj] = 1  # mark as visited

        return -1
