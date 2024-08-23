# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []
        def func(root):
            if not root:
                return
            func(root.left)
            inorder.append(root.val)
            func(root.right)
        func(root)
        return inorder              