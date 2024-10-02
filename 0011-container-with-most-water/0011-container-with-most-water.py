class Solution:
    def maxArea(self, height: List[int]) -> int:
        right,left=len(height)-1, 0
        maxarea=0
        while left<=right:
            area=(right-left)*min(height[right],height[left])
            maxarea=max(maxarea, area)
            if height[left]<=height[right]:
                left+=1
            else:
                right-=1
        return maxarea            