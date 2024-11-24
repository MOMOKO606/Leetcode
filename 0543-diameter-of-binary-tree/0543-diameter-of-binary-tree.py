# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(node=root):
            if not node: return 0
            l, r = helper(node.left), helper(node.right)
            self.ans = max(self.ans, l + r + 1)
            return 1 + max(l, r)

        
        self.ans = 0
        helper()
        return self.ans - 1
        