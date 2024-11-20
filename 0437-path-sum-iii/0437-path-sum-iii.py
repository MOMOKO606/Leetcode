# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def helper(node):
            if not node: return 
            self.preSum += node.val
            self.ans += self.preSums.get(self.preSum - targetSum, 0)
            self.preSums[self.preSum] = self.preSums.get(self.preSum, 0) + 1
            helper(node.left)
            helper(node.right)
           
            self.preSums[self.preSum] -= 1
            self.preSum -= node.val
        
        self.preSums, self.preSum, self.ans = {0: 1}, 0, 0
        helper(root)
        return self.ans

        