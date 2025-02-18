"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def is_leaf(r, c, n):
            for i in range(r, r + n):
                for j in range(c, c + n):
                    if grid[i][j] != grid[r][c]: return False
            return True


        def helper(r, c, n):
            if is_leaf(r, c, n): return Node(grid[r][c], True, None, None, None, None)
            n //= 2
            top_left = helper(r, c, n)
            top_right = helper(r, c + n, n)
            bottom_left = helper(r + n, c, n)
            bottom_right = helper(r + n, c + n, n)
            return Node(1, False, top_left, top_right, bottom_left, bottom_right)
        
        return helper(0, 0, len(grid))
        