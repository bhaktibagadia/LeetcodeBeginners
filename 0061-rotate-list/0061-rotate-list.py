# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        cnt = 1
        temp = head
        while temp.next:
            cnt+=1
            temp = temp.next
        temp.next = head    
        k=k%cnt
        k=cnt - k
        temp = head
        for _ in range(k-1):
            temp = temp.next
        
        head = temp.next  
        temp.next = None
        return head  
