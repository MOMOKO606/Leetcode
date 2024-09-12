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
                self.second = node
                if not self.first: self.first = self.prev
            self.prev = node
            if self.first and self.second: print(self.first.val, self.second.val, self.prev.val)
            helper(node.right)


        self.first, self.second, self.prev = None, None, None
        helper()
        self.first.val, self.second.val = self.second.val, self.first.val
        