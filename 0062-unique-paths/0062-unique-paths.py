class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def rec(r, c):
            if 0>r or r>=m or c<0 or c>=n:
                return 0
            if r==m-1 and c==n-1:
                return 1
            if  dp[r][c]!=-1:
                return dp[r][c]
            right = rec(r+1, c)
            bottom = rec(r, c+1)
            dp[r][c] = right+bottom
            return dp[r][c]

        dp = [[-1]*n for _ in range(m)]
        ans = rec(0,0)
        return ans           