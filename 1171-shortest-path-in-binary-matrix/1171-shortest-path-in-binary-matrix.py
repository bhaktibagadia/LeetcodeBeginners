class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        dir = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

        queue = deque([(0,0,1)])
        grid[0][0]=1

        while queue:
            i, j, path = queue.popleft()
            if i==n-1 and j==n-1:
                return path
            for di, dj in dir:
                deli = di+i
                delj = dj+j
                if 0<=deli<n and 0<=delj<n and grid[deli][delj]==0:
                    queue.append((deli, delj, path+1))
                    grid[deli][delj] = 1
        return -1            
