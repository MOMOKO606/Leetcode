# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def helper(prev=None, node=root):
            if not node: return 0
            if prev and prev.left == node and not node.left and not node.right: return node.val
            ans = 0
            ans += helper(node, node.left)
            ans += helper(node, node.right)
            return ans
        return helper()


        