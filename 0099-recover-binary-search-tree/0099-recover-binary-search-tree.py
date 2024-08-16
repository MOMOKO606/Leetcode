# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(node):
            if not node: return []
            return helper(node.left) + [node.val] + helper(node.right)

        def helper2(node):
            if not node: return
            helper2(node.left)
            if node.val == left: node.val = right
            elif node.val == right: node.val = left
            helper2(node.right)
      
        nums = helper(root)
        sorted_nums = sorted(nums)
        for num1, num2 in zip(nums, sorted_nums):
            if num1 != num2: 
                left = num1
                break
        for num1, num2 in zip(reversed(nums), reversed(sorted_nums)):
            if num1 != num2: 
                right = num1
                break
        helper2(root)

        
 

