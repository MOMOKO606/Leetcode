# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return 
        k = inorder.index(preorder[0])
        return TreeNode(preorder[0], self.buildTree(preorder[1:k + 1], inorder[:k]), self.buildTree(preorder[k + 1:], inorder[k + 1:]))
        