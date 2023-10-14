# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, left, right):
            if not node: return True
            return left < node.val < right and helper(node.left, left, node.val) and helper(node.right, node.val, right)
        return helper(root, -math.inf, math.inf)
        