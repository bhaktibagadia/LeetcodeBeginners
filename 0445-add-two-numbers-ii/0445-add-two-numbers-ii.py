# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def findnum(ll):
            num=0
            mul=1
            temp=ll
            while temp:
                num=(num*10+temp.val)
                temp=temp.next
            return num
        num1=findnum(l1)
        num2=findnum(l2)
        sumnum=num1+num2
        sumlist=[]
        while sumnum:
            digit=sumnum%10
            sumlist.append(digit)
            sumnum//=10
        if not sumlist:
            return ListNode(0)
        head=ListNode(sumlist.pop())
        temp=head
        while sumlist:
            newnode=ListNode(sumlist.pop())
            temp.next=newnode
            temp=temp.next
        return head    