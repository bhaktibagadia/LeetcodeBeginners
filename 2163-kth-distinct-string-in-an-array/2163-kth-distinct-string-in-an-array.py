class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        for a in arr:
            if arr.count(a)==1:
                k-=1
            if k==0:
                return a
        return ""            