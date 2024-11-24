# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node=root):
            if not node: return 
            helper(node.right)
            node.val += self.total
            self.total = node.val
            helper(node.left)

        self.total = 0
        helper()
        return root


        