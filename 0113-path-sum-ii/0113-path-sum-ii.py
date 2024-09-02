# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def helper(node, seq, targetSum):
            if not node: return
            if not node.left and not node.right and node.val == targetSum:
                self.ans.append(seq + [node.val])
                return
            helper(node.left, seq + [node.val], targetSum - node.val)
            helper(node.right, seq + [node.val], targetSum - node.val)

        self.ans = []
        helper(root, [], targetSum)
        return self.ans

        