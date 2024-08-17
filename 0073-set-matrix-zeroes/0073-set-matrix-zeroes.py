class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = [0]*len(matrix)
        column = [0]*len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row[i]=1
                    column[j]=1

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row[i] or column[j]:
                    matrix[i][j]=0                        