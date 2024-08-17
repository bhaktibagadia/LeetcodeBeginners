class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dip = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i]<nums[i+1]:
                dip = i
                break
        if dip == -1:
            nums.reverse()
        else:            
            for i in range(len(nums)-1, -1, -1):   
                if nums[i]>nums[dip]:
                    nums[i], nums[dip] = nums[dip], nums[i]
                    break
        nums[dip+1:] = sorted(nums[dip+1:])                 
        