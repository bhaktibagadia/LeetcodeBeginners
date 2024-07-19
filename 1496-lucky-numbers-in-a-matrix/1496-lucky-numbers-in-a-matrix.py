class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        for i in range(len(matrix)):
            minarray = min(matrix[i])
            indexofmin = matrix[i].index(minarray)
            if minarray == max(matrix[j][indexofmin] for j in range(len(matrix))):
                ans.append(minarray)
        return ans
