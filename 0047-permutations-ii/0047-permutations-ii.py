class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def rec(ind):
            if ind==len(nums)-1:
                if nums not in res:
                    res.append(nums[:])
                return
            for i in range(ind, len(nums)):
                nums[i], nums[ind] = nums[ind], nums[i]
                rec(ind+1)
                nums[i], nums[ind] = nums[ind], nums[i]
        rec(0)
        return res        
