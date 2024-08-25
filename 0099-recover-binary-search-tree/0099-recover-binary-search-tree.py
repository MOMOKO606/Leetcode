# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(node):
            if not node: return
            helper(node.left)
            if self.prev and self.prev.val > node.val:
                if self.left: self.right = node
                else: self.left, self.right = self.prev, node
            self.prev = node
            helper(node.right)

        self.left, self.right, self.prev = None, None, None
        helper(root)
        self.left.val, self.right.val = self.right.val, self.left.val
        