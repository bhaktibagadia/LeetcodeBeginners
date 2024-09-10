# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def getGCD(a,b):
            while a>0 and b>0:
                if a>b:
                    a=a%b
                else:
                    b = b%a
            if a==0:
                return b
            return a                
        prev = head
        curr = prev.next
        while curr:
            gcdnode = ListNode(0)
            gcdnode.val = getGCD(prev.val, curr.val)
            prev.next = gcdnode
            gcdnode.next = curr
            prev = curr
            curr = curr.next
        return head    