class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def rec(target):
            if target=="":
                return True
            if target in dp:
                return dp[target]
            for word in wordDict:
                if target[:len(word)]==word and rec(target[len(word):]):
                    dp[target] = True
                    return dp[target]
            dp[target] = False
            return dp[target]

        dp={}
        return rec(s)            
