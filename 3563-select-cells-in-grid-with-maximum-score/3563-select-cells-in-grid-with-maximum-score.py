class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        def dfs_helper(i=0):
            if i == len(remain): return 0
            ans = -inf
            for row in val_to_rows[remain[i]]:
                if row not in visited:
                    visited.add(row)
                    ans = max(ans, remain[i] + dfs_helper(i + 1))
                    visited.remove(row)
            return ans if ans != -inf else dfs_helper(i + 1)

        
        rows, cols, val_to_rows = len(grid), len(grid[0]), collections.defaultdict(set)
        for i in range(rows):
            for j in range(cols):
                val_to_rows[grid[i][j]].add(i)
        remain, visited = sorted(list(val_to_rows.keys()), reverse=True), set()
        return dfs_helper()
        