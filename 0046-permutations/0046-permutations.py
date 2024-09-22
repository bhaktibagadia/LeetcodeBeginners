class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def rec(ind):
            if ind==len(nums)-1:
                ans.append(nums[:])
                return
            for i in range(ind, len(nums)):
                nums[ind], nums[i] = nums[i], nums[ind]
                rec(ind+1)
                nums[i], nums[ind] = nums[ind], nums[i]
        ans = []
        rec(0)
        return ans
