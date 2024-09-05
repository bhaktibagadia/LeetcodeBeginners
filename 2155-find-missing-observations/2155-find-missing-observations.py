class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # mean = sum(rolls)+summ//len(rolls)+n
        summ = (mean*(len(rolls)+n))-sum(rolls)
        ans = []
        if not n<=summ<=6*n:
            return ans
        temp = summ//n
        ans = [temp]*n
        rem = summ%n
        for i in range(rem):
            ans[i]+=1
        return ans       
