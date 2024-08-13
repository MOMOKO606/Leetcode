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
        def isLeaf(r, c, n):
            for i in range(r, r + n):
                for j in range(c, c + n):
                    if grid[i][j] != grid[r][c]: return False
            return True


        def helper(r, c, n):
            if isLeaf(r, c, n): return Node(grid[r][c], True, None, None, None, None)
            n //= 2
            topLeft = helper(r, c, n)
            topRight = helper(r, c + n, n)
            bottomLeft = helper(r + n, c, n)
            bottomRight = helper(r + n, c + n, n)
            return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)

        return helper(0, 0, len(grid))
        