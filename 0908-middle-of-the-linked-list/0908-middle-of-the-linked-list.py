# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        temp = head
        cnt = 0
        while temp:
            cnt+=1
            temp = temp.next
        cnt = cnt//2
        temp = head
        while cnt and temp.next:
            temp = temp.next
            cnt -= 1
        return temp       