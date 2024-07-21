class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diagonals=defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                diagonals[i-j].append(mat[i][j])
        for key in diagonals:
            diagonals[key].sort()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j]=diagonals[i-j].pop(0)
        return mat        
        
            