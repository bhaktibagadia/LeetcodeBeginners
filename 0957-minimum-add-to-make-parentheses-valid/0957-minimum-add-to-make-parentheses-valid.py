class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        for parenthesis in s:
            if not stack:
                stack.append(parenthesis)
            elif parenthesis=='(':
                stack.append(parenthesis)
            elif (stack[-1]==')' and stack):
                stack.append(parenthesis)
            else:
                stack.pop()     
        return len(stack)            