class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def rec(i, k):
            if i==1:
                return '0'
            length = int(2**i - 1)
            mid = length//2 + 1
            if k==mid:
                return '1'
            elif k<mid:
                return rec(i-1, k)
            else:
                mirror = length-k+1
                bit = rec(i-1, mirror)
                return '1' if bit == '0' else '0'
        return rec(n, k)                   