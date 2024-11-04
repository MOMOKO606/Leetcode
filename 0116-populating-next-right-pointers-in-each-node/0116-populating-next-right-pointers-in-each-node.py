"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return root
        queue = [root]
        while queue:
            nextQueue = []
            for prev, cur in zip(queue, queue[1:] + [None]): prev.next = cur
            for node in queue:
                if node.left: nextQueue.append(node.left)
                if node.right: nextQueue.append(node.right)
            queue = nextQueue
        return root

        