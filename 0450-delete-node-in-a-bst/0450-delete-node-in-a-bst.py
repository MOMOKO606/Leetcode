# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def successorVal(node):
            node, val = node.right, node.val
            while node:
                node, val = node.left, node.val
            return val

        def predecessorVal(node):
            node, val = node.left, node.val
            while node:
                node, val = node.right, node.val
            return val

        if not root: return 
        if root.val < key: root.right = self.deleteNode(root.right, key)
        elif root.val > key: root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right: return 
            elif root.right:
                root.val = successorVal(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = predecessorVal(root)
                root.left = self.deleteNode(root.left, root.val)
        return root

    
        