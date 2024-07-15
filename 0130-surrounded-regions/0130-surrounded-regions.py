class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(r,c):
            vis[r][c]=1
            for k in range(4):
                drow, dcol = r+delrow[k], c+delcol[k]
                if 0<=drow<m and 0<=dcol<n and not vis[drow][dcol] and board[drow][dcol]=='O':
                    dfs(drow,dcol)

        delrow=[0, -1, 0, 1]
        delcol=[1, 0, -1, 0]
        m,n = len(board), len(board[0])
        vis=[[0]*n for _ in range(m)]
        for i in range(m):
            if board[i][0]=='O':
                dfs(i,0)
        for i in range(m):
            if board[i][n-1]=='O':
                dfs(i, n-1)
        for i in range(n):
            if board[0][i]=='O':
                dfs(0, i)
        for i in range(n):
            if board[m-1][i]=='O':
                dfs(m-1, i)    

        for i in range(m):
            for j in range(n):
                if board[i][j]=='O' and not vis[i][j]:
                    board[i][j]='X'
