class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0]!=5:
            return False
        five, ten = 0,0
        for bill in bills:
            if bill == 5:
                five+=1   
            elif bill == 10:
                if five<1:
                    return False
                else:
                    five-=1
                ten+=1
            else:
                if five>0 and ten>0:
                    five-=1
                    ten-=1
                elif five>2:
                    five-=3
                else:
                    return False
        return True                                 