# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helper(node=root):
            if not node or self.count > k: return
            helper(node.left)
            self.count += 1
            if self.count == k: 
                self.ans = node.val
                return 
            helper(node.right)
        
        self.count = 0
        helper()
        return self.ans
        