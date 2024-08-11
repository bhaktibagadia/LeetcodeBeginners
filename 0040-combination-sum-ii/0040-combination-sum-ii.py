class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def rec(i, tar, ds):
            if tar==0:
                ans.append(ds[:])
                return
            for j in range(i, len(candidates)):
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                if candidates[j]>tar:
                    break
                ds.append(candidates[j])
                rec(j+1, tar-candidates[j], ds)
                ds.pop()

        ans=[]
        candidates.sort()
        rec(0, target, [])
        return ans