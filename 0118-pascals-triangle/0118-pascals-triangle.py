class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            row = []
            for j in range(i+1):
                row.append(factorial(i)//(factorial(j)*factorial(i-j)))
            ans.append(row)
        return ans        