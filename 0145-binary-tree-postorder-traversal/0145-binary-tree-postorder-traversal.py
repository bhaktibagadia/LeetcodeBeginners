# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postorder = []
        def func(root):
            if not root:
                return
            func(root.left)
            func(root.right)
            postorder.append(root.val)
        func(root)
        return postorder        