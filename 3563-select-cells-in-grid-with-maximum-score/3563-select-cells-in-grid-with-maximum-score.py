class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        @cache
        def helper(i=0, cur_total=0):
            if i == rows: return cur_total
            ans = -inf
            for j in range(cols):
                if grid[i][j] in visited: continue
                visited.add(grid[i][j])
                ans = max(ans, helper(i + 1, cur_total + grid[i][j]))
                visited.remove(grid[i][j])
            return ans if ans != -inf else cur_total + helper(i + 1)

        rows, cols, visited = len(grid), len(grid[0]), set()
        return helper()

        