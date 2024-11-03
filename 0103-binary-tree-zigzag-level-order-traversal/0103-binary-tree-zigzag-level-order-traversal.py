# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue, ans, isReverse = [root], [], False
        while queue:
            nextQueue = []
            if isReverse:
                ans.append([node.val for node in reversed(queue)])
            else:
                ans.append([node.val for node in queue])
            for node in queue:
                if node.left: nextQueue.append(node.left)
                if node.right: nextQueue.append(node.right)
            queue, isReverse = nextQueue, not isReverse
        return ans
        