class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def rec(i, ds):
            if i==len(nums):
                if ds not in ans:
                    ans.append(ds[:])
                return
            ds.append(nums[i])    
            rec(i+1, ds)
            ds.pop()
            rec(i+1, ds)
        nums.sort()    
        rec(0, [])
        ans.sort()
        return ans        
                