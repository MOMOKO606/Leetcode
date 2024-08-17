# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def helper(left, right):
            if left > right: return [None]
            ans = []
            for val in range(left, right + 1):
                for l in helper(left, val - 1):
                    for r in helper(val + 1, right):
                        ans.append(TreeNode(val=val, left=l, right=r))
            return ans
        return helper(1, n)

        