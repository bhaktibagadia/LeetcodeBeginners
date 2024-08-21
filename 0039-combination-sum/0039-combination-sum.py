class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def rec(i, ds, summ):
            if i==len(candidates):
                return
            if summ ==  target:
                ans.append(ds[:])
                return
            if summ+candidates[i]<=target:    
                ds.append(candidates[i])
                summ+=candidates[i]
                rec(i, ds, summ)
                summ-=candidates[i]
                ds.pop()
            rec(i+1, ds, summ)  
        rec(0, [], 0)
        return ans          