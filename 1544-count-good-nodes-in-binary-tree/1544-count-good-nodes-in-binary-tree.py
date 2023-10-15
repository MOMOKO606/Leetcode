# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node, maxSoFar):
            if not node: return 0
            if node.val >= maxSoFar: 
                maxSoFar = node.val
                return 1 + helper(node.left, maxSoFar) + helper(node.right, maxSoFar)
            return helper(node.left, maxSoFar) + helper(node.right, maxSoFar)

        return helper(root, -math.inf)