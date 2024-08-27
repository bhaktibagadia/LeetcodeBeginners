class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = []
        for i in range(n):
            friends.append(i+1)
        j = 0    
        while len(friends)!=1:
            j =  (j+k-1)%(len(friends))
            friends.remove(friends[j])
        return friends[0]       