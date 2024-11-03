# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def helper(node=root, targetSum=targetSum, seq=[]):
            if not node: return
            if not node.left and not node.right and node.val == targetSum:
                ans.append(seq + [node.val])
                return 
            helper(node.left, targetSum - node.val, seq + [node.val])
            helper(node.right, targetSum - node.val, seq + [node.val])

        ans = []
        helper()
        return ans
        