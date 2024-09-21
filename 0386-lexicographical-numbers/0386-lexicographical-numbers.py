class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        for i in range(1, n+1):
            ans.append(str(i))    
        ans.sort()
        for i in range(len(ans)):
            ans[i] = int(ans[i])
        return ans