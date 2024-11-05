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
        if not node: return node
        clones, queue, root = {node: Node(val=node.val, neighbors=[])}, [node], node
        while queue:
            nextQueue = []
            for node in queue:
                for neighbor in node.neighbors:
                    if neighbor not in clones:
                        nextQueue.append(neighbor)
                        clones[neighbor] = Node(val=neighbor.val, neighbors=[])
                    clones[node].neighbors.append(clones[neighbor])
            queue = nextQueue
        return clones[root]
        