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
                if not self.first: self.first = self.prev
                self.second = node
            self.prev = node
            helper(node.right)
        
        
        self.first, self.second, self.prev = None, None, None
        helper(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        