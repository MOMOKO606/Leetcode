"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return
        clones, queue = {node.val: Node(node.val, [])}, [node]
        while queue:
            nextQueue = []
            for curNode in queue:
                for neighbor in curNode.neighbors:
                    if neighbor.val not in clones:
                        clones[neighbor.val] = Node(neighbor.val, [])
                        nextQueue.append(neighbor)
                    clones[curNode.val].neighbors.append(clones[neighbor.val])
            queue = nextQueue
        return clones[node.val]        
        

        