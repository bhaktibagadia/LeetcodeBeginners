class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def rec(i, j):
            if i<0 or i>=len(obstacleGrid) or j<0 or j>=len(obstacleGrid[0]) or obstacleGrid[i][j]==1:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if i==len(obstacleGrid)-1 and j==len(obstacleGrid[0])-1:
                return 1    

            right = rec(i+1, j)
            down = rec(i, j+1)

            dp[i][j]=right+down

            return dp[i][j]

        dp=[[-1]*len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        return rec(0,0)
                