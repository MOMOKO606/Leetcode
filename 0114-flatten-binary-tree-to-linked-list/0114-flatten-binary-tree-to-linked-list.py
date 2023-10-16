# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(root):
            if not root: return
            
            self.cur, left, right = root, root.left, root.right
            if self.prev: self.prev.left, self.prev.right = None, self.cur
            self.prev = self.cur

            helper(left)
            helper(right)

        self.prev, self.cur = None, None
        helper(root)
        