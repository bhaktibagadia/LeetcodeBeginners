# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        temp = head
        lengthofLL = 0   
        while temp:
            lengthofLL+=1
            temp=temp.next
        num = lengthofLL//k
        rem = lengthofLL%k
        res = []
        curr = head
        for i in range(k):
            temphead = curr
            tempsize = num + (1 if rem>0 else 0)
            rem-=1

            for _ in range(tempsize-1):
                if curr:
                    curr = curr.next

            if curr:
                tempnext = curr.next
                curr.next = None
                curr = tempnext
            res.append(temphead)
        return res                

