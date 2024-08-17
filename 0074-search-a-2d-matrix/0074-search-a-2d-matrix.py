class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binSearch(arr):
            low, high = 0, len(arr)-1
            while low<=high:
                mid = (low+high)//2
                if arr[mid]==target:
                    return True
                elif arr[mid]<target:
                    low=mid+1 
                else:
                    high = mid -1
            return False

        for m in matrix:
            if m[0]<=target<=m[-1]:
                return binSearch(m)
        return False                           