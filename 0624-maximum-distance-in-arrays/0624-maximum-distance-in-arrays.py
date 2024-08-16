class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        yetmax, yetmin = arrays[0][-1], arrays[0][0]
        ans = 0
        for array in arrays[1:]:
            tempmax, tempmin = array[-1], array[0]
            ans = max(ans, abs(yetmax-tempmin), abs(tempmax-yetmin))  
            yetmin = min(yetmin, tempmin)
            yetmax = max(yetmax, tempmax)
        return ans    