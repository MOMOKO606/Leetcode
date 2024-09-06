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
        clones, queue, visited = {node: Node(val=node.val, neighbors=[])}, [node], set([node])
        while queue:
            next_queue = []
            for cur_node in queue:
                for neighbor in cur_node.neighbors:
                    if neighbor not in clones:
                        clones[neighbor] = Node(val=neighbor.val, neighbors=[])
                    clones[cur_node].neighbors.append(clones[neighbor])
                    if neighbor not in visited:
                        visited.add(neighbor)
                        next_queue.append(neighbor)
            queue = next_queue
        return clones[node]


        