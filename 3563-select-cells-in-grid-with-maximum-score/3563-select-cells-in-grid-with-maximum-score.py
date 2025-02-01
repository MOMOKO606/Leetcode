class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        rows, cols, val_to_rows = len(grid), len(grid[0]), defaultdict(set)
        for i in range(rows):
            for j in range(cols):
                val_to_rows[grid[i][j]].add(i)

  
        def dfs(row_set, remaining_values, score):
            if not remaining_values:
                return score

            value = remaining_values[0]
            remaining_values = remaining_values[1:]

            score_list = []

            for row in val_to_rows[value]:
                if row not in row_set:
                    score_list.append(dfs(row_set | {row}, remaining_values, score + value))
            if not score_list:
                score_list.append(dfs(row_set, remaining_values, score))
            return max(score_list)

        return dfs(set(), sorted(list(val_to_rows.keys()), reverse=True), 0)