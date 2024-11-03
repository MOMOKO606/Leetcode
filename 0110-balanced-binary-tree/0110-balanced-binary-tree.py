# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node: return [0, True]
            lHeight, isLeftBalanced = helper(node.left)
            rHeight, isRightBalanced = helper(node.right)
            return [1 + max(lHeight, rHeight), abs(lHeight - rHeight) < 2 and isLeftBalanced and isRightBalanced]

        _, ans = helper(root)
        return ans

        