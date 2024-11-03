# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return None
        target = preorder[0]
        i = inorder.index(target)
        return TreeNode(val=target, left=self.buildTree(preorder[1: i + 1], inorder[:i]), right=self.buildTree(preorder[i + 1:], inorder[i + 1:]))
        