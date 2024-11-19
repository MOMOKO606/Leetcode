"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return root
        queue, ans = [root], []
        while queue:
            nextQueue = []
            ans.append([node.val for node in queue])
            for node in queue:
                for child in node.children:
                    nextQueue.append(child)
            queue = nextQueue
        return ans
