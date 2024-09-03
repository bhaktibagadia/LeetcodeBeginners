class Solution:
    def getLucky(self, s: str, k: int) -> int:
        number = ''
        for char in s:
            number+=str(ord(char)-ord('a')+1)
        while k>0:
            temp = 0
            for num in number:
                temp+=int(num)
            k-=1
            number = str(temp)
        return int(number)            