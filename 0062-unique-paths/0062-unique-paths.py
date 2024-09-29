class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def rec(i, j):
            if i>=m or j>=n:
                return 0
            if i==m-1 and j==n-1:
                return 1
            if (i, j) in dp:
                return dp[(i,j)]    
            down = rec(i+1, j)
            right = rec(i, j+1)
            dp[(i, j)] = down+right
            return dp[(i,j)]

        dp = {}
        return rec(0,0)            