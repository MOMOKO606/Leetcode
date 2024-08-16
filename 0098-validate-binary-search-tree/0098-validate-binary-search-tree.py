# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node=root, low=-inf, high=inf):
            if not node: return True
            if not (low < node.val < high): return False
            if not helper(node.left, low, node.val) or not helper(node.right, node.val, high): return False
            return True

        return helper()
            


        