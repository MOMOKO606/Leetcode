class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        def dfs_helper(i=0, visited=set()):
            if i == len(remain): return 0
            ans = -inf
            for row in val_to_rows[remain[i]]:
                if row not in visited:
                    ans = max(ans, remain[i] + dfs_helper(i + 1, visited | {row}))
            return ans if ans != -inf else dfs_helper(i + 1, visited)

        
        rows, cols, val_to_rows = len(grid), len(grid[0]), collections.defaultdict(set)
        for i in range(rows):
            for j in range(cols):
                val_to_rows[grid[i][j]].add(i)
        remain = sorted(list(val_to_rows.keys()), reverse=True)
        return dfs_helper()
        