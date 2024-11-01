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
        def helper(node=root):
            if not node: return 
            helper(node.left)
            if self.prev and self.prev.val > node.val:
                if not self.left:
                    self.left = self.prev
                self.right = node
            self.prev = node
            helper(node.right)

        self.prev, self.left, self.right = None, None, None
        helper()
        self.left.val, self.right.val = self.right.val, self.left.val
        