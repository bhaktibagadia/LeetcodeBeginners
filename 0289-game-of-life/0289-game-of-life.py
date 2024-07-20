class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==0:
                    board[i][j]=-2
                else:
                    board[i][j]=-1

        def countones(r, c):
            cnt=0
            directions=[(1,0), (0, 1), (-1, 0), (0, -1), (1, -1), (-1, 1), (1, 1), (-1,-1)]
            for delrow, delcol in directions:
                if 0<=r+delrow<len(board) and 0<=c+delcol<len(board[0]) and (board[r+delrow][c+delcol]==-1 or board[r+delrow][c+delcol]==1):
                    cnt+=1
            return cnt

        for i in range(len(board)):
            for j in range(len(board[0])):
                val=board[i][j]
                if board[i][j]==-1 and 2<=countones(i, j)<=3:
                    board[i][j]=abs(val)
                elif board[i][j]==-2 and countones(i, j)==3:
                    board[i][j]=abs(val)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]>0:
                    board[i][j]=1
                else:
                    board[i][j]=0


        