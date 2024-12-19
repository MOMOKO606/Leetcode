# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node=root):
            if not node: return
            helper(node.right)
            if self.prev: node.val += self.prev.val
            self.prev = node
            helper(node.left)

        self.prev = None
        helper()
        return root
        

        