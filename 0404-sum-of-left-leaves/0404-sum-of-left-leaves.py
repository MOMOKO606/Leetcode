# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def helper(node=root, parent=None):
            if not node: return 0
            if not node.left and not node.right:
                return node.val if parent and parent.left == node else 0
            return helper(node.left, node) + helper(node.right, node)
        return helper()

        