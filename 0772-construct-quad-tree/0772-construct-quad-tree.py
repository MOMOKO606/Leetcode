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
        def is_leaf(row, col, n):
            for i in range(row, row + n):
                for j in range(col, col + n):
                    if grid[i][j] != grid[row][col]: return False
            return True

        def helper(row, col, n):
            if is_leaf(row, col, n):
                return Node(grid[row][col], True, None, None, None, None)
            n //= 2
            topLeft = helper(row, col, n)
            topRight = helper(row, col + n, n)
            bottomLeft = helper(row + n, col, n)
            bottomRight = helper(row + n, col + n, n)
            return Node(1, False, topLeft, topRight, bottomLeft, bottomRight) 

        return helper(row=0, col=0, n=len(grid))    

