# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def helper(i, j):
            if i > j: return [None]
            ans = []
            for k in range(i, j + 1):
                for l in helper(i, k - 1):
                    for r in helper(k + 1, j):
                        ans.append(TreeNode(k, l, r))                
            return ans
        return helper(1, n)
                
        