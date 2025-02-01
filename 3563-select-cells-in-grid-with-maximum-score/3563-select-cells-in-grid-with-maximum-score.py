class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        def dfs(row_set, i):
            if i == len(remain): return 0
            value = remain[i]
            ans = -inf
            for row in val_to_rows[value]:
                if row not in row_set:
                   ans = max(ans, value + dfs(row_set | {row}, i + 1))
            return ans if ans != -inf else dfs(row_set, i + 1)

        rows, cols, val_to_rows = len(grid), len(grid[0]), defaultdict(set)
        for i in range(rows):
            for j in range(cols):
                val_to_rows[grid[i][j]].add(i)
        remain = sorted(list(val_to_rows.keys()), reverse=True)
        return dfs(set(), 0)