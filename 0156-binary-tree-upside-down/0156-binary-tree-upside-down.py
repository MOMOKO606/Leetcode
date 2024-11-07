# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        if not root.left and not root.right: return root
        left, right = root.left, root.right
        newRoot = self.upsideDownBinaryTree(root.left)
        left.right, left.left, root.left, root.right = root, right, None, None
        return newRoot


        