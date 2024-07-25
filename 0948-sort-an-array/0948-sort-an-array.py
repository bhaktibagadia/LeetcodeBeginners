class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(left, right):
            l, r = 0, 0
            sortedarray=[]

            while l<len(left) and r<len(right):
                if left[l]<right[r]:
                    sortedarray.append(left[l])
                    l+=1
                else:
                    sortedarray.append(right[r])
                    r+=1
            while l<len(left):
                sortedarray.append(left[l])
                l+=1
            while r<len(right):
                sortedarray.append(right[r])
                r+=1
            return sortedarray 

        if len(nums)<=1:
            return nums
        mid=len(nums)//2
        lefthalf=self.sortArray(nums[:mid])
        righthalf=self.sortArray(nums[mid:])
        return merge(lefthalf, righthalf)