# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(node, head):
            if not node:
                return False
            if not head.next:
                return True
            right, left = False, False
            if node.left and head.next and node.left.val == head.next.val:
                left = dfs(node.left, head.next)
            if node.right and head.next and node.right.val == head.next.val:
                right = dfs(node.right, head.next)  
            return left or right

        if not root:
            return False
        if root.val == head.val:
            if dfs(root, head):
                return True
        return self.isSubPath(head,root.left) or self.isSubPath(head, root.right)                              