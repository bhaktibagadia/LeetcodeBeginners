# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2=0,0
        temp=l1
        i=1
        while temp:
            num1+=(temp.val*i)
            i*=10
            temp=temp.next
        temp=l2
        i=1
        while temp:
            num2+=(temp.val*i)
            i*=10
            temp=temp.next
        ans=num1+num2
        newnode=ListNode(ans%10)
        ans//=10
        curr=newnode
        while ans:
            curr.next=ListNode(ans%10)
            ans//=10
            curr=curr.next
        return newnode    
