class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def rec(idx, temp):
            if idx==len(nums):
                if sorted(temp) not in ans:
                    ans.append(sorted(temp[:]))
                return
            temp.append(nums[idx])    
            rec(idx+1,temp) 
            temp.pop()
            rec(idx+1,temp)
        rec(0, [])
        return sorted(ans)    