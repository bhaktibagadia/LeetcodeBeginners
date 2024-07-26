class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def rec(i,stack, sumofstack):
            if sumofstack==target:
                return ds.append(stack[:])
            if i==len(candidates):
                return
            if sumofstack>target:
                return
            nottake = rec(i+1, stack, sumofstack)
            if sumofstack<target:
                stack.append(candidates[i])
                take = rec(i, stack,sumofstack+candidates[i])
                stack.pop()
        ds=[]
        rec(0, [], 0)
        return ds 