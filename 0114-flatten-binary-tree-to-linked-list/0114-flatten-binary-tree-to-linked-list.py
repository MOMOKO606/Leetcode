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
        def helper(node):
            if not node: return
            left, right = node.left, node.right
            if self.prev:
                self.prev.left, self.prev.right = None, node
            self.prev = node
            helper(left)
            helper(right)

        self.prev = None
        helper(root)

        
        