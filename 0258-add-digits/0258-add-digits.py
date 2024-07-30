class Solution:
    def addDigits(self, num: int) -> int:
        if num<=9:
            return num
        while num>9:
            sumnum=0
            while num:
                sumnum+=(num%10)
                num//=10
            num=sumnum    
        return sumnum      