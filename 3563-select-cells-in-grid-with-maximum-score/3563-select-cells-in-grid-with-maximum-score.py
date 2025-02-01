class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        def dfs(i):
            if i == len(remain): return 0
            value = remain[i]
            ans = -inf
            for row in val_to_rows[value]:
                if row not in row_set:
                   row_set.add(row)
                   ans = max(ans, value + dfs(i + 1))
                   row_set.remove(row)
            return ans if ans != -inf else dfs(i + 1)

        rows, cols, val_to_rows = len(grid), len(grid[0]), defaultdict(set)
        for i in range(rows):
            for j in range(cols):
                val_to_rows[grid[i][j]].add(i)
        remain, row_set = sorted(list(val_to_rows.keys()), reverse=True), set()
        return dfs(0)