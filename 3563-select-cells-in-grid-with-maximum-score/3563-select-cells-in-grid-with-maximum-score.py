class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        def dfs(row_set, i, score):
            if i == len(remain): return score
            value = remain[i]
            ans = -inf
            for row in val_to_rows[value]:
                if row not in row_set:
                   ans = max(ans, (dfs(row_set | {row}, i + 1, score + value)))
            return ans if ans != -inf else dfs(row_set, i + 1, score)

        rows, cols, val_to_rows = len(grid), len(grid[0]), defaultdict(set)
        for i in range(rows):
            for j in range(cols):
                val_to_rows[grid[i][j]].add(i)
        remain = sorted(list(val_to_rows.keys()), reverse=True)
        return dfs(set(), 0, 0)